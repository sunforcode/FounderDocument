# 记录研究project.pbxproj文件
### 目录节点
* PBXBuildFile 文件列表的一个索引,声明了(所有需要编译的文件的)唯一id 和 引用记录了引用ID
* PBXFileReference (记录了所有文件,包括.h和.m资源文件,框架等的具体信息)
* PBXFrameworksBuildPhase 添加了的框架会在这个地方显示
* PBXGroup 记录分组的信息,分组套分组一层层的记录下去
* PBXNativeTarget 这个地方记录的是具体target信息 项目文件中的

> Xcode中的 PROJECT 和 TARGETS区别 PROJECT 相当于一个基类,部分的配置可以再TARGETS中改变 说白了就是说 TARGETS是一个的实例对象

* PBXProject 上面讲到的PROJECT信息
* PBXResourcesBuildPhase 需要编译使用的资源文件 对应着build Phases-> Copy bundle Resources 
* PBXShellScriptBuildPhase 需要编译的脚本路径 对应着build Phases->Run Script
* PBXSourcesBuildPhase 具体编译的源码文件 对应着build Phases ->Compile Sources 
* PBXVariantGroup 这个里面的文件只有storyboard和launchScreen
* XCBuildConfiguration build Setting的设置 这里面有Project对应的setting 还有实例化的buildsetting 的设置
* XCConfigurationList 对上面的configuration的

### 新注意到的问题
* 在classes中的native文件夹中只导入了.cpp文件,并没有导入.h文件
* 在uuid 和后面的注释上必须有个空格 不然就会报错
* 后面的文件名称注释 不会被读取 是没有关系的
* 导入到了加入框架的部分

### 1. 增加一个新文件的操作
* 在PBXBuildFile中新增了一条记录: 

>

    2D4A21B01EA6FB09005F66D6 /* FirstViewController.m inSources */ = {
    isa = PBXBuildFile;
    fileRef = 2D4A21AF1EA6FB09005F66D6 /* FirstViewController.m */; 
    };
    
> 1.如果添加了-fobjc-arc 会在这个位置显示 settings =  
> 2.第一个id为该文件的id,会在PBXSourcesBuildPhase中用到(因为在这里是指向具体的文件),第二个fileRef 是在PBXFileReference中声明了的,在引用如Group中使用

     2D4A21B01EA6FB09005F66D6 /* FirstViewController.m in Sources */ = {
     isa = PBXBuildFile; 
     fileRef = 2D4A21AF1EA6FB09005F66D6/* FirstViewController.m */; 
     settings = {COMPILER_FLAGS = "-fobjc-arc"; }; 
     
* 在PBXFileReference中新增一条记录: 这个地方是文件的具体记录

>
 
   	2D4A21AF1EA6FB09005F66D6 /* FirstViewController.m */ = {
   	isa = PBXFileReference; 
   	fileEncoding = 4; 
   	lastKnownFileType = sourcecode.c.objc; 
   	name = FirstViewController.m; 
   	path = ../FirstViewController.m; 
   	sourceTree = "<group>"; 
   	};

* 在PBXGroup中添加一条记录,这个地方是引用记录

> 

	2D4A217A1EA6F991005F66D6 /* AutoDemo */ = {
			isa = PBXGroup;
			children = (
				2D4A21AE1EA6FB09005F66D6 /* FirstViewController.h */,
				2D4A21AF1EA6FB09005F66D6 /* FirstViewController.m */,
				2D4A217E1EA6F991005F66D6 /* AppDelegate.h */,
				2D4A217F1EA6F991005F66D6 /* AppDelegate.m */,
				2D4A21811EA6F991005F66D6 /* ViewController.h */,
				2D4A21821EA6F991005F66D6 /* ViewController.m */,
				2D4A21841EA6F991005F66D6 /* Main.storyboard */,
				2D4A21871EA6F991005F66D6 /* Assets.xcassets */,
				2D4A21891EA6F991005F66D6 /* LaunchScreen.storyboard */,
				2D4A218C1EA6F991005F66D6 /* Info.plist */,
				2D4A217B1EA6F991005F66D6 /* Supporting Files */,
			);
			path = AutoDemo;
			sourceTree = "<group>";
		};



* 在PBXSourcesBuildPhase中添加一个文件记录

> 

    2D4A21741EA6F991005F66D6 /* Sources */ = {
    isa = PBXSourcesBuildPhase;
    buildActionMask = 2147483647;
	files = (
		2D4A21831EA6F991005F66D6 /* ViewController.m in Sources */,
		2D4A21801EA6F991005F66D6 /* AppDelegate.m in Sources */,
		2D4A217D1EA6F991005F66D6 /* main.m in Sources */,
		2D4A21B01EA6FB09005F66D6 /* FirstViewController.m in Sources */,
			);
	runOnlyForDeploymentPostprocessing = 0;
		};

### 新增一个分组(黄色文件夹: DemoGroup)
* 在PBXGroup中声明这个分组 在需要新增的位置直接新增一个
有uuid 和注释组成的记录 并在声明后实现它

>

    2D4A216F1EA6F991005F66D6 = {
	isa = PBXGroup;
	children = (
    ->声明   2D4A21B11EA705D9005F66D6 /* DemoGroup */,
		2D4A217A1EA6F991005F66D6 /* AutoDemo */,
		2D4A21941EA6F991005F66D6 /* AutoDemoTests */,
		2D4A219F1EA6F991005F66D6 /* AutoDemoUITests */,
		2D4A21791EA6F991005F66D6 /* Products */,
		);
	sourceTree = "<group>";
	};


* 在PBXGroup中声明这个分组 记录这个group中的文件

> 在mainGroup = 2DFDD1611EA9DBC60088B9B5;这个id的节点中添加,前面报错是因为少加了","

> 

    -> 实现    
	2D4A21B11EA705D9005F66D6 /* DemoGroup */ = {
	    isa = PBXGroup;
		children = (
		2D4A21B21EA7086F005F66D6 /* LasViewController.h */,
		2D4A21B31EA7086F005F66D6 /* LasViewController.m */,
			);
		name = DemoGroup;
		sourceTree = "<group>";
		};
### 新拖进一个蓝色文件夹 
> 和新增文件类似 在这里面会将该文件夹下所有的文件都引用到项目中

* 在PBXBuildFile中新增记录

>

    2D4A21B61EA70C5F005F66D6 /* AutoDemoDoc in Resources */ = {
	isa = PBXBuildFile;
	fileRef = 2D4A21B51EA70C5F005F66D6 /* AutoDemoDoc */; };
 

* 在PBXFileReference 中新增记录

> 

	2D4A21B51EA70C5F005F66D6 /* AutoDemoDoc */ = {
	isa = PBXFileReference; 
	lastKnownFileType = folder; 
	path = AutoDemoDoc; 
	sourceTree = "<group>"; };
	
* 在PBXGroup中新增记录

> 

	2D4A216F1EA6F991005F66D6 = {
	isa = PBXGroup;
	children = (
		2D4A21B51EA70C5F005F66D6 /* AutoDemoDoc */,
		2D4A21B11EA705D9005F66D6 /* DemoGroup */,
		2D4A217A1EA6F991005F66D6 /* AutoDemo */,
		2D4A21941EA6F991005F66D6 /* AutoDemoTests */,
		2D4A219F1EA6F991005F66D6 /* AutoDemoUITests */,
		2D4A21791EA6F991005F66D6 /* Products */,
		);
	sourceTree = "<group>";
		};
 
 * 在PBXResourcesBuildPhase中添加记录

> 

	2D4A21761EA6F991005F66D6 /* Resources */ = {
	isa = PBXResourcesBuildPhase;
	buildActionMask = 2147483647;
	files = (
		2D4A218B1EA6F991005F66D6 /* LaunchScreen.storyboard in Resources */,
		2D4A21881EA6F991005F66D6 /* Assets.xcassets in Resources */,
		2D4A21861EA6F991005F66D6 /* Main.storyboard in Resources */,
		2D4A21B61EA70C5F005F66D6 /* AutoDemoDoc in Resources */,
			);
	runOnlyForDeploymentPostprocessing = 0;
		};
		
### 添加框架 AudioToolbox.framework Optional

* 在PBXBuildFile中添加一条记录

> 

	228A23321EA0688400B45CC5 /* AudioToolbox.framework in Frameworks */ = {
	isa = PBXBuildFile; 
	fileRef = 228A23311EA0688400B45CC5 /* AudioToolbox.framework */; 
	settings = {ATTRIBUTES = (Weak, ); }; 
	};

* 在PBXFileReference中添加记录

> 

	228A23311EA0688400B45CC5 /* AudioToolbox.framework */ = {
	isa = PBXFileReference;
	lastKnownFileType = wrapper.framework; 
	name = AudioToolbox.framework; 
	path = System/Library/Frameworks/AudioToolbox.framework; 
	sourceTree = SDKROOT; };

* 在PBXFrameworksBuildPhase中添加记录


> 

    22462A991E8B523F00B2D25F /* Frameworks */ = {
    	isa = PBXFrameworksBuildPhase;
		buildActionMask = 2147483647;
		files = (
				228A23321EA0688400B45CC5 /* AudioToolbox.framework in Frameworks */,
			);
		runOnlyForDeploymentPostprocessing = 0;
		};
		
* 在PBXGroup中添加一条记录

> 

	228A23301EA0688300B45CC5 /* Frameworks */ = {
		isa = PBXGroup;
		children = (
			228A23311EA0688400B45CC5 /* AudioToolbox.framework */,
			);
		name = Frameworks;
		sourceTree = "<group>";
		};
		
#### 修改pch文件,将unity中的Prefix.pch中的代码全部复制到自己的E_Publishing_Prefix.pch中

> 

* 在PBXFileReference中添加记录

> 

	2D4A21B71EA74AD0005F66D6 /* PrefixHeader.pch */ = {
	isa = PBXFileReference; 
	lastKnownFileType = sourcecode.c.h; 
	path = PrefixHeader.pch; 
	sourceTree = "<group>"; 
	};

* 在PBXGroup中添加记录

> 

    2D4A216F1EA6F991005F66D6 = {
		isa = PBXGroup;
		children = (
			2D4A21B71EA74AD0005F66D6 /* PrefixHeader.pch */,
			2D4A21B51EA70C5F005F66D6 /* AutoDemoDoc */,
			2D4A21B11EA705D9005F66D6 /* DemoGroup */,
			2D4A217A1EA6F991005F66D6 /* AutoDemo */,
			2D4A21941EA6F991005F66D6 /* AutoDemoTests */,
			2D4A219F1EA6F991005F66D6 /* AutoDemoUITests */,
			2D4A21791EA6F991005F66D6 /* Products */,
			);
		sourceTree = "<group>";
	};
	
* 在XCBuildConfiguration中添加记录

> 

	2D4A21A71EA6F991005F66D6 /* Release */ = {
		isa = XCBuildConfiguration;
		buildSettings = {
			ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
			DEVELOPMENT_TEAM = JWD48Y236P;
		->	GCC_PREFIX_HEADER = PrefixHeader.pch;
			INFOPLIST_FILE = AutoDemo/Info.plist;
			LD_RUNPATH_SEARCH_PATHS = "$(inherited) @executable_path/Frameworks";
			OTHER_LDFLAGS = "-c";
			PRODUCT_BUNDLE_IDENTIFIER = com.founder.AutoDemo;
			PRODUCT_NAME = "$(TARGET_NAME)";
		};
		name = Release;
		};

#### 修改Other Linker Flags 将unity中设置复制到原生项目中

* 在XCBuildConfiguration中修改键值,build setting 有两个一个是全局的PROJRECT一个是TARGET中的各个target的独立设置, 在debug和release中都要对应着改,分别生效

> 
 				
    ->  OTHER_LDFLAGS = (
		"-liconv",
		"-lz",
		"-lGraph2d",
		"-lGraph3d",
		"-ljson",
		"-lc++",
		"-weak_framework",
		CoreMotion,
		"-weak-lSystem",
		"$(OTHER_LDFLAGS)",
				);


#### write link map file
* 修改对应的键值对
 
> 

    LD_GENERATE_MAP_FILE = NO;

#### head search path
* 修改对应的键值对

> 

	HEADER_SEARCH_PATHS = (
			path1,
			path2,
		);


#### libra search path

* 修改对应的键值对

> 

    LIBRARY_SEARCH_PATHS = (
		libPath1,
		libPath2,
	);
#### Other C Flags 
* 修改对应的键值对

> 

    OTHER_CFLAGS = "-DINIT_SCRIPTING_BACKEND=1";

#### C++ language dialect
* 修改对应的键值对


> 

    CLANG_CXX_LANGUAGE_STANDARD

#### C++ standard Library
* 修改对应的键值对

> 

    CLANG_CXX_LIBRARY

#### enable C++ runtime Types
* 修改对应的键值对

> 

    GCC_ENABLE_CPP_RTTI

#### enable Object-c extensions
* 修改对应的键值对

> 

    GCC_ENABLE_OBJC_EXCEPTIONS = NO;
    
#### overriding deprecated Objecet-c methods
* 修改对应的键值对

> 

    CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS
    
#### GCC_USE_INDIRECT_FUNCTION_CALLS

* 增加键值对

> 

    GCC_USE_INDIRECT_FUNCTION_CALLS = NO;

#### UNITY_RUNTIME_VERSION

* 增加价值对

> 

    UNITY_RUNTIME_VERSION = 5.5.2f1;


#### UNITY_SCRIPTING_BACKEND

* 增加键值对

> 

    UNITY_SCRIPTING_BACKEND = il2cpp;



#### GCC_THUMB_SUPPORT

* 增加键值对

> 
 
    GCC_THUMB_SUPPORT = NO;

#### 添加runscript

* 在PBXNativeTarget中添加字段

> 

	2D4A21771EA6F991005F66D6 /* AutoDemo */ = {
		isa = PBXNativeTarget;
		buildConfigurationList = 2D4A21A51EA6F991005F66D6 /* Build configuration list for PBXNativeTarget "AutoDemo" */;
		buildPhases = (
			2D4A21741EA6F991005F66D6 /* Sources */,
			2D4A21751EA6F991005F66D6 /* Frameworks */,
			2D4A21761EA6F991005F66D6 /* Resources */,
     ->		2D4A21B91EA75F9D005F66D6 /* ShellScript */,
		);
		buildRules = (
		);
		dependencies = (
		);
		name = AutoDemo;
		productName = AutoDemo;
		productReference = 2D4A21781EA6F991005F66D6 /* AutoDemo.app */;
		productType = "com.apple.product-type.application";
		};
		
> 

    /* Begin PBXShellScriptBuildPhase section */
		033966F41B18B03000ECD701 /* ShellScript */ = {
			isa = PBXShellScriptBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			inputPaths = (
			);
			outputPaths = (
			);
			runOnlyForDeploymentPostprocessing = 0;
			shellPath = /bin/sh;
			shellScript = "\"$PROJECT_DIR/MapFileParser.sh\"\nrm -rf \"$TARGET_BUILD_DIR/$PRODUCT_NAME.app/Data/Raw/QCAR\"";
		};
    /* End PBXShellScriptBuildPhase section */