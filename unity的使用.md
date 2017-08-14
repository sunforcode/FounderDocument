# unity的使用

* 获取unity中的终端命令行参数

		string CommandLine = Environment.CommandLine;
		string[] CommandLineArgs = Environment.GetCommandLineArgs();
		foreach (string arg in CommandLineArgs){
			Debug.Log ("获取到的参数是"+arg );
		}