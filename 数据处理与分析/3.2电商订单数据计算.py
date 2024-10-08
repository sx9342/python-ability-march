# 3.2：电商订单数据计算
# 任务详情
# 请根据系统提供的订单数据表，按要求完成以下三个任务：
# 传入一个字符串，返回订单总金额 (quantity * item_price) 最大或最小的商品，并返回商品的名称
# (item_name)。
# 请根据以上要求，将函数 salesStr() 补充完整，函数的返回值为字符(str)，比如："Steak Burrito"
# 订单数据访问地址请见下方：
# 字段名 中文含义
# order_id 商品编号
# quantity 数量
# item_name 商品名称
# choice_description 描述
# item_price 单价
# 任务要求
# 1. 传入一个字符串('max' 或 'min')，返回订单总金额最大或最小的商品的名称(item_name) ；
# 2. 传入的字符串不区分大小写，即传入值可能是"Max"，也可能是"max"；
# 3. 传入"max"，返回订单总金额 (quantity * item_price) 最大的商品名称；传入“min”，返回订单总
# 金额 (quantity * item_price) 最小的商品名称；
# 4. 返回字符串区分大小写，且保留字符串中间空格。

import pandas as pd

class Solution:
    def salesStr(self, condition: str) -> str:
        url = 'http://72.itmc.org.cn:80/JS001/data/user/16130/80/fj_order_data.csv'
        chipo = pd.read_csv(url, sep=',')
        
        # 锁定“item_name”,"item_price","quantity"
        item_data = chipo[["item_name", "item_price", "quantity"]]
        
        # 去掉“$”并转换为浮点数
        item_data["item_price"] = item_data["item_price"].str.replace('$', '').astype(float)
        
        # 计算总价
        item_data["sales"] = item_data["item_price"] * item_data["quantity"]
        
        # 分组并计算总销售额
        grouped_data = item_data.groupby("item_name")["sales"].sum().reset_index()
        
        # 按销售额降序排序
        sorted_data = grouped_data.sort_values(by="sales", ascending=False)
        
        if condition.lower() == "max":
            return str(sorted_data.iloc[0]["item_name"])
        elif condition.lower() == "min":
            return str(sorted_data.iloc[-1]["item_name"])

# 示例调用
solution = Solution()
print(solution.salesStr("max"))