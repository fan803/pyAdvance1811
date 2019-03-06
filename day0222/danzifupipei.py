import re
#. 匹配任意1个字符（除了\n）（单行模式合一匹配\n）
result = re.findall(".", "123 \n china", flags=re.M)
# "." 不可以匹配换行符
print(result)

#[ ] 匹配[ ]中列举的字符
result = re.findall("[012].ello", "0hello 1hello 2 ello 88ello 888ello")
print(result)

#\d 匹配数字，即0-9
result = re.findall("\dhello", "hello 1hello 5hello 0hello")
print(result)

#\D 匹配非数字，即不是数字
result = re.findall("\Dhello", "xhello 1hello 5hello 0hello")
print(result)

#\s 匹配空白，即 空格，tab键
result = re.findall("\shello", " 1hello  hello   hello")
print(result)

#\S匹配空白，即 空格，tab键
result = re.findall("\Shello", " 1hello  hello   hello")
print(result)

#\w 匹配单词字符，即a-z、A-Z、0-9、_
result = re.findall("\wello", "hello aello5ello_ello .ello ^ello")
print(result)

#\W 匹配单词字符，即a-z、A-Z、0-9、_
result = re.findall("\Wello", "hello aello5ello_ello .ello ^ello")
print(result)

