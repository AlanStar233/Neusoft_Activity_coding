from lxml import html
import requests

r = requests.get(url='https://www.bilibili.com')
print(r.status_code)