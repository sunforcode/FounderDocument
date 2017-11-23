# beginBackgroundTaskWithExpirationHandler

正常程序退出后，会在几秒内停止工作；
要想申请更长的时间，需要用到
beginBackgroundTaskWithExpirationHandler
endBackgroundTask
一定要成对出现

```
- (void)applicationDidEnterBackground:(UIApplication *)application {

    [self beginTask];
    //在非主线程开启一个操作在更长时间内执行； 执行的动作
    aa =0;
    _timer = [NSTimer scheduledTimerWithTimeInterval:1 target:self selector:@selector(go:) userInfo:nil repeats:YES]; 
  }

-(void)go:(NSTimer *)tim
{
    NSLog(@"%@==%ld ",[NSDate date],aa);
    aa++;
    if (aa==9) {
        [_timer invalidate];
            [self endBack]; // 任务执行完毕，主动调用该方法结束任务
    }
}

-(void)beginTask
{
    NSLog(@"begin=============");
   _backIden = [[UIApplication sharedApplication] beginBackgroundTaskWithExpirationHandler:^{
       NSLog(@"begin  bgend=============");
       [self endBack]; // 如果在系统规定时间内任务还没有完成，在时间到之前会调用到这个方法，一般是10分钟
   }];
}

-(void)endBack
{
    NSLog(@"end=============");
    [[UIApplication sharedApplication] endBackgroundTask:_backIden];
    _backIden = UIBackgroundTaskInvalid;
}

```