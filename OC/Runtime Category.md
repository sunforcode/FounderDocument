# Runtime Category

原文章地址： [链接](https://tech.meituan.com/DiveIntoCategory.html)
本文只是在阅读文章后的一点点总结记录

###1.category的简介

cate是objc2.0之后添加的语言特性，主要作用是为已经存在的类添加方法。除此之外，apple 还推荐了category的另外两个使用场景

	* 可以把类的实现放在几个不同的文件夹里面
	* 声明私有方法

### category的真面目

category用结构体category_t，包含了

1).类的名字（name）

2).类（cls）

3)、category中所有给类添加的实例方法的列表（instanceMethods）

4)、category中所有添加的类方法的列表（classMethods）

5)、category实现的所有协议的列表（protocols）

6)、category中添加的所有属性（instanceProperties）

```
typedef struct category_t {
    const char *name;
    classref_t cls;
    struct method_list_t *instanceMethods;
    struct method_list_t *classMethods;
    struct protocol_list_t *protocols;
    struct property_list_t *instanceProperties;
} category_t;
```

从category的定义可看,可以添加实例方法,类方法,实现协议,添加属性 不能添加实例变量

### cate如何加载

category的方法被放到了新方法列表的前面,把原来类的方法放到了新方法列表的后面,就是说category的方法会 "覆盖"掉原来类的同名方法,运行时一招到对应名字的方法,就会罢休,原方法还在后面藏着

### category的load方法

在1)、可以调用，因为附加category到类的工作会先于+load方法的执行
2)、+load的执行顺序是先类，后category，而category的+load执行顺序是根据编译顺序决定的。

load 方法调用总结
我们知道了 load 是在被添加到 runtime 时开始执行，父类最先执行，然后是子类，最后是 Category。又因为是直接获取函数指针来执行，不会像 objc_msgSend 一样会有方法查找的过程。

### 调用category覆盖前的源方法的代码

```
Class currentClass = [MyClass class];
MyClass *my = [[MyClass alloc] init];

if (currentClass) {
    unsigned int methodCount;
    Method *methodList = class_copyMethodList(currentClass, &methodCount);
    IMP lastImp = NULL;
    SEL lastSel = NULL;
    for (NSInteger i = 0; i < methodCount; i++) {
        Method method = methodList[i];
        NSString *methodName = [NSString stringWithCString:sel_getName(method_getName(method)) 
                                        encoding:NSUTF8StringEncoding];
        if ([@"printName" isEqualToString:methodName]) {
            lastImp = method_getImplementation(method);
            lastSel = method_getName(method);
        }
    }
    typedef void (*fn)(id,SEL);

    if (lastImp != NULL) {
        fn f = (fn)lastImp;
        f(my,lastSel);
    }
    free(methodList);
}
```


### category中添加实例变量

方法为: 自己添加set 和get 的方法 并且添加关联对象

```
- (void)setName:(NSString *)name
{
    objc_setAssociatedObject(self,
                             "name",
                             name,
                             OBJC_ASSOCIATION_COPY);
}

- (NSString*)name
{
    NSString *nameObject = objc_getAssociatedObject(self, "name");
    return nameObject;
}
```

AssociationsManager里面是由一个静态AssociationsHashMap来存储所有的关联对象的。这相当于把所有对象的关联对象都存在一个全局map里面。而map的的key是这个对象的指针地址（任意两个不同对象的指针地址一定是不同的），而这个map的value又是另外一个AssociationsHashMap，里面保存了关联对象的kv对。
而在对象的销毁逻辑里面，见objc-runtime-new.mm:


### sel和imp 
 sel 就是方法的名字 
 
 SEL selector=NSSelectorFromString(@"setOrientation:");
 
 IMP 实际上就是一个函数指针，指向方法实现的首地址。

通过取得 IMP，我们可以跳过 runtime 的消息传递机制，直接执行 IMP指向的函数实现，这样省去了 runtime 消息传递过程中所做的一系列查找操作，会比直接向对象发送消息高效一些，当然必须说明的是，这种方式只适用于极特殊的优化场景，如效率敏感的场景下大量循环的调用某方法[1]。

 Dispatch table是一张SEL和IMP的对应表。
 
 通过dispatch table表中找到这个class中对应sel的imp 执行
 
> 简单的直接执行IMP的方法

```
1. 在build Setting 中设置 Enable Strict Checking of objc_msgSend Calls = NO

- (void)viewDidLoad {
    [super viewDidLoad];

   void (*imp) (id,SEL,id) = (void (*)(id,SEL,id))[self methodForSelector:@selector(testImp)];
    
    imp(self,@selector(testImp),nil);
    
    
}


- (void)testImp{
    NSLog(@"hello IMP");
}

```

### iOS方法调用流程

**objc_msgSend**

1.检查调用着 target 是否为nil , 如果为nil ,直接return

2.在当前class中的方法缓存中寻找 cache methodLists,找到的话就执行

3.如没有找到 就在class的methodList中寻找,找到了就添加到方法缓存LIst中,然后执行该方法

4.如果还没找到就调到父类的缓存列表中,和methodList中查找,直到找到基类为止

5.如若上述步骤找不到IMP,则进入消息动态处理和消息转发流程

### RunTime的消息转发

第一种: 动态方法解析

首先，当接受到未能识别的选择子时，运行时系统会调用该函数用以给对象一次机会来添加相应的方法实现，如果用户在该函数中动态添加了相应方法的实现，则跳转到方法的实现部分，并将该实现存入缓存中，以供下次调用。

```
+ (BOOL)resolveInstanceMethod:(SEL)sel {
    NSLog(@"%@", NSStringFromSelector(sel));
    
    if ([NSStringFromSelector(sel) isEqualToString:@"notFond"]){
        IMP imp = class_getMethodImplementation(self, @selector(testImp));

        class_addMethod([self class], sel, imp, "v@:@");
        return YES;
    }else {

        return [super resolveInstanceMethod:sel];
    }
}
```

第二种: 备援接收者

如果运行时在消息转发的第一步中未找到所调用方法的实现，那么当前接收者还有第二次机会进行未知选择子的处理。这时运行期系统会调用上述方法，并将未知选择子作为参数传入，该方法可以返回一个能处理该选择子的对象，运行时系统会根据返回的对象进行查找，若找到则跳转到相应方法的实现，则消息转发结束。

```

+ (BOOL)resolveInstanceMethod:(SEL)sel {
    NSLog(@"%@", NSStringFromSelector(sel));
    return NO;
//    if ([NSStringFromSelector(sel) isEqualToString:@"notFond"]){
//        IMP imp = class_getMethodImplementation(self, @selector(testImp));
//
//        class_addMethod([self class], sel, imp, "v@:@");
//        return YES;
//    }else {
//
//        return [super resolveInstanceMethod:sel];
//    }
}

-(id)forwardingTargetForSelector:(SEL)aSelector {

    if ([NSStringFromSelector(aSelector) isEqualToString:@"notFond"]) {
        return [ViewController1 new];
    }else{
        return [super forwardingTargetForSelector:aSelector];

    }
}
```
 
 第三种:完整的消息转发
 
 当运行时系统检测到第二步中用户未返回能处理相应选择子的对象时，那么来到这一步就要启动完整的消息转发机制了。该方法可以改变消息调用目标，运行时系统根据所改变的调用目标，向调用目标方法列表中查询对应方法的实现并实现跳转，这种方式和第二步的操作非常相似。当然你也可以修改方法的选择子，亦或者向所调用方法中追加一个参数等来跳转到相关方法的实现。

最后，如果消息转发的第三步还未能处理该未知选择子的话，那么最终会调用NSObject类的如下方法用以异常的抛出，表明该选择子最终未能处理。

 ```
 + (BOOL)resolveInstanceMethod:(SEL)sel {
    NSLog(@"%@", NSStringFromSelector(sel));
    return NO;
//    if ([NSStringFromSelector(sel) isEqualToString:@"notFond"]){
//        IMP imp = class_getMethodImplementation(self, @selector(testImp));
//
//        class_addMethod([self class], sel, imp, "v@:@");
//        return YES;
//    }else {
//
//        return [super resolveInstanceMethod:sel];
//    }
}

-(id)forwardingTargetForSelector:(SEL)aSelector {
    return nil;
//    if ([NSStringFromSelector(aSelector) isEqualToString:@"notFond"]) {
//        return [ViewController1 new];
//    }else{
//        return [super forwardingTargetForSelector:aSelector];
//
//    }
}

- (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector {
    if ([NSStringFromSelector(aSelector) isEqualToString:@"notFond:"]) {
        return [NSMethodSignature signatureWithObjCTypes:"v@:@"];
    }else {
        return [super methodSignatureForSelector:aSelector];
    }
}

-(void)forwardInvocation:(NSInvocation *)anInvocation {
    
    [anInvocation invokeWithTarget:[ViewController1 new]];
}
 ```
 
 ![](/Users/CharlyZhang/Documents/工作文档/snipImages/Message.png)
 
 [最后的type的链接](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html#//apple_ref/doc/uid/TP40008048-CH100)
 
 
### 阻止崩溃的方法

* 步骤一: 在methodSignatureForSelector中返回一个能正确执行的方法的methodSignature
* 步骤二: 在forwardInvocation中写try, catch,finally 将错误信息打印,但是并不会崩溃报错

```
- (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector {
    
    NSLog(@"%p", aSelector);
    if ([NSStringFromSelector(aSelector) isEqualToString:@"notFond:"]) {
        return [ViewController1 instanceMethodSignatureForSelector:@selector(notFond:)];
    }else {
        return [super methodSignatureForSelector:aSelector];
    }
}

-(void)forwardInvocation:(NSInvocation *)anInvocation {
//    return
    @try {
        [super forwardInvocation:anInvocation];
    }@catch(NSException *exception) {
        NSLog(@"找到了错误 %@", exception.name);
    } @finally {
        
    }

}
```
**methodSignatureForSelector** 和 **instanceMethodSignatureForSelector**区别是前者是对象方法,后者为类方法
 
