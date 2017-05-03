# 总体设计要求
> Unity中各路径对应的移动端位置

#### iOS:
* Application.dataPath : Application/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/xxx.app/Data
* Application.streamingAssetsPath : Application/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/xxx.app/Data/Raw
* Application.persistentDataPath : Application/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/Documents
* Application.temporaryCachePath : Application/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/Library/Caches

#### Android:
* Application.dataPath :  /data/app/xxx.xxx.xxx.apk
* Application.streamingAssetsPath :  jar:file:///data/app/xxx.xxx.xxx.apk/!/assets
* Application.persistentDataPath :  /data/data/xxx.xxx.xxx/files
* Application.temporaryCachePath :  /data/data/xxx.xxx.xxx/cache
```

## 用例过程

> 开始

* 用例开始

> 云端书架浏览AR图书,下载
  
  * 按照原有逻辑在服务器请求数据,存到数据库中
  * 在服务器中按照AR图书的标识Url下载到本地
  * 解压到对应的路径上,这个路径是后续要传给unity读取资源的路径

```objc
  解压路径: (最终的文件所在位置) 例: 书名为 ARBookDemo
  Application/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/Documents/ARBookResources/ARBookDemo  
  
  ARBookDemo 对应的是服务器返回的bookUUID
```

> 打开图书

* 1. 首次打开图书,传资源路径到unity中
传从doc目录下的半个的路径, 在unity中拼接字符串,拼成资源的全路径

```objc
 extern "C"
{
    // 对Unity中的unityToIOS方法进行实现
    char * GetIOSParamsFromNative(){
    retrun "iOSParams";
    //例如: ARBookResources/ARBookDemo 
}
```
 
* 2.读取出版物级别的横竖屏设置,提示用户横竖屏显示,若设备的方向和设置的方向有差异,则用户旋转设备后加载unity


 
* 3.显示Unity主界面 
 
 
```objc
- (void)startUnity {
    if (isFirstStartUnity) {//第一次启动Unity       
    [self startUnity:[UIApplication sharedApplication]];
        isFirstStartUnity = NO;
    }else {//非第一次启动Unity
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
* 4.unity要提供的第一帧的方法 (暂时无用,后续有用在添加功能)

```objc
extern "C"
{
    void UpdateFirstFrame() {
//第一帧调用的方法
    }    
}
```

* unity中某些热区的点击事件 调用内核 这个位置要检测该本书是否已经下载 未下载要先提示到云端下载该本资源

```objc
extern "C"
{
    void UpdateFirstFrame(string bookId) {
        UnityAppController *appController =  (UnityAppController *)[UIApplication sharedApplication].delegate;
        [appController enterBookKernelWithBookId:bookId];
    }    
}

```

> 返回到书架

```objc
extern "C" {
void unityBackToShelf() {
UnityAppController *appController =  (UnityAppController *)[UIApplication sharedApplication].delegate;
[appController backToShelf];
}
}

```

> 循环往复 打开下一本书 给unity传该书的路径

## 功能选项

* 拍照合影功能
 
 
```objc
 extern "C" {
 void unitySendPicToNative(string picName) {
//将图片存到 Application.persistentDataPath/unityPictureTemp 目录下 然后存储到对应的位置后删除该目录下的文件
 } 
 }
 
```

* Unity中的报错显示

```objc
extern "C" {
// error 传过来的错误信息 可以是错误信息 也可以是一个包含错误信息的json串
void UnityReportError(string error) {
}
}

```

## 后续

* 退到后台通知到unity(暂定按照unity的原有功能使用)
 
* 分享,暂时不做等后期添加



