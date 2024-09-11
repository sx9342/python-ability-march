# 1.2：判断数组重复元素
# 任务详情
# 编写一个函数 arrayRepeat()，对于任意输入的一个整数数组，如果整数数组中存在重复元素且重复元
# 素均不相邻，函数返回 字符"01"；
# 如果整数数组每个元素均不相同且偶数元素个数大于奇数元素个数，函数返回字符"02"；
# 如果整数数组均不满足上述两个条件，函数返回字符 "03"
# 任务要求
# 1. 代码编写必须在右边指定的区域编写；
# 2. 函数接收一个变量 arr，list 数据类型；
# 3. 函数返回值必须为字符串数据类型。
# 测试用例
# 输入：[1, 2, 6, 4, 6] 输出：'01'；
# 输入：[2, 3, 8, 5, 6] 输出：'02'；
# 输入：[2, 2, 5, 3, 5] 输出：'03'；
# 输入：[0, 0, 0, 0, 0] 输出：'03'

class Solution:
    def arrayRepeat(self,arr:list):
        lenth = len(arr)
        odd = 0
        even = 0
        if lenth != len(set(arr)): # 转化成集合对比
            for i in range(0,lenth):
                if  arr[i] == arr[i-1]:
                    return "03" #有相同元素且相邻、
            return "01" #有相同元素且不相邻    
        else:
            for i in range(lenth):
                if arr[i] %2 == 0:
                    even +=1
                else:
                    odd+=1
            if even > odd:
                return "02"
            else:
                return "03"
        


