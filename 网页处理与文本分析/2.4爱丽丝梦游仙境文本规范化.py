# 2.4：爱丽丝梦游仙境文本规范化
# 任务详情
# 采用Python自带的函数库进行数据操作，完成任务下方《爱丽丝梦游仙境》英文文本词频的分析。
# 请将右边的函数 aliceText() 补充完整，使其能够输出某个单词的词频。
# 任务要求
# 1. 不得直接使用 Jieba 库对文本进行分词；
# 2. 函数 aliceText() 接收一个英文单词 word，str 数据类型；返回该单词的词频，int 数据类型；
# 3. 只保留单词长度大于等于 3 的单词的词频统计；
# 4. 英文单词不区分大小写；
# 5. 不同时态和单复数的英文单词为不同英文单词，不需要合并词频统计。如果文本中没有该单词，词
# 频为0；
# 6. 文本可以使用 requests 库进行读取，UTF-8 编码方式，否则无法正确读取文本。
# 测试用例
# 输入：'Pictures' 输出：3
# 输入：'nothing' 输出：13
# 输入：'caterpillar' 输出：14
# 输入：'python' 输出：0

import re

import requests


class Solution:
    def aliceText(self, word: str) -> int:
        url = 'http://72.itmc.org.cn:80/JS001/data/user/16130/76/fj_alice_adventure.txt'
        
        text = requests.get(url).text
        
        text = text.lower() # 全部转换为小写，因为不区分
        words = re.findall(r'\b\w{3,}\b', text) # 采用正则表达式来忽略长度小于3的词汇
        word_count = words.count(word.lower()) 
        return word_count
    
        pass