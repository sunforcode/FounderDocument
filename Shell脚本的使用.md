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