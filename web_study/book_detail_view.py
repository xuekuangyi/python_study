import cgitb
cgitb.enable()

import cgi
import yate
import book_service as book_service

#使用cig.FieldStorage() 访问web请求发送给web服务器的数据，这些数据为一个Python字典
form_data = cgi.FieldStorage()

print("Content-type:text/html\n")
print('<html>')
print('<head>')
print('<title>Book List</title>')
print('</head>')
print('<body>')
print(yate.header('Book Detail:'))
try:
   book_name = form_data['bookname'].value
   book_dict=book_service.get_book_dict()
   book=book_dict[book_name]
   print(book.get_html)
except KeyError as kerr:
   print(yate.para('please choose a book...'))
print(yate.link("/index.html",'Home'))
print(yate.link("book_list_view.py",'Book List'))
print('</body>')