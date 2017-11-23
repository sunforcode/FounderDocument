# Collection Views

## View

### UICollectionView

* 直接改变collectionviewLayout会直接改变布局,调用setCollectionViewLayout:animated:completion: 方法会动画的显示
* 如果想要通过交互来改变布局,使用   **startInteractiveTransitionToCollectionViewLayout:completion:**方法改变布局
* supplementary views 除了从用标识外,还有一个额外的标识,存在layout中 比如 UICollectionViewFlowLayout类支持两种类型 UICollectionElementKindSectionHeader 和 UICollectionElementKindSectionFooter

#### 移动单元格

* 1.给collectionview添加长按的手势

```
UILongPressGestureRecognizer *longPress = [[UILongPressGestureRecognizer alloc]initWithTarget:self action:@selector(didLongProessCollectionView:)];
self.longPress = longPress;
[collectView addGestureRecognizer:longPress];
 
    
self.array = [NSMutableArray arrayWithObjects:@"红包", @"转账", @"手机充值", @"芝麻信用",
              @"天猫", @"生活缴费", @"蚂蚁呗", @"世界那么大",
              @"余额宝", @"安全快付", @"蚂蚁聚宝", @"哈哈",@"红包1", @"转账1", @"手机充值1", @"芝麻信用1",
              @"天猫1", @"生活缴费1", @"蚂蚁呗1", @"世界那么大1",
              @"余额宝1", @"安全快付1", @"蚂蚁聚宝1", @"哈哈1",  nil];
```

* 2.手势对应的响应方法

```
- (void)didLongProessCollectionView:(UILongPressGestureRecognizer *)longpress  {
    
switch (longpress.state) {
    case UIGestureRecognizerStateBegan:{
        NSIndexPath *selectedIndex =  [self.collectionView indexPathForItemAtPoint:[longpress locationInView:self.collectionView]];

        [self.collectionView beginInteractiveMovementForItemAtIndexPath:selectedIndex];
    }
        break;
    case UIGestureRecognizerStateChanged:
        [self.collectionView updateInteractiveMovementTargetPosition:[longpress locationInView:self.collectionView]];
        
        break;
    case UIGestureRecognizerStateEnded:
        [self.collectionView endInteractiveMovement];
        break;
    default:
        break;
}
}

```

* 3.对应的cell的move方法 (如果不实现 没有反应)

```
- (void)collectionView:(UICollectionView *)collectionView moveItemAtIndexPath:(nonnull NSIndexPath *)sourceIndexPath toIndexPath:(nonnull NSIndexPath *)destinationIndexPath
{
    NSLog(@"移动了");
    [self.array exchangeObjectAtIndex:sourceIndexPath.item withObjectAtIndex:destinationIndexPath.item];
    [self.collectionView reloadData];
}
```


