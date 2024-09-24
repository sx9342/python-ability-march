class Solution:

    
    def detectCapital(self, st: str) -> bool:
        """
        检测句子中的单词拼写是否符合规则。
        
        参数:
        st (str): 输入的英文句子。
        
        返回:
        bool: 如果句子中的单词拼写符合规则，则返回True；否则返回False。
        """
        
        # 将句子分割成单词列表
        word_li = st.split() 
        # 特殊单词列表，这些单词必须按特定形式出现
        special_word_li = ['Python', 'Java', 'MachineLearning', 'DataMining']
        
        # 遍历特殊单词列表，检查句子中的单词是否符合规则
        for word in special_word_li:
            # 检查句子第一个单词是否是特殊单词的小写形式，如果是且不在特殊单词列表中，则返回False
            if word.lower() == word_li[0].lower() and word_li[0] not in special_word_li:
                return False
            
            # 检查句子第一个单词的首字母是否应大写
            if word_li[0][0].isalpha() and word_li[0] not in special_word_li:
                if word_li[0][0].islower():
                    return False
            # 检查句子第一个单词是否为“数字+字母”形式，如果是，则检查字母部分是否全部大写
            if word_li[0][0].isdigit() and len(word_li[0]) >= 2 and not word_li[0][1:].isupper():    
                return False
            
            # 遍历句子中的其他单词，检查它们是否符合规则
            for word in word_li[1:]:
                for sw in special_word_li:
                    # 检查是否为特殊单词的小写形式，如果是且不在特殊单词列表中，则返回False
                    if word.lower() == sw.lower() and word not in special_word_li:
                        return False
                # 检查是否为“数字+字母”形式的单词，如果是，则检查字母部分是否全部大写
                if word[0].isdigit() and not word[1:].isupper():
                    return False
                # 检查非特殊单词是否符合规定的大小写规则
                if word not in special_word_li and not word.islower() and not word.isupper():    
                    return False
        # 如果所有单词都符合规则，则返回True
        return True
    
    # "I love Python"
    # “Love Python”