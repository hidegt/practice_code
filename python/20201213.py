money = 5000
print('お財布の中に' + str(money) + '円あります。\nスーパーで果物を買いましょう。')

fruits = ['りんご', 'オレンジ', 'イチゴ', 'バナナ', 'ぶどう']
price = [100,150,400,200,700]
for fruit, p in zip(fruits,price):
    print(fruit + ':' + str(p) + '円')
for fruit, p in zip(fruits,price):
    amount = input(fruit + 'を何個買いますか')
    new_price = int(amount) * p
    print(fruit + '個、' + str(new_price) + '円')

# 続き
# 財布残高から合計金額を引いていく
# ０円になったら
# 財布がからになりました
# 財布残高をこしたら
# お金がたりません