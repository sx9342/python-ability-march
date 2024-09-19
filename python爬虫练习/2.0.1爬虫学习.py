import requests

url = "https://www.bing.com/search?q=周杰伦"

headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

resp = requests.get(url,headers = headers)
print(resp.text)
