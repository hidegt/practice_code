# 初めてのpython
# print('Hello word')

# 代入
# a = 10
# b =20 + 10
# print(a + b)

# リスト
# a = [3,4,5,1,2]
# print(a[2])
# print(a[0:3])
# print(a[:-4])

a = 'dog'
b = ['dog', 'cat', 'caw']
# aという要素がリストbに含まれない
if a not in b:
    print('please dog!!!!')
else:
    print('already ok')
#aという要素がリストbに含まれる
if a in b:
     print('dog')
else:
     print('miss dog')

# for分ついでにfizzbuzz
for i in range(1,30):
    if i % 3 == 0 and i % 5  == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)

# while文
i = 0
while i < 10:
    print(i + 1)
    i += 2