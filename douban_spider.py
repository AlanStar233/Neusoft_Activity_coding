import requests
import os
from lxml import html

location = input("Please type your location:")
url = 'https://movie.douban.com/cinema/later/{}/'.format(location)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

# 配置response和html_data
resp = requests.get(url, headers=headers)
html_data = resp.text
selector = html.fromstring(html_data)

# 选择器
selector = html.fromstring(html_data)
movie_list = selector.xpath('//div[@id="showing-soon"]/div')

# 检测&创建imgs 文件夹
if not (os.path.exists('imgs')):
    os.makedirs('imgs')

# 封面
for movie in movie_list:
    # 获得图片地址
    img_src = movie.xpath('a/img/@src')[0]
    # 获得图片名称
    movie_name = movie.xpath('div[@class="intro"]/h3/a/text()')[0]
    # 下载图片
    img_data = requests.get(img_src).content

    # 图片处理&写入
    with open('./imgs/{}.jpg'.format(movie_name), mode='wb') as f:
        f.write(img_data)

    # 打印影片名称
    print(movie_name)
    # 上映日期
    movie_coming_date = movie.xpath('div[@class="intro"]/ul/li[1]/text()')[0]
    print(movie_coming_date)
    # 影片类型
    movie_type = movie.xpath('div[@class="intro"]/ul/li[2]/text()')[0]
    print(movie_type)
    # 上映地区
    movie_coming_area = movie.xpath('div[@class="intro"]/ul/li[3]/text()')[0]
    print(movie_coming_area)
    # 想看人数
    movie_waiting_people = movie.xpath('div[@class="intro"]/ul/li[@class="dt last"]/span/text()')[0]
    print(movie_waiting_people)
