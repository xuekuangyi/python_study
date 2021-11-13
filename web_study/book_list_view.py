#Python标准库中定义的CGI跟踪模块：cgibt
import cgitb
import yate
import book_service
cgitb.enable()
#启用这个模块时，会在web浏览器上显示详细的错误信息。enable()函数打开CGI跟踪
#CGI脚本产生一个异常时，Python会将消息显示在stderr（标准输出）上。CGI机制会忽略这个输出，因为它想要的只是CGI的标准输出（stdout）
#CGI标准指出，服务器端程序（CGI脚本）生成的任何输出都将会由Web服务器捕获，并发送到等待的web浏览器。具体来说，会捕获发送到Stdout（标准输出）的所有内容
#一个CGI脚本由2部分组成, 第一部分输出 Response Headers, 第二部分输出常规的html.

print("Content-type:text/html\n")#Response Headers
#网页内容：有html标签组成的文本
print('<html>')
print('<head>')
print('<title>图书列表</title>')
print('</head>')
print('<body>')
print('<h2>图书列表</h2>')
print(yate.start_form('book_detail_view.py'))
book_dict=book_service.get_book_dict()
for book_name in book_dict:
    print(yate.radio_button('书名',book_dict[book_name].name))
print(yate.end_form('detail'))
print(yate.link("/index.html",'Home'))
print('</body>')
print('</html>')