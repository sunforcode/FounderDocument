# UInavigation 相关

###1.navigation的title问题
**self.navigationItem.title**
 = @"my title"; sets navigation bar title.

self.tabBarItem.title
 = @"my title"; sets tab bar title.

self.title
 = @"my title"; sets both of these.
 
 
###2.apparence 

**[UINavigationBar appearance]**

## 改变navigationItem

### 左边的按钮

* 设置了leftbarButtonItem
* 前一个控制器设置了backBarButtonItem的属性
* 如果前面两项都没有设置,就会使用默认设置,title的名字为 前一个控制器的title属性,只有一个控制器不会显示
> note: 如果前一个控制的名字太长的话,会更改系统设置的控制为back,自定义控制不会更改名字

### 中间的按钮

* 如果控制器设置了titleView的属性的话,就会使用这个view
* 显示当前控制器的名称,self.title,如果设置navigation.itme.title的话会显示这个属性(显示和tabbar的不一致)

### 右边的按钮

* 设置了rightbaritem ,则显示rightbaritem
* 没有设置的话 ,显示空白



### 返回上层的设置

self.navigationController.interactivePopGestureRecognizer.enabled = NO;