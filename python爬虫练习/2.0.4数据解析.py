# re解析（正则表达式）
# bs4解析
# xpath解析
import re
# findall 匹配字符串中所有的符合正则的内容
# lst = re.findall(r"\d+", "1a2b3c4d5e")

# # finditer 匹配字符串中所有符合正则的内容，返回一个迭代器

# iter = re.finditer(r"\d+", "1a2b3c4d5e")
# for i in iter:
#     print(i.group())

# # search 匹配字符串中第一个符合正则的内容,只要找到结果就返回
# s = re.search(r"\d+", "1a2b3c4d5e")
# print(s.group())

# match 匹配字符串中第一个符合正则的内容，从字符串的开头开始匹配
# s = re.match(r"a\d+", "abc123")

# 预加载正则表达式
# obj = re.compile(r"\d+")
# ret = obj.finditer("1a2b3c4d5e")
# for i in ret: 
#     print(i.group())

# s = """<div class="Anon"><span id = "1">千早爱音</span></div>
# <div class="Soyo"><span id = "2">长崎素世</span></div>
# <div class="Takki"><span id = "3"椎名立希</span></div>
# <div class="Tomori"><span id = "4">高松灯</span></div>
# <div class="Rana"><span><span id = "5">要乐奈</span></span></div>
# """
# # (?P<name>正则) 可以单独提取内容
# obj = re.compile(r"<div class=\"(.*?)\">(.*?)</div>")
# ret = obj.finditer(s)
# for i in ret: 
#     print(i.group())

