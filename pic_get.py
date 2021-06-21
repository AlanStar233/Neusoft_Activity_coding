import requests

url = 'https://p1.ssl.qhimg.com/t013d604236ae4f79c2.jpg'
response = requests.get(url)
print(response.status_code)

# wb --> write binary
with open('likangju.jpg', mode='wb') as f:
    f.write(response.content)
