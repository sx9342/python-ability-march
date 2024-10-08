# 任务详情
# 给定一个DataFrame对象 df，要求返回各行的平均值。
# 具体操作如下：

# 添加新列 'avg' 用于计算各行的平均值；

# 使用数组返回新列 'avg'。

# 任务要求
# 程序接收 DataFrame 对象 df，返回结果是 list 数据类型；

# 注意：平均值需要四舍五入保留两位小数。
import pandas
class Solution:
    
    def CalAvg(self, df: 'pandas.DataFrame') -> list:
        df["avg"] = df.mean(axis=1).round(2) # 添加新列，列为平均值mean，axis=1表示行的平均值，round(2)表示保留两位小数
        return df["avg"].tolist() # 返回新列,转换为list