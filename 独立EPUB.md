# 独立EPUB
* 添加了libxml2 的库 然后在buildsetting中添加变量 headersearchpath
${SDK_ROOT}/usr/include/libxml2

success = [EncodeDecode htmlFileEncode:filePath]; 注释了 HYEpubController.h


## 类别的记录

@interface EpubChapter : NSObject <UIWebViewDelegate,EPUBWebviewProtocal,NSCopying>


### epub的左边章节跳转逻辑

在点击了对应的单元格后

```
[delegate showPageWithChapter:markObject.chapterIndex page:markObject.pageNum jsMark:nil];
```

在**EpubMainViewController**中,代理方法

1. 获取EpubChapter对象,EpubChapter *chapter = [epubDataModel.chapterArray objectAtIndexedSubscript:cindex];
2.     [self setNowChapterIndex:cindex pageIndex:pIndex]; 设置相关状态
3. pagenating,是否在计算页面


### EPUB总长度和页面的计算

EPUBDateModel generateChapterPositonAndGetTotolCount 返回总共的页面

循环计算每一个chapterArray的页面,然后在计算总页面

for (NSInteger i = 1; i < chapterArray.count; i++) {
	pageNUm * perPageLength

每一页的长度为屏幕的宽度,pageNum是计算出来的

计算的关键在EpubWebView的didFinishLoad中,通过js获取到"getPageSize()"
获取到页面的长度

在这个方法的最后,还会回调上一个方法 [mainViewDelegate(epubChapter) webviewFinishLoad:self];

创建临时的webview 是在

epubchapter

-(EpubWebView *)loadWebViewWithFlag:(NSInteger)flag size:(CGSize)theWindowSize

        if(webview.firstLoad == YES)


### EpubWebView解析 

继承 JSBridgeWebView


### EPUB总长度中的chapterArray设置赋值

在HYEpubController中设置

> -(NSArray *)getChapterListArrayWithChapterArray:(NSArray *)chapterArray
返回一个包含filePath的ChapterArray;

> -(NSArray *)getBookChapterFileArray
返回的是 EpubListObject数组

### EpubListObject解析


### 首次进入加载页码

使用一个loaded 变量控制,判断标准是是否在catalog中有一个数组,并且字号什么的变化也会导致返回no,从而重新或者首次加载

### 加载页码的时机

是第一次完成loadRequest,然后用变量控制只计算一次

```
if(webview.firstLoad == YES)
{
    
    webview.firstLoad = NO;
    epubLoaded = YES;
    [self delayLoadPageWithWebview:webview];
    [epubController updatePagination];
}
```
s
判断是否计算完毕EpubDatamodel 

```
if(tempChapter.chapterIndex + 1 < [chapterArray count]){
[chapter loadChapterWithWindowSize:CGSizeMake([epubDelegate getViewwidth], [epubDelegate getViewHeight])];
}
else {
lastCountPageIndex = 0;
[epubDelegate finishUpdateChapterArray];
    
}

```

### Epub的待完成项目

 注销了 #import "IQKeyboardManager.h"
 
 
 PDF_RELEASE


EncodeDecode.h 注释了

将textBookId 替换了userInfo.userState.textbookID

userInfo.userState.pageNum = pageNum; 注释

//extern BOOL isEncrypt; 注释



