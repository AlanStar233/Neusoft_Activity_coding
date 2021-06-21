# 提取html中的元素
from lxml import html

with open('index.html', mode='r', encoding='utf-8') as f:
    data = f.read()

selector = html.fromstring(data)

h1 = selector.xpath('/html/body/h1/text()')
print(h1)
p = selector.xpath('/html/body/p/text()')
print(p)

baidu_text = selector.xpath('/html/body/div/a/text()')
print(baidu_text)

# 从任意位置定位标签名
tag = selector.xpath("//div[@id='container']/a/text()")
print(tag)

# 定位特定属性名
href = selector.xpath("//div[@id='container']/a/@href")
print(href)
