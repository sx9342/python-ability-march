# 1. 我们需要完成乐高商店的分析，请你根据指引完成以下任务：
# 1. 使用 Pandas 读取数据；
# 2. 去掉没有价格的数据，将销量为空的数据填充为0；
# 3. 计算所有产品总收入；
# 4. 计算该数据中产品价格的平均值;
# 5. 程序后台传入产品标题title，要求计算该产品的收入（收入总计）；
# 6. 将总收入、平均价格、产品收入保存到列表里，返回给后台。
# 题目要求
# 1. 程序传入标题title数据类型是str；
# 2. 程序传出数据类型是列表类型，列表中所有元素的数据类型均是 float；
# 3. 如果产品标题title存在多个，则计算相同title商品的总收入；
# 4. 平均价格需要四舍五入保留小数点后2位。
# 测试用例
# 输入：’乐高旗舰店官网大电影系列70837Shimmer&Shine闪亮水疗馆玩具积木’
# 输出；[xxx, xxx, 1598.0]
# 解释：总收入和平均价格隐藏，当前产品收入总计是1598.0
# 输入：’乐高旗舰店幻影忍者系列70668雷电忍者杰的暴风战机’
# 输出：[xxx, xxx, 259073.0]
# 解释：总收入和平均价格隐藏，当前产品收入总计是259073.0
# 输入：’乐高旗舰店官网创意百变高手系列10261大型过山车积木成人送礼’
# 输出：[xxx, xxx, 41986.0]
# import pandas as pd


# class Solution:
#     def task(self, title):
#         data = pd.read_excel("http://72.itmc.org.cn:80/JS001/data/user/16130/241/fj_lego_tmallshop_sales_data.xlsx")
#         # 去掉没有价格的数据，全部换成0
#         new_DataFrame = data[["title","price","sales_num"]]
#         new_DataFrame.fillna(0,inplace=True)
        
        
#         # 计算所有产品总收入
#         total_price = float((new_DataFrame["price"]*new_DataFrame["sales_num"]).sum()) #总收入
#         # 总销售量
#         total_sales_num = new_DataFrame["sales_num"].sum()
#         # 平均价格
#         avg_price = float((total_price / total_sales_num).round(2))
#         price_singele =new_DataFrame.loc[new_DataFrame["title"]==title]
#         price_singele_ = float(price_singele["price"]*price_singele["sales_num"])
#         return [total_price,avg_price,price_singele_]
#         pass
# sol = Solution().task("乐高旗舰店官网创意百变高手系列10261大型过山车积木成人送礼")    
# print(sol)
import pandas as pd

class Solution:
    def task(self, title):
        # 读取 Excel 文件
        data = pd.read_excel("http://72.itmc.org.cn:80/JS001/data/user/16130/241/fj_lego_tmallshop_sales_data.xlsx")
        
        # 对原始 DataFrame 进行填充缺失值
        data.fillna(0, inplace=True)
        
        # 提取所需列
        new_DataFrame = data[["title", "price", "sales_num"]]
        
        # 计算所有产品的总收入
        new_DataFrame["All_price"] = new_DataFrame["price"] * new_DataFrame["sales_num"] # 总收入
        
        # 总销售量
        total_sales = new_DataFrame["All_price"].sum()
        # 平均价格
        price_mean = new_DataFrame["price"].mean()        
        # 查找特定标题的产品并计算其销售额
        product_sales = new_DataFrame[new_DataFrame["title"] == title]["All_price"].sum()
        return [total_sales, price_mean.round(2), product_sales]
