import requests
url = 'https://fanyi.baidu.com/sug'

s = input("请输入要翻译的单词: ")

data = {
    'kw': s
}
# 发送请求,发送的数据必须放在字典中，通过data参数传递
resp = requests.post(url, data = data)

print(resp.json()) #服务器返回的内容直接处理成Json
