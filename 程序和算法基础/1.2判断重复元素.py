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
# 方法一：用集合强制排除重复元素，再进行就判断

# class Solution:
#     def arrayRepeat(self,arr:list):
#         lenth = len(arr)
#         odd = 0
#         even = 0
#         if lenth != len(set(arr)): # 转化成集合对比
#             for i in range(0,lenth):
#                 if  arr[i] == arr[i-1]:
#                     return "03" #有相同元素且相邻、
#             return "01" #有相同元素且不相邻    
#         else:
#             for i in range(lenth):
#                 if arr[i] %2 == 0:
#                     even +=1
#                 else:
#                     odd+=1
#             if even > odd:
#                 return "02"
#             else:
#                 return "03"
        


# 改进后方法1
# class Solution:
#     def arrayRepeat(self, arr: list):
#         length = len(arr)
#         odd = 0
#         even = 0
        
#         if length != len(set(arr)):  # 如果有重复元素
#             for i in range(1, length):  # 从1开始，避免访问负索引
#                 if arr[i] == arr[i-1]:  # 检查相邻元素是否相同
#                     return "03"  # 有相同元素且相邻
#             return "01"  # 有相同元素但不相邻
        
#         else:  # 没有重复元素
#             for i in range(length):
#                 if arr[i] % 2 == 0:
#                     even += 1
#                 else:
#                     odd += 1
            
#             if even > odd:
#                 return "02"  # 偶数多
#             elif odd > even:
#                 return "03"  # 奇数多
#             else:
#                 return "03"  # 偶数和奇数数量相等（新添加的条件）

# 方法2，用一个字典记录索引位置，并计算偶数和奇数的个数
# class Solution:
#     """
#     解决数组重复问题的类
    
#     此类中的方法用于检查数组中是否存在重复元素，并根据重复元素的状态返回不同的字符串标识。
#     """
    
#     def arrayRepeat(self, arr: list) -> str:
#         """
#         检查数组中是否存在重复元素，并根据重复元素的状态返回标识字符串
        
#         参数:
#         arr (list): 需要检查的数组
        
#         返回:
#         str: 根据重复元素状态返回的标识字符串
#         """
#         # 初始化字典用于记录元素的索引位置
#         index_map = {}
#         # 初始化偶数和奇数的计数器
#         odd = 0
#         even = 0
        
#         # 遍历数组，记录每个元素的索引位置，并计算偶数和奇数的个数
#         for i in range(len(arr)):
#             # 如果当前元素在字典中存在且距离上次出现的位置大于1，则有相同元素且不相邻
#             if arr[i] in index_map and i - index_map[arr[i]] > 1:
#                 return "01"  # 返回标识字符串，表示有相同元素且不相邻
#             # 记录当前元素的索引
#             index_map[arr[i]] = i
            
#             # 根据当前元素是偶数还是奇数，更新对应的计数器
#             if arr[i] % 2 == 0:
#                 even += 1
#             else:
#                 odd += 1
        
#         # 检查是否偶数个数大于奇数个数
#         if even > odd:
#             return "02"  # 返回标识字符串，表示偶数个数大于奇数个数
#         else:
#             return "03"  # 返回标识字符串，表示偶数个数不大于奇数个数

# 改进后方法2
class Solution:
    def arrayRepeat(self, arr: list) -> str:
        index_map = {}
        odd = 0
        even = 0
        
        # 遍历数组，记录每个元素的索引位置，并计算偶数和奇数的个数
        for i in range(len(arr)):
            if arr[i] in index_map:  # 检查是否遇到重复元素
                if i - index_map[arr[i]] == 1:  # 如果相邻
                    return "03"  # 有相同元素且相邻
                else:
                    return "01"  # 有相同元素且不相邻
            index_map[arr[i]] = i  # 记录当前元素的索引
            
            # 统计偶数和奇数个数
            if arr[i] % 2 == 0:
                even += 1
            else:
                odd += 1
        
        # 检查是否偶数个数大于奇数个数
        if even > odd:
            return "02"  # 偶数多于奇数
        else:
            return "03"  # 奇数多或相等
