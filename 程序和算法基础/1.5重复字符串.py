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
    def repeatString(self, s: str) -> str:
        lenth = len(s)
        for i in range(1,lenth//2+1):
            if lenth % i == 0 and s[:i] * (lenth//i) == s:
                return s[:i]
            return s
        
        