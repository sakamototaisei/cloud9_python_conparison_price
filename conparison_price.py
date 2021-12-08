import requests
from bs4 import BeautifulSoup


# 楽天市場から商品のタイトルを取得する関数
def get_rakuten():
    url = 'https://search.rakuten.co.jp/search/mall/pythonチュートリアル/'
    responce = requests.get(url)
    # .textでそのページのg¥htmlを取得している
    html = responce.text
    # 解析する
    soup = BeautifulSoup(html, 'html.parser')
    # 商品のタイトルだけを取得する webサイトで検証し取得したい箇所を調べる
    items = soup.select('.searchresultitem')
    
    for item in items:
        # .select_one()で見つけた１つ目を取得しリスト型にすることはない
        title = item.select_one('.title')
        print(title.text)
    
    

get_rakuten()