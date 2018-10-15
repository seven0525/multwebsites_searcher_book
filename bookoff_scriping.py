import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def amazon_get(key):
    r = requests.get("http://www.bookoffonline.co.jp/display/L001,q={}".format(key))
    soup = BeautifulSoup(r.content, 'html.parser')
    titleTags = soup.find_all('p', class_="itemttl")
    names = []
    for titleTag in titleTags:
        name = titleTag.text.strip()
        names.append(name)
    names_uniq = []
    for d_name in names:
        if d_name not in names_uniq:
            names_uniq.append(d_name)
    print(names_uniq)

key_word = input("検索したい本のキーワードを入力してください")
amazon_get(key_word)