# 1.4：句子拼写检查
# 任务详情
# 给定一段英文句子，判断句中单词拼写是否满足以下规则。
# 除以下特殊情况外，句子中第一个单词首字母必须大写，其它所有单词小写：
# 1. 如果句中的某个单词或短语，字母全部为大写，则该单词或短语拼写正确。比如“USA”、“UK”、
# “JUST DO IT”等；
# 2. “Python”、“Java”、“MachineLearning”、“DataMining”四个单词必须为双引号中给出的形式，否
# 则拼写不正确；
# 3. 如果句中单词为“数字+字母”的混合形式，比如“5G”，该单词所有字母全部大写。
# 任务要求
# 1. 输入英文句子为 str 类型，输出为 bool 类型；
# 2. 如果句子满足规则要求，程序返回结果为 True；否则返回 False。
# 测试用例
# 输入：'I love Python' 输出：True
# 输入：'python love me' 输出：False

class Solution:
    def detectCapital(self, st: str) -> bool:
        word_li = st.split() 
        special_word_li = ['Python', 'Java', 'MachineLearning', 'DataMining']
        for word in special_word_li:
            if word.lower() == word_li[0].lower() and word_li[0] not in special_word_li:
                return False
            
            if word_li[0][0].isalpha() and word_li[0] not in special_word_li:
                if word_li[0][0].islower():
                    return False
            if word_li[0][0].isdigit() and len(word_li[0]) >= 2 and not word_li[0][1:].isupper():    
                return False
            for word in word_li[1:]:
                for sw in special_word_li:
                    if word.lower() == sw.lower() and word not in special_word_li:
                        return False
            if word[0].isdigit() and not word[1:].isupper():
                return False

            if word not in special_word_li and not word.islower() and not word.isupper():    
                return False
        return True      