# queen
Q = 4
#左上、左下に数字がないかチェック
def check(x, col):
    for i , row in enumerate(reversed(col)):
      #enumerate 要素とインデックスを取得
      #reversed 要素を要素を逆順に取り出すイテレータを生成
        if ( x + i + 1 == row) or (x - i - 1 == row):
          return False
    return True

def search(col):
    if len(col) == Q:
        print(col)
        return

    for i in range(Q):
      #not in  iの中にcolがない場合true
      if i not in col:
          if check(i,col):
              #col=iの配列番号
              #例　３つめのcolをチェックしている場合
              #(i,col)
              #i=0(for文で順に代入)
              #col=1,3が入っている(関数などでチェック完了したもの)
              col.append(i)
              #trueの場合、iがcolに追加される
              search(col)
              col.pop()
search([])
#１０までなら問題なし。数字大きくなるに連れて莫大な時間がかかる