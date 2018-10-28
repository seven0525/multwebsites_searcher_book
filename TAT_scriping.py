import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main(key_word):
    r = requests.get("https://libwebservice.biblio.tuat.ac.jp/opac/opac_search/?lang=0&amode=2&appname=Netscape&version=5&cmode=0&smode=0&kywd={}".format(key_word))
    soup = BeautifulSoup(r.content, 'html.parser')
    titleTags = soup.find_all('span', class_="tit_name")
    names = []
    for titleTag in titleTags:
        name = titleTag.text.strip()
        names.append(name)
    names_uniq = []
    for d_name in names:
        if d_name not in names_uniq:
            names_uniq.append(d_name)
    # print(names_uniq)
    return names_uniq[0], names_uniq[1], names_uniq[2], names_uniq[3], names_uniq[4]

# key_word = input("検索したい本のキーワードを入力してください")
# amazon_get(key_word)
