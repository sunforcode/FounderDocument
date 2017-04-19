# 记录研究project.pbxproj文件

### 1. 增加一个新文件的操作
* 在PBXBuildFile中新增了一条记录: 

>

    2D4A21B01EA6FB09005F66D6 /* FirstViewController.m inSources */ = {
    isa = PBXBuildFile;
    fileRef = 2D4A21AF1EA6FB09005F66D6 /* FirstViewController.m */; };


> 如果添加了-fobjc-arc 会在这个位置显示 settings = 

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
* 在PBXGroup中声明这个分组

>


    2D4A216F1EA6F991005F66D6 = {
	isa = PBXGroup;
	children = (
	   2D4A21B11EA705D9005F66D6 /* DemoGroup */,
		2D4A217A1EA6F991005F66D6 /* AutoDemo */,
		2D4A21941EA6F991005F66D6 /* AutoDemoTests */,
		2D4A219F1EA6F991005F66D6 /* AutoDemoUITests */,
		2D4A21791EA6F991005F66D6 /* Products */,
		);
	sourceTree = "<group>";
	};

* 在PBXGroup中声明这个分组 记录这个group中的文件

> 

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
和新增文件类似

* 在PBXBuildFile中新增记录

>

    2D4A21B61EA70C5F005F66D6 /* AutoDemoDoc in Resources */ = {
	isa = PBXBuildFile;
	fileRef = 2D4A21B51EA70C5F005F66D6 /* AutoDemoDoc */; };
 

* 在PBXFileReference 中新增记录

> 

	2D4A21B51EA70C5F005F66D6 /* AutoDemoDoc */ = {isa = PBXFileReference; lastKnownFileType = folder; path = AutoDemoDoc; sourceTree = "<group>"; };
	
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