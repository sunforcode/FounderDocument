# Unity和Xcode项目融合全记录

选取的Unity项目为演示demo： vefuriaDemo

选取的Xcode项目为Mrc项目的最近最近一次提交

##第一步 Unity项目的一些设置

将unity项目导出成iOS的原生项目

需要注意的几个地方： 

* 在Player Settings 中设置scrit engine
* 设置unity中是否显示logo和设置自定义启动画面
* 设置bundleId等操作
* 设置unity项目支持的旋转方向，最好设置为四个方向都支持，以为2.0项目是支持旋转屏幕的，如果不选择四个方向的话可能出现崩溃的问题
* Target SDK 选择是模拟器运行还是真机运行

## 第二步 开始融合
### 1.在原生项目中添加unity项目的文件
* 原项目中创建一个LoadAR的文件夹
* 将对应的文件拖入到这个文件夹中
* MapFileParser.sh 这个文件在项目目录中没有显示，但是要放到LoadAR中

> * 导出来的Unity项目的项目结构如图所示，其中 QCAR Vuforia 和 data要用文件夹的形式添加到项目中
> * Classes和Libraries要用黄色文件夹 group添加到项目中 ，classes文件和原项目中的classes会造成冲突，所以改为UnityClasses，其中classes中文件特别多，拖入的时候会造成卡顿，需要一些耐心

###2.在原生项目中添加对应的框架
>对照着Unity项目中的框架一个个添加

###3.对应着unity项目修改BuildSettings
* 修改pch文件,将unity中的Prefix.pch中的代码全部复制到自己的E_Publishing_Prefix.pch中
* 修改Other Linker Flags 将unity中设置复制到原生项目中
* write link map file
* head search path
* libra search path
* Other C Flags 
* C++ language dialect
* C++ standard Library
* enable C++ runtime Types
* enable Object-c extensions
* overriding deprecated Objecet-c methods
* GCC_USE_INDIRECT_FUNCTION_CALLS
* UNITY_RUNTIME_VERSION
* UNITY_SCRIPTING_BACKEND

>注意修改路径的时候的修改正确

###4.修改Build Phases

>添加Run Script 对照图修改 注意修改路径 LoadAR

##第三步 修改编译报错

修改了C++11以后 所有的.mm文件的编译都将变严格,众多类型不匹配的问题需要修改

* Cannot use '@throw' with Objective-C exceptions disabled

> 将一步的修改 enable Object-c extensions 改回yes

* Unknown type name 'il2cpp_z_Byte'; did you mean 'il2cpp_z_uInt'?

> 直接编译器修改

##第四步
### 1.修改main
* 将unity项目中的maim.mm中的代码全部覆盖到原生项目的main.m中
* 将main.mm跟项目的关系解除或者直接删了
* 将main.m改为main.mm

##第五步 到此为止 build success

##第六步 修改Unity项目中的部分文件为arc编译(可选)
> 在unity项目中的build phases -> compile sources 搜索所有的.m 或者.mm 文件 在原有项目将对应的文件打上 -fobjc-arc

##第七步  自定义启动unity

到这里就可以在原生项目中直接运行unity的项目了,但是要做到自定启动unity还要做下一步的操作

###1.修改unity界面不自己立即启动
* 在UnityAppController.mm中修改

```objc
static bool	_startUnityScheduled	= true;//按照计划表来启动 ,true的话就是按照自定义时刻启动 默认是false
```
* 添加退出按钮

```objc 
extern "C"//这个方法是在unity中声明的第一帧调用的方法
{
    void UpdateFirstFrame() {
        UnityAppController *appController =  (UnityAppController *)[UIApplication sharedApplication].delegate;
        [appController addCustomBackToShelf];
    }
    // 对Unity中的unityToIOS方法进行实现
    
}
```
> 因为不知道怎么直接调用,所以用了这种间接的方法调用加载退出按钮

```objc
- (void)addCustomBackToShelf {
    UIButton *exitButton  = [[UIButton alloc]initWithFrame:CGRectMake(50, 50, 100, 30)];
    [exitButton setTitle:@"退出" forState:UIControlStateNormal];
    [exitButton addTarget:self action:@selector(didClickExit) forControlEvents:UIControlEventTouchUpInside];
    [_unityView addSubview:exitButton];
}
```


###2.自定义启动画面(自定义rootviewController)
```objc
@property(nonatomic, strong)UIViewController *nativeRootViewController;

- (void)applicationDidBecomeActive:(UIApplication*)application
{
    
    ::printf("-> applicationDidBecomeActive()\n");
    
    [self removeSnapshotView];
    //这就话就是自定义启动画面
    [self addCustomView];
    
    
    if(_unityAppReady)
    {
        if(UnityIsPaused() && _wasPausedExternal == false)
        {
            UnityWillResume();
            UnityPause(0);
        }
        UnitySetPlayerFocus(1);
    }
    else if(!_startUnityScheduled)
    {
        _startUnityScheduled = true;
        [self performSelector:@selector(startUnity:) withObject:application afterDelay:0];
    }
    
    _didResignActive = false;
}

- (void)addCustomView {
    //    userInfo = [UserInfo readLastLoginUser];
    self.window = [[UIWindow alloc]initWithFrame:[UIScreen mainScreen].bounds];
    NSString *storyBoardName =  isPad ? @"Main_iPad": @"Main_iPhone";
    
    UINavigationController *navigation = [[UIStoryboard storyboardWithName:storyBoardName bundle:nil] instantiateInitialViewController];
    self.nativeRootViewController = navigation;
    self.window.rootViewController = self.nativeRootViewController;
    [self.window makeKeyAndVisible];
    _rootController = self.nativeRootViewController;
}
```

### 3.自定义启动unity时刻

``` objc
- (void)startUnity {//先要在.h中声明
    if (isFirstStartUnity) {//第一次启动Unity
        [self startUnity:[UIApplication sharedApplication]];
        isFirstStartUnity = NO;
    }else {
        _window.rootViewController = _rootController;
        _rootView.hidden = NO;
        [_window makeKeyAndVisible];
        if (_didResignActive) {
            UnityPause(0);
            _didResignActive = NO;
        }
    }
}
```
退出到自定义界面

```objc
    //第一句话是要在别的控制器知道退出的事件,
    [[NSNotificationCenter defaultCenter]postNotificationName:@"exitUnity" object:nil];
    //下面是关键代码
    UnityPause(1);
    _didResignActive = YES;
    _window.rootViewController = self.nativeRootViewController;
    _rootView.hidden = YES;
    [_window makeKeyAndVisible];
}
```
###4.调用

```objc
   //需要把对应的控制器改为.mm
   #import "UnityAppController.h"

  [GetAppController() startUnity];
```


#附1: Unity和Xcode项目的互相调用
官方的[Unity文档](https://docs.unity3d.com/Manual/PluginsForIOS.html).

###1.unity调ios并传值

```C#
//unity脚本中的方法声明
[DllImport ("__Internal")]
private static extern string GetIOSParamsFromNative();
```


```objc
//ios中的实现
//声明
static char unityPath[2048]; 
char *unitymsg = NULL;
extern "C"
{
    // 对Unity中的unityToIOS方法进行实现
    char * GetIOSParamsFromNative(){        
        if(unitymsg == NULL)
        {
            unitymsg = (char *)calloc(1, 2048);
        }        
        memset(unitymsg, 0, 2048);
        strcpy(unitymsg, unityPath);        
        return unitymsg;
    }
}
```

>这个地方有几个问题要注意

* 不能直接传string对象,因为这个地方传的是指针,指针传过去了,但是指针对应的内存空间被释放,所以直接传值会报错,上面的方法是一位老司机教导我的<smile>
* 如果在unity中声明了,并不在ios中实现的话会报编译的错误

###2.ios调用unity
```
UnitySendMessage("GameObjectName1", "MethodName1", "Message to send");
```
> 第三个参数可以不传  
