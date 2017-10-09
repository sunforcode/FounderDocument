# git的使用问题


###1.在机器更换了github账号后,无法正确使用git push


提示的问题是说 

```
remote: Permission to sssss/useGit.git denied to ***username***.

```

解决办法: 
将钥匙串中涉及到github的所以记录都删除掉,

或者使用终端敲命令行:

```
git credential-osxkeychain erase
host=github.com
protocol=https
[Press Return]
```

最后附上github的[帮助链接](https://help.github.com/articles/updating-credentials-from-the-osx-keychain/)