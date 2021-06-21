import requests
import json
import parse
from lxml import html

# dynamic_id '538016418435871183'
dynamic_id = input("Please type dynamic_id:")
url = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/get_dynamic_detail?dynamic_id={}'.format(dynamic_id)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
# 试请求访问目标地址
# r = requests.get(url)
# print(r.status_code)

# 配置response和html_data
resp = requests.get(url, headers=headers)
# print(resp.status_code)

html_data = resp.text
selector = html.fromstring(html_data)
# print(html_data)

# 返回Python的数据类型
html_data = json.loads(html_data)
# print(html_data)
# print(type(html_data))

# 返回json的数据类型,一定是""修饰
# html_data = json.dumps(html_data, indent=4)
# print(html_data)
# print(type(html_data))
# rid = str(html_data[])
# print(rid)

rid = html_data['data']['card']['desc']['rid']
print(rid)

