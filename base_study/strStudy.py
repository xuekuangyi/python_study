# 定义&赋值两个字符串型变量
str_for_zn = '中文测试'
str_for_en = 'to learning String in English'
str_en_alphabet = 'abcdefghijklmnopqrstuvwxyz'
str_num = '0123456789'

# 所见即所得的三个单引号
multi_line = '''
a.这是一段多行文本的测试，这是第一行；
b.这是多文本测试的第二行；
c.这是多文本测试的第三行；
d.这是多文本测试的最后一行；'''  # 注意如果换行的话，会空出一行

# 字符串类型的索引
# 字符串[开始索引号:结束索引号]
# 以下是几种字符串索引的写法

print('1、只写一个索引号时，定位到的是这个索引编号的字符，例如字符串', str_for_en, '的倒数第二个字符是 :', str_for_en[-2])
print('2、像excel的写法一样，写明开始和结束“坐标”，则是指明一个范围内的内容：', str_for_en, '的第三个到第倒数第二个字符之间的字符串是:', \
      str_for_en[2:-2])
# print(str_for_zn, ':', str_for_zn[3:-3]) #无字符输出
print('3、采用引号分隔的开始索引号可以一闭一开，甚至全开，比如“左闭右开”', str_num, '[1:]得到这样的结果：', str_num[1:])
print('\t“左开右闭”', str_num, '[:5]得到这样的结果：', str_num[:5])
print('\t“全开”', str_num + '[:]得到这样的结果：' + str_num[:])
# 疑问，以上语句输出结果中的str_num与[之间为何会有空格？使用“+”拼接字符串即无空额，而用','分隔则会有空格
print('4、利用循环与索引结合的一个小例子，把字符串一个字符占一行展示')
position = 0
for begin in range(4):  # 初试循环写法
    print(str_for_zn[begin:begin + 1])
print('5、采用三个单引号嵌套可以得到所见即所得的多行文本效果：' + multi_line)
print('6、字符串拼接示例：将数字与字母拼接起来：' + str_num + str_en_alphabet)
# 利用{}来在字符串内引入变量
print('7、6的示例可用格式为：f\'{变量}{变量} 其它字符串内容\'来表示，效果：' + f'{str_num}{str_en_alphabet}是把数字和 \
字母链接起来的简单的方式')
print('8、len()方法返回字符串的长度：' + str(len(str_num)))  # len() 方法返回的值是int型
print(f'9、对于字符串类型，python还提供了很多方法，如针对英文的upper()和lower():将变量str_en_alphabet的值全部转为大写 {str_en_alphabet.upper()}，'
      f'再转换小写{str_en_alphabet.upper().lower()}')
print(str_en_alphabet)
letter = 'q'
print(f"10、查找方法.find()查找{letter}是第{str_en_alphabet.find(letter)+1}个字母")  # 方法参数中的p，注意单双引号的配合
l_pos = str_en_alphabet.find(letter)
print(l_pos)
print(f'11、替换方法.replace()：将指定字母换为大写 {str_en_alphabet.replace(str_en_alphabet[l_pos],str_en_alphabet[l_pos].upper())}')
print('''
总结：
string[x:y]：返回字符串中指定坐标或范围的内容
''''''：三对单引号，可以用于多行文本的所见即所得
.len()：返回int型的字符串长度
.upper()/.lower()：大小写转换
.title()：首字母大写
.find('被查找内容')：查找指定的字符串，返回索引号；
.replace('被替换内容', '将内容替换成此值')：替换方法
'目标字符串' in 字符串:判断目标字符串是否在字符串中
''')

print(type(type(str_for_en)))  # type是类
