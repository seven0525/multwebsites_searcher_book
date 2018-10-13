import requests
from bs4 import BeautifulSoup

r = requests.get('https://hikkoshi.suumo.jp/sankaku/')
soup = BeautifulSoup(r.text, 'html.parser')
titleTags = soup.select('a')
names = []
for titleTag in titleTags:
    name = titleTag.text.strip()
    names.append(name)
#distinct_names = list(set(names))

names_uniq = []
for d_name in names:
    if d_name not in names_uniq:
        names_uniq.append(d_name)


print(names_uniq)

