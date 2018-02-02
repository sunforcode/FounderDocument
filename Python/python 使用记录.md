# python 使用记录

###1.Pycharm Unresolved Reference无法引入包

####1.问题描述: 	
在项目中P存在文件夹A、B、C，A有文件夹a和b，在a中引入b的一个类，
a.py:

> from b import func1

虽然运行成功，但是在Pycharm中显示： Unresolved reference

例如

![](http://okzs58u17.bkt.clouddn.com/python_01.png)

####2.产生的原因:

Pycharm 默认该项目的根目录为source目录,每次import都是从source目录开始查找,也就是从P所在的目录开始,而不是A

####3.解决办法:

1. 将A文件夹 设置为source,

![](http://okzs58u17.bkt.clouddn.com/python_02.png)

2. 确保将soucers加入到PYTHONPATH:

![](http://okzs58u17.bkt.clouddn.com/python_03.png)

3. 自己测试中,将另外的一个目录下的文件夹也设置为source也可以将其中的文件正确的引用到,而不报红


#### BOM
读取text时候,会出现第一行的文件头为
data = data.replace(codecs.BOM_UTF8,"")