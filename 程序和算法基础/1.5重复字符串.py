# 1.5：重复字符串
# 任务详情
# 给定一个字符串 s，判断它是否由它的子串重复多次构成。如果由子串重复多次构成，输出子串，否则
# 输出整个字符串。
# 任务要求
# 1. 给定字符串 s 为 str 类型，输出字符串为 str 类型。
# 测试用例
# 输入：'abcabc'
# 输出：'abc'
# 输入：'abefd'
# 输出：'abefd
class Solution:
    
    def patternRepeatedSubstring(self, s: str) -> str:
    
        length = len(s)
        
        # 遍历从1到字符串一半的长度
        for i in range(1, length // 2 + 1):
            # 如果当前长度可以整除字符串总长度，并且当前子串重复可以构成整个字符串
            if length % i == 0 and s[:i] * (length // i) == s:
                return s[:i]
        
        # 如果没有符合的子串，返回整个字符串
        return s