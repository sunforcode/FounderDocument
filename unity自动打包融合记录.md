# unity自动打包融合记录
 unity的打包问题主要是利用unity提供的终端命令,通过命令行的输入,自动启动unity,调用unity提供的方法来生成工程文件
 
#### 第一部分是unity中的脚本文件 
这部分的unity提供的文档地址:[unity的文档地址](https://docs.unity3d.com/ScriptReference/BuildPipeline.BuildPlayer.html)

	using UnityEditor;
	
	public class BuildPlayerExample : MonoBehaviour
	{
	    [MenuItem("Build/Build iOS")]//在菜单栏显示buidl build ios 的下拉菜单
	    public static void MyBuild()
	    {
	        BuildPlayerOptions buildPlayerOptions = new BuildPlayerOptions();
	        buildPlayerOptions.scenes = new[] {"Assets/Scene1.unity", "Assets/Scene2.unity"};//这个地方为scene的路径,可以点击scene show in finder 获取位置,从asset的后面可是填写
	        buildPlayerOptions.locationPathName = "iOSBuild";//这个是你想要打包出来的项目的路径存放位置
	        buildPlayerOptions.target = BuildTarget.iOS;//这个是你想要打包的方式
	        buildPlayerOptions.options = BuildOptions.None;
	        BuildPipeline.BuildPlayer(buildPlayerOptions);//开始构建
	    }
	}

#### 第二部分,在终端中调用unity提供的命令

在终端中直接敲命令行就可以调用unity的上面创建的脚本的静态方法,[文档地址](https://docs.unity3d.com/Manual/CommandLineArguments.html)

	#!/bin/sh #shell脚本的标识#
	
	#UNITY程序的路径# 
	UNITY_PATH=/Applications/Unity/Unity.app/Contents/MacOS/Unity
	
	#游戏程序路径#
	PROJECT_PATH=/Users/CharlyZhang/Git/ARProject/Sourcecode/FounderARBookProject
	
	#IOS打包脚本路径#
	BUILD_IOS_PATH=${PROJECT_PATH}/Assets/Shell/build.py
	
	#生成的Xcode工程路径#
	XCODE_PATH=${PROJECT_PATH}/$1
	
	#将unity导出成xcode工程#
	$UNITY_PATH -projectPath $PROJECT_PATH -executeMethod ProjectBuild.BuildForIPhone project-$1
	    
	echo "XCODE工程生成完毕"
