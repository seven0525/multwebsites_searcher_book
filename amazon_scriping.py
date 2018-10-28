import os


from amazon.api import AmazonAPI  # pip install python-amazon-simple-product-api

# 環境変数から認証情報を取得する。
AMAZON_ACCESS_KEY = "YOURS"
AMAZON_SECRET_KEY = "YOURS"
AMAZON_ASSOCIATE_TAG = "YOURS"

# AmazonAPIオブジェクトを作成する。キーワード引数Regionに'JP'を指定し、Amazon.co.jpを選択する。
amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOCIATE_TAG, Region='JP')

# search()メソッドでItemSearch操作を使い、商品情報を検索する。
# キーワード引数Keywordsで検索語句を、SearchIndexで検索対象とする商品のカテゴリを指定する。
# SearchIndex='All'はすべてのカテゴリから検索することを意味する。

titles = []

def main(key_word):
    products = amazon.search(Keywords=key_word, SearchIndex='Books')
    count = 0
    for product in products:  # 得られた商品（AmazonProductオブジェクト）について反復する。
        count += 1
        if count > 5: # 検索結果のうち上位3つのみを表示
            break
        titles.append(product.title)
    
    return titles[0], titles[1], titles[2], titles[3], titles[4]
        # print(product.title)      # 商品名を表示。
        # print(product.offer_url)  # 商品のURLを表示。
        # price, currency = product.price_and_currency
        # print(price, currency)    # 価格と通貨を表示。
