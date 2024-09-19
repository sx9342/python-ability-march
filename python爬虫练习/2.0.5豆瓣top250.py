# 拿到页面源代码 requests
# 正则表达式提取有效信息 re
import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}
resp = requests.get(url, headers=headers)  # 拿到页面源代码

# 确保请求成功
if resp.status_code == 200:
    # 解析 HTML 内容
    html_content = resp.text

    # 定义正则表达式模式
    pattern_movie = re.compile(r'<span class="title">([\u4e00-\u9fa5]+)</span>')  # 匹配中文电影名称
    pattern_rating = re.compile(r'<span class="rating_num" property="v:average">(\d\.\d)</span>')  # 匹配评分

    # 提取电影名称
    movie_names = pattern_movie.findall(html_content)
    # 提取评分
    ratings = pattern_rating.findall(html_content)

    # 打开 CSV 文件并写入数据
    with open("data.csv", mode="w", newline='', encoding='utf-8') as f:
        csvwriter = csv.writer(f)
        # 写入 CSV 文件的标题行
        csvwriter.writerow(["name", "rating"])
        # 打印结果并写入 CSV 文件
        print("豆瓣电影Top250：")
        for i in range(len(movie_names)):
            print(f"{i+1}. {movie_names[i]}, 评分: {ratings[i]}")
            csvwriter.writerow([movie_names[i], ratings[i]])
    
    print("数据已保存到 data.csv 文件中。")

else:
    print("请求失败，请检查 URL 或网络连接。")