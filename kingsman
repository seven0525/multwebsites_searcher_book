from urllib.request import urlopen
from bs4 import BeautifulSoup


def amazon_get(key):
    url ="https://www.amazon.co.jp/s/ref=nb_sb_noss_2?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&url=search-alias%3Dstripbooks&field-keywords={0}&rh=n%3A465392%2Ck%{0}".format(key)
    html = urlopen(url)
    data = html.read()
    html = data.decode("utf-8")
    soup = BeautifulSoup(html,"html.parser")
    book_name = soup.select("#result_0 > div > div:nth-of-type(3) > div:nth-of-type(1) > a > h2")
    print(book_name)

amazon_get("nature")
