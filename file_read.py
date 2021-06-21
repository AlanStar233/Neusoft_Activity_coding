#file read
text = 'This is my content'

with open('content.txt', mode='w', encoding='utf-8') as f:
    f.write(text)

with open('index.html', mode='r', encoding='utf-8') as f:
    data = f.read()
print(data)

