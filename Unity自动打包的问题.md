# Unity自动打包的问题

* 分为三个步骤:
	* 两个scense都打包(white Secense放在前面),显示了一个方块()
	* 只打包一个white(一个方框的Secense),只显示一个方块
	* 只打包一个black(一个球的scense),只显示了一个球

> 解决文件没有运行权限的命令 :chmod +x <filePath>


	[MenuItem("Build/Build iOS")] //在ide中菜单栏中显示Build Build Ios 选项
	public static void BuildForIPhone()
	{
		BuildPlayerOptions buildPlayerOptions = new BuildPlayerOptions();
		buildPlayerOptions.scenes = new[] {"Assets/Black.unity"};//需要打包的场景,从assets文件目录开始填写
		buildPlayerOptions.locationPathName = "/Users/CharlyZhang/Desktop";
		//需要导出的文件目录路径
		buildPlayerOptions.target = BuildTarget.Android;//需要按照哪个方式打包
		buildPlayerOptions.options = BuildOptions.AcceptExternalModificationsToPlayer;//这个选项的意思是将项目按照goolgle源码的方式导出来(ADT)
		String result = BuildPipeline.BuildPlayer(buildPlayerOptions);//创建player
	}