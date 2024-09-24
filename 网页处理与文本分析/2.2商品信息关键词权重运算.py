# 任务详情
# 根据提供的商品文本信息，对商品的标题内容、属性内容和描述内容进行分词（不包含标题和商品的属
# 性名），完成文本分析工作。
# 请根据以上要求，将以下所需的函数补充完整。
# 本任务提供了 jieba 中文分词库和 requests 库。
# 任务要求
# 1. 构建函数 wordTfidf()，对商品中除停用词外的关键词，计算其TF-IDF值；
# 2. 返回文本中 TF-IDF 最大的前5个关键词，返回结果为 list 数据类型；
# 3. 只保留词性为 n、nr、ns 的关键词；
# 4. 下方给出的文本编码为UTF-8。
# 测试用例
# 输入：任务中商品信息
# 输出：['裙子', '', '', ...]
# （此处隐藏剩余四个关键词的数据）

import requests
import jieba
from jieba import analyse


class Solution:

    def wordTfidf(self) -> list:
        # 获取商品信息，获取页面源代码
        url = "http://72.itmc.org.cn:80/JS001/data/user/16130/61/fj_chiffon_lady_dress.txt"
        resp = requests.get(url)
        resp.encoding = resp.apparent_encoding # 自动设置编码
        product_info = resp.text #保存商品信息

        # 用jieba库进行分词
        results = analyse.extract_tags(product_info,topK = 5, allowPOS=('n','nr','ns')) # 这是官方文档给出的求tf-idf值的函数，请参考https://github.com/fxsjy/jiebajieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
        # sentence 为待提取的文本
        # topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
        #withWeight 为是否一并返回关键词权重值，默认值为 False
        #allowPOS 仅包括指定词性的词，默认值为空，即不筛选
        return results

        pass

