import requests
import json
import parse
from lxml import html

# dynamic_id '538016418435871183'
# dynamic_id = input("Please type dynamic_id:")
url = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/get_dynamic_detail?dynamic_id=538016418435871183'  # .format(dynamic_id)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

# 配置response和html_data
resp = requests.get(url, headers=headers)
html_data = resp.text
selector = html.fromstring(html_data)

# 返回Python的数据类型
html_data = json.loads(html_data)

# 获取rid
rid = html_data['data']['card']['desc']['rid']

# 将rid传入api_url
api_url = 'https://api.bilibili.com/x/v2/reply?type=11&oid={}&sort=2&ps=49&pn=2'.format(rid)

# 配置api_resp、api_data、api_selector
api_resp = requests.get(api_url, headers=headers)
api_data = api_resp.text
api_selector = html.fromstring(api_data)

# 返回Python的数据类型
api_selector = json.loads(api_data)
print(api_selector)

# 定义list nick_name
nick_name = {}

# 获取昵称和UID
for info in api_selector:
    nick_name = api_selector['data']['replies']['member']['uname']
    # print(nick_name)
