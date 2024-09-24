import requests
import re
from bs4 import BeautifulSoup

# 尝试抓取古诗文网页面的源代码
url = "https://www.gushiwen.cn/shiwenv_75a1b85e870f.aspx"

resp = requests.get(url)
resp.encoding = resp.apparent_encoding
page = resp.text

# 把页面源代码装进去，告诉BS解析器是什么
soup = BeautifulSoup(page, 'html.parser')

# 如何解析
# 语法规则：soup.find('标签名', {'属性名':'属性值'})
contson = soup.find("div", {'class':'contson','id':"contson75a1b85e870f" })
tittle = soup.find('div',attrs={'id':'zhengwen75a1b85e870f'})
# 提取纯文本内容

text_content = contson.get_text(strip=True)
with open("送宗判官归滑台序.txt","w",encoding='utf-8') as file:
    file.write(tittle.text)
    file.write(text_content)
