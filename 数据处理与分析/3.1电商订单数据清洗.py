# 任务详情
# 请根据系统提供的订单数据表，按要求完成以下任务：
# 统计订单表格中，商品描述(choice_description)中为“NaN”的数量，并将其批量替换为“banana”，
# 请根据以上要求，将函数 nanCount() 补充完整，函数的返回值为整数值，既为“NaN”的数量。
# 任务要求
# 1. 订单数据表为以逗号为分隔符的csv文件，编码方式为 UTF-8；
# 2. 注意：DataFrame 由后台生成，作为参数 order_data 传递到 nonCount() 中，不需要生成新的
# DataFrame；
# 3. DataFrame 读取为订单数据表；
# 4. 返回值为 NaN 的数量，int 数据类型。
# 订单数据访问地址请见下方：
class Solution:
    def nanCount(self, order_data:'DataFrame') -> int: # 此题不用编写文件读取，只需要做好数据处理操作即可
        # 从此处开始编写代码
        # 后台读取csv示例代码如下（参考）
        # order_data = pandas.read_csv(url, sep=',')
        num = int(order_data['choice_description'].isna().sum()) # 获取NaN的数量，计数
        order_data['choice_description'].fillna('banana', inplace=True)# 批量替换为“banana”
        return num