# bug解决

Attempted to dereference an invalid ObjC Object or send it an unrecognized selector.
The process has been returned to the state before expression evaluation.

* 修改了名称,没改变所有的内容后不崩溃了




> symbol(s) not found for architecture arm64



* a parameter list without types is only allowed in a function definition

		修改c language dialect GNU99



## Masonry 报错unrecognized

```
在buildSetting 中添加-l"Masonry"
```


## 在加载从stroyBoard中的controller的控件，使用set方法，会发现在set方法中 UI控件为空

* 解决办法： 在set方法放到主线程最后中去 dispathqueue.main.async

```
```

#### 强制转屏 在用户锁定了屏幕锁定时，可以调用强制转屏
