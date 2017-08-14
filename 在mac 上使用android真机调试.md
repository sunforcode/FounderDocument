# 在mac 上使用android真机调试

* 下载androidStudio后,初始化一个工程,会显示gradle一直在加载的问题,

	* 先安装brew 
	
	> brew install
	
	* 在用brew安装gradle
	
	> brew install gradle
	
	* 重启以后 稍等一会就可以进去了
	


* 1.在Mac上安装adb

		brew cask install android-platform-tools
		
* 安装adb

		brew cask install android-platform-tools
		
* 启动adb

		adb devices
		
		
### unity 的设置 
* java sdk 按照android studio中的设置设置
* java 环境的配置是在

> mac 下java的默认存放位置
> /Library/Java/JavaVirtualMachines/jdk1.8.0_111.jdk
