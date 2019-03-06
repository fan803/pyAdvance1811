import re

pattern = "py123你好"
result = ("py123你好 hello py123你好 你好 py123你好")
# result = re.match(pattern,result)
# print(result.group())

# result = re.search(pattern,result)
# print(result.group())

# result = re.fullmatch(pattern,result)
# print(result.group())

# result = re.findall(pattern,result)
# print(result)

#返回分割列表
# result = re.split(pattern,result)
# print(result)

#返回替换
# result = re.sub("py123","py1811","py123你好 hello py123你好 你好 py123你好")
# print(result)

#返回迭代器
# result = re.finditer(pattern,result)
# for i in result:
#     print(i.group())

# pat = re.compile("123")
# print(pat)
# result = pat.search("123456")
# print(result)

