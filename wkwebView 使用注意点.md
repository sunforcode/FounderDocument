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



* 是否允许请求

```
 func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
        if navigationAction.request.url!.absoluteString.contains("baidu")  {
            decisionHandler(WKNavigationActionPolicy.cancel)
        }else{
         decisionHandler(WKNavigationActionPolicy.allow)
        }
    }
```

* 调取js的代码

```
func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping () -> Void) {
        
    }

```

* 通过message来传值

```
class ProfileH5NotifacationVC: BaseVC,WKNavigationDelegate,WKUIDelegate,WKScriptMessageHandler  {

    var webview :WKWebView?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setNavigationBar(isHidden: true)
        setUpUI()
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        webview?.configuration.userContentController.add(self as WKScriptMessageHandler, name: "kGoBackJSName")
    }
    
    override func viewWillDisappear(_ animated: Bool) {
        super.viewDidDisappear(animated)
        webview?.configuration.userContentController.removeScriptMessageHandler(forName: "kGoBackJSName")
    }
    
    func setUpUI(){
        view.backgroundColor = UIColor.appGreen
        let urlString  = "http://\(API.ip)/mobile/student/discuss/list.do?wxtype=1&ptype=4&subjectId=&openid=\(User.current.id)"
        let url = URL.init(string: urlString)!
        
        let configuration = WKWebViewConfiguration.init()
        let preference = WKPreferences.init()
        
        preference.javaScriptCanOpenWindowsAutomatically = true
        preference.minimumFontSize = 40.0
        configuration.preferences = preference
        
        let webView =  WKWebView(frame: CGRect(x: 0, y: 0, width: UIScreen.main.bounds.size.width, height: UIScreen.main.bounds.size.height), configuration: configuration)
        webview = webView
        self.automaticallyAdjustsScrollViewInsets = false
        view.addSubview(webView)
        webView.navigationDelegate = self as WKNavigationDelegate
        webView.uiDelegate = self as WKUIDelegate
        webView.load(URLRequest(url: url))
        
    }
    
    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        if let messageString = message.body as? String {
            if messageString == "ok" {
                 pop()
            }
        }
    }

```

``` 		 
js代码   kGoBackJSName 为在swift代码中需要填写的string
	function goBack(){		          if (/(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)) {		              //alert(navigator.userAgent);		        	  window.webkit.messageHandlers.kGoBackJSName.postMessage('ok');		          } else if (/(Android)/i.test(navigator.userAgent)) {		              //alert(navigator.userAgent);		        	  window.AndroidGoBack.back(); 		          }  			}
```
