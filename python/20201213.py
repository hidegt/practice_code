# お買い物
import sys

money = 5000
print('お財布の中に' + str(money) + '円あります。\nスーパーで果物を買いましょう。')

fruits = ['りんご', 'オレンジ', 'イチゴ', 'バナナ', 'ぶどう']
price = [100,150,400,200,700]
for fruit, p in zip(fruits,price):
    print(fruit + ':' + str(p) + '円')
for fruit, p in zip(fruits,price):
    amount = input(fruit + 'を何個買いますか')
    new_price = int(amount) * p
    print(fruit + amount + '個、' + str(new_price) + '円')
    if new_price > money:
        print('お金がたりません。' + fruit + 'を買えませんでした。')
        sys.exit()
    elif money - new_price == 0:
        print('財布が空になりました。買い物を終了します。')
        sys.exit()
    else:
        money = money - new_price
        print('残金は' + str(money) + '円です。')