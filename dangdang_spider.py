import requests
# import pymssql
from lxml import html

# ISBN = '9787513919524'
ISBN = input("Please type book's number:")
url = 'http://search.dangdang.com/?key={}&act=input'.format(ISBN)

# 配置response和html_data
response = requests.get(url)
html_data = response.text

# 选择器定义
selector = html.fromstring(html_data)
book_list = selector.xpath('//div[@id="search_nature_rg"]/ul/li')

# 创建数据库
# db = pymssql.connect(server='ROG-STRIX-ALAN\MSSQLSERVER01', database='DangDang_result', charset='utf-8')
# cursor = db.cursor()
# sql = '''
# create table DangDangResult(
# book_name varchar(100),
# book_price varchar(20),
# book_link varchar(100),
# book_store varchar(50)
# )
# '''

# 遍历book_name
for li in book_list:
    # book_name
    book_name = li.xpath('p[@class="name"]/a/text()')
    print(book_name)
    # book_price
    book_price = li.xpath('p[@class="price"]/span[@class="search_now_price"]/text()')
    book_price = book_price[0].replace("¥", "")
    print(book_price)
    # book_link
    book_link = li.xpath('p[@class="name"]/a/@href')
    print(book_link)
    # book_store
    book_store = li.xpath('p[@class="search_shangjia"]/a/@title')
    print(book_store)