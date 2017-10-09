# wkwebView 使用注意点

* 允许自动播放音视频

```
wkConfiguration.mediaPlaybackRequiresUserAction = NO;
wkConfiguration.allowsInlineMediaPlayback = YES;
WKWebView *wkweb = [[WKWebView alloc]initWithFrame:CGRectZero configuration:wkConfiguration];
```

* 关闭网页打开的音乐界面

```
[self.wkWeb loadRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:@"about:blank"]]];

```