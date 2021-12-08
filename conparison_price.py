import requests
from bs4 import BeautifulSoup



search_word = input('比較したい商品を入力してください : ')

# 楽天市場から商品のタイトルを取得する関数
def get_rakuten():
    # 価格が安いかつ送料が無料の順の検索ページを取得している
    url = 'https://search.rakuten.co.jp/search/mall/' + search_word + '/' + '?filter=fs&s=2'
    # url = 'https://search.rakuten.co.jp/search/mall/pythonチュートリアル/'
    responce = requests.get(url)
    # .textでそのページのg¥htmlを取得している
    html = responce.text
    # 解析する
    soup = BeautifulSoup(html, 'html.parser')
    # 商品のタイトルだけを取得する webサイトで検証し取得したい箇所を調べる
    items = soup.select('.searchresultitem')
    
    # 商品番号をつける
    item_number = 0
    # 商品の価格をリスト化
    price_list = []
    
    for item in items:
        # .select_one()で見つけた１つ目を取得しリスト型にすることはない
        title = item.select_one('.title')
        # 商品の価格を取得する
        price = item.select_one('.important').text.replace(',', '').replace('円', '')
        price_list.append(price)
        print('【' + str(item_number) + '】 '  + format(title.text))
        print('【価格】: {}'.format(price))
        print('\n')
        item_number += 1
        
    selected_item_number = int(input('楽天 : 商品番号を入力してください : '))
    selected_price = int(price_list[selected_item_number])
    return selected_price
    

rakuten_price = get_rakuten()
# print(rakuten_price)
