# 任务详情
# 下方的网页为微信公共号数据分析展示页，网页数量为1。

# 请根据网页给出的信息，完成以下任务，将右边的函数 weixinData() 补充完整。

# 给定原创排行榜里任一微信公众号的名称，请判断该公众号是否满足以下条件：

# 1.“头条平均阅读”数 > 90000

# 2.“原创平均阅读”数 > 80000

# 3.“预估活跃粉丝”数 < 300万

# 如果满足，函数 weixinData() 返回大写英文单词“YES”，否则返回“NO”。

# 任务要求
# 1. 函数接收 str 数据类型的微信公众号名称 name；

# 2. 函数返回为英文字符“YES”或“NO”，返回参数为 str 数据类型；

# 3. 不得修改函数 weixinData() 的名称；

# 4. 题目所需网站链接已经在下方给出，编码方式为UTF-8。

# 测试用例
# 输入：“占豪”            输出：“NO”

# 输入：“Vista看天下” 输出：“YES”


# -*- coding: utf-8 -*-
import re

import requests
import bs4
from bs4 import BeautifulSoup

class Solution:
    def weixinData(self, name: str) -> str:
        url = 'http://72.itmc.org.cn:80/JS001/open/show/weixindata.html'
        resp = requests.get(url) 
        resp.encoding = 'utf-8'
        resp_text = resp.text 
        soup = BeautifulSoup(resp_text,'html.parser') # 解析网页，解析器为html.parser
        span_list = soup.find_all("span",{'class':"",'data-bizid':""})
        span_text = [span.get_text(strip=True) for span in span_list]

        p_name = span_text[:-1] # 公众号名称和账户

        td_num = soup.find_all('td',{'class':""})

        td_text = [td.get_text(strip=True) for td in td_num ]

        filtered_td_text = [text for text in td_text if text != "详情"] # 这里涉及到我的知识盲区，列表推导式（list comprehension）new_list = [expression for item in iterable if condition]

        # 调整数据，将数据中的“万”和万+去掉，改成浮点数
        processed_td_text = []
        for text in filtered_td_text:
            if "万" in text or "万+" in text:
                num_str = text.replace("万", "").replace("万+", "") # 去掉 “万”
                if num_str.isdigit(): # 判断是否为纯数字
                    num = float(num_str) * 10000 
                elif '+' in num_str: #一旦出现了x+这种不确定数据就把它视作很大的值
                    # 将 '10+' 视作一个较大的数值，例如 100000
                    num = 100000
                else:
                    num = float(num_str) * 10000
                processed_td_text.append(float(num))
            else:
                processed_td_text.append(float(text))
                

        # 将两个数据以1对8的映射放入字典
        details_per_name = len(processed_td_text) // len(p_name)
        data_dict = {
            p_name[i]: processed_td_text[i * details_per_name : (i + 1) * details_per_name]
            for i in range(len(p_name))
        } # 此处存储数据的方法：字典推导式和嵌套切片

        # 遍历字典，判断是否满足条件
        for fname,details in data_dict.items():
            if name in fname:
                if details[1] < 3000000 and details[2] > 90000 and details[5] > 80000:
                    return 'YES'
                else:
                    return 'NO'
        
        

         
        pass  