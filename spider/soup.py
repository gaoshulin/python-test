import requests
from bs4 import BeautifulSoup

url = "https://juejin.cn/recommended?sort=newest"
response = requests.get(url, timeout=10)
html = response.text
if response.status_code == 200:
    with open('soup.html', 'w', encoding='utf-8') as f:
        f.write(html)
else:
    print("请求失败")

soup = BeautifulSoup(html, 'html.parser')

# 提取网页标题
tags = soup.select('#juejin > div > div > header > div > nav > ul > li > ul > li')
for tag in tags:
    link = tag.find('a')
    if link is not None and isinstance(link, BeautifulSoup):
        print('text:', link.text)
        # 使用link['href']来获取href属性值，而不是使用get()方法
        print('url:', link['href'] if 'href' in link.attrs else '')
        print('--------------------------')
