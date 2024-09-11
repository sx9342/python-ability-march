# 1.1：求两数之和
# 任务详情
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出“和”为目标值的两个整数，并返
# 回他们的数组下标。
# 你可以假设每种输入只会对应一个答案，数组中元素不能重复输入。
# 请根据上面的要求，编写相应的算法，将右边的函数 twoSum() 补充完整。
# 举例
# 给定 nums = [2, 7, 11, 15]，target = 9；
# nums[0] + nums[1] = 2 + 7 = 9，返回[0, 1]。
# 任务要求
# 1. 代码编写必须在右边指定的区域编写；
# 2. 函数接收两个变量，一个是整数数组 nums：list，另一个是目标值 target: int；
# 3. 如果存在两种或以上符合目标值 target 的情况，返回下标相加之和较小的数组；
# 4. 函数返回的值必须为一个数组，list数据类型，元素排序为正序排序，如返回 [1, 3] 符合条件，[3,
# 1] 不符合条件。
# 测试用例
# 用例一
# 输入：[2，3，2，4], 7
# 输出：[1, 3]
# 用例二
# 输入：[2, 6, 7, 7], 9
# 输出：[0, 2]

class Solution:
    def twoSum(self, nums: list, target: int):
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):  # j从i+1开始
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # 如果没有找到，返回空列表




