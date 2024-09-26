import re

import bs4
import requests
from bs4 import BeautifulSoup

class Solution:
    def BoxOfficeSpider(self,moive_name:str) -> list:
        # 获取请求
        url = 'http://72.itmc.org.cn:80/JS001/open/show/box_office_on_a_certain_day.html'
        resp = requests.get(url)
        resp.encoding = 'utf-8'

        #初始化结果数组
        #results = [0,0.00,0.00] #按照[int,float,float]初始化，即上映天数，综合票房（万元），排片占比
        # 数据处理
        soup = BeautifulSoup(resp.text, 'html.parser')
        moive = soup.find_all('div',{'class': 'name-wrap'})#拿到电影名称的Html
        
        moive_text = [moives.get_text(strip=True) for moives in moive] #用推导式将标签去掉

        moive_data_html = soup.find_all('div',{'class': 'boxDesc-wrap red-color'}) # 这是一个关于票房的中间变量

        moive_data_ticket = [moive_data.get_text(strip=True) for moive_data in moive_data_html] #爬取综合票房并去掉标签

        moive_row_html = soup.find_all('div',{'class': 'countRate-wrap'}) # 这是一个关于排片的中间变量
        moive_row = [moive_row.get_text(strip=True) for moive_row in moive_row_html] #爬取排片占比并去掉标签
        moive_all = {}
        # 将所有的电影名称装入列表
        moive_names = [] #拿到电影名称
        moive_day_sum = []#统计电影的上映时间

        for i in moive_text:
            match = re.search(r'(.+?)(?=上映|首日|点映)', i) # 提取出电影名称，用正则表达式优化算法
            if match:
                name_str = match.group(0).strip() # 匹配到字符串加入临时变量
                moive_names.append(name_str)

                if '上映' in i:
                    moive_day_match = re.search(r'(\d+)天', i)
                    moive_day = int(moive_day_match.group(1)) if moive_day_match else 0 # 这里用了三元运算符，相当巧妙
                    moive_day_sum.append(moive_day)
                else:
                    moive_day_sum.append(-1 if '点映' in i else 0)        
        # for i in moive_text: #用循环自动提取影片名称以及上映时间
        #     if '上映' in i and '首日' not in i:
                
        #         name_str = i[ :i.find('上映')]
        #         moive_names.append(name_str)
        #         moive_day = i[i.find('上映')+2:i.find('天',1)]#电影名《天道王》里面的"天"产生干扰
        #         moive_day_sum.append(int(moive_day))
        #     elif '上映首日' in moive_text and '首日' in i:
        #         name_str = i[:i.find('上映首日')]
        #         moive_names.append(name_str)
        #         moive_day =0
        #         moive_day_sum.append(moive_day)     
        #     elif '点映' in i:
        #         name_str = i[:i.find('点映')]
        #         moive_names.append(name_str) 
        #         moive_day = -1
        #         moive_day_sum.append(moive_day)   
        # 排片数据格式化
        moive_row_data = []
        for i in moive_row:
              if '%' in i and '<' not in i:
                  row = i[:i.find('%')]
                  row =round(float(row)*0.01,3)
                  
                  moive_row_data.append(row)
              elif '<' in i and '%' in i:
                  moive_row_data.append(0.001)

        
        moive_all = {moive_names[i]: [moive_day_sum[i],float(moive_data_ticket[i]),moive_row_data[i]] for i in range(0,len(moive_names)) } #找个字典把所有数据装起来
        
        for fname,fvalue in moive_all.items():
            if moive_name == fname:
                return fvalue
                
        print(moive_all)
        
                        
#Solution().BoxOfficeSpider()   
 