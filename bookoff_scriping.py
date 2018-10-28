import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main(key_word):
    r = requests.get("http://www.bookoffonline.co.jp/display/L001,q={}".format(key_word))
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
    # print(names_uniq)

    return names_uniq[0], names_uniq[1], names_uniq[2], names_uniq[3], names_uniq[4]
