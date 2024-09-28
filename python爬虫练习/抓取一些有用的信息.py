# 导入requests库，用于发送HTTP请求
import requests
# 导入BeautifulSoup库，用于解析HTML内容
from bs4 import BeautifulSoup

# 定义目标URL，指向需要抓取的网页地址
url = "https://soc.ustc.edu.cn/COD/other/ask/#:~:text=%E8%BF%99%E7%AF%87%E6%96%87%E7%AB%A0%E8%AE%A9%E5%A4%A7%E5%AE%B6%E4%BA%86%E8%A7%A3%E5%87%A0"
# 发送GET请求，获取网页内容
res = requests.get(url)
# 设置正确的编码方式，确保内容正确解析
res.encoding = "utf-8"
# 使用BeautifulSoup对网页内容进行解析
soup = BeautifulSoup(res.text, "html.parser")

# 查找所有的<p>标签，这些标签通常包含段落文本
text = soup.find_all("p")
# 遍历所有找到的段落标签，提取文本内容
text = [text.get_text(strip = True) for text in text]

# 打开（或创建）一个名为"ustc.txt"的文件，用于写入提取的文本内容
with open("ustc.txt", "w", encoding = "utf-8") as file:
    # 将提取的文本内容写入文件，每个段落文本后写入一个新行
    file.write("\n".join(text))
    # 文件操作完成后，关闭文件
    file.close()