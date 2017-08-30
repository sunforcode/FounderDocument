# http的学习记录


* http协议工作于客户端-服务端架构上

	> http的三点注意事项

#### http的三点注意事项

* http是无连接 限制每次链接只处理一个请求.服务器处理完客户的请求,并收到客户的应答后,即断开链接.采用这种方式可以节省传输时间

* http是媒体独立的: 这意味着,只要客户端和服务器知道如何处理的数据内容,任何类型的数据都可以通过http发送.客户端以及服务器指定使用适合的MIME-type内容类型

* http是无状态: HTTP协议是无状态协议.无状态协议是指协议对于事务处理没有记忆能力.缺少状态意味着如果后续处理需要前面的信息.则它必须重传,这样可能导致每次连接发送的数据量增大.另一方面,在服务器不需要先前信息是它的应答就较快

#### 客户端请求信息

客户端发送一个HTTP请求到服务器的请求消息包括以下格式: 请求行(request line), 请求头部(header), 空行和请求数据四个部分组成, 下图给出了请求报文的一般格式.

![](http://okzs58u17.bkt.clouddn.com/http_record_01) 

#### 服务器响应信息

HTTP响应也由四个部分组成,分别是:状态行,消息报头,空行和响应正文.

![](http://okzs58u17.bkt.clouddn.com/Snip20170830_5.png)

#### 实例

* 客户端请求

```
GET /hello.txt HTTP/1.1
User-Agent: curl/7.16.3 libcurl/7.16.3 OpenSSL/0.9.7l zlib/1.2.3
Host: www.example.com
Accept-Language: en, mi
```

* 服务端响应

```
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2009 12:28:53 GMT
Server: Apache
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
ETag: "34aa387-d-1568eb00"
Accept-Ranges: bytes
Content-Length: 51
Vary: Accept-Encoding
Content-Type: text/plain
```

#### HTTP状态码

当浏览者访问一个网页时,浏览者的浏览器会向网页所在服务器发出请求.当浏览器接受并显示网页前,此网页所在的服务返回一个包含HTTP状态码的信息头(server header)用以响应浏览器的请求.
[详细的Url](http://www.runoob.com/http/http-status-codes.html)

HTTP状态码的英文为HTTP Status Code

* 200 - 请求成功
* 301 - 资源被永久转移到其他URL
* 404 - 请求的资源,网页等,不存在
* 500 - 内部服务器错误
