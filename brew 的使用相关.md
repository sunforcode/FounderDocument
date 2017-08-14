# brew 的使用相关

* brew在使用的时候哦碰到了权限的问题

		解决办法:
		sudo chown -R $(whoami):admin /usr/local
		sudo chown -R $(whoami) /Library/Caches/Homebrew
		brew doctor 
		brew prune
		brew update