# Epub的思路

1.向外提供两个阅读的进入接口

- initwithFilePath:(NSString *)path PageNum:(int)page


过程: 
1.先解析chapter
2.显示当前的webView
3.最后计算阅读进度

2.页面显示和页码计算要分离