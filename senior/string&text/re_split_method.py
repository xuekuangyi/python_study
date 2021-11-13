

import re

line = 'wasd, abcd, hijk; o. r'
# re.split——增强型的split，分隔符可以是分号、逗号、空格、句点
print(re.split(r'[;,\s,.]\s*',line))