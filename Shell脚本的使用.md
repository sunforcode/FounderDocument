# Shell脚本的使用

* 使用的变量在引用的时候 要加$

		
		PROJECT_PATH = user/destop... 
		echo $PROJECT_PATH
		

* shell脚本写控制流程

		if ["a" == "a"]
		then
		    command1
		elif ["a" == "a"] 
		then 
		    command2
		else
		    commandN
		fi
		
*  shell脚本退出的命令

		exit
		

#### 脚本任何位置运行
		
*  对于Linux或者Mac,如果希望能够在任何位置都可以执行,都可以把qshell所在的目录加入到环境变量 **$PATH**中去. 假设qshell命令被解压到路径 **/home/jemy/tools**目录下面,那么我们可以把如下的命令写入到你所使用的bash所对应的配置文件中,如果是**/bin/bash**,如果是**/bin/zsh**,那么就是**~/.zshrc**文件中,如果是**/bin/bash**,那么就是**~/.bashrc**文件.写入的内容为:

```
export PATH=$PATH:/home/jemy/tools
```

保存完毕之后,可以通过两种方式立即生效,其一为输入 **source ~/.zshrc**或者**source ~/.bashrc**来使配置立即生效, 或者完全关闭命令行,重新打开一个,接下来就可以在任何位置使用**qshell**命令了