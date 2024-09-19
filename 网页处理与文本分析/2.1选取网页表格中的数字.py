# 1. 运行或提交代码不需要自己编写测试用例，后台自动进行测试检查。
# 2. 您编写代码的区域需要限制在Solution类或其他类和函数体内，保证输入与输出符合任务要求即可。
# 3. 点击“提交代码”按钮，系统将查看程序是否正确，并保存代码，记录任务数据。
# 4. 提交代码次数越多，任务得分越低。
# 5. 点击右上方“结束任务”按钮，系统将在后台计算任务得分，任务结束。
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


class Solution:

    def table_num(self, row: int, col: int) -> int:
        url = "http://72.itmc.org.cn/JS001/open/show/random-num/index.html"
        resp =  requests.get(url)
        page = BeautifulSoup(resp.text, "html.parser")
        target = page.find_all("tr")[row].find_all("td")[col]
        num = int(target.text)
        return num
        pass