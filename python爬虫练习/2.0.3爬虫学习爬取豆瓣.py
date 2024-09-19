import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}
# 重新封装参数
url = "https://movie.douban.com/typerank"
param = {
    "type": "24",
    "interval_id": "100:90",  
    "action": ""
}
resp =  requests.get(url=url, params=param,headers = headers)

print(resp.text)
resp.close() # 访问结束后关闭连接