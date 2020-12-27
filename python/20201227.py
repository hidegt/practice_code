def drink(n):
    left_drink = 0
    while n >=3:
        n -= 2
        left_drink += 3
    left_drink += n
    return left_drink
n = input('ドリンクリサイクルキャンペーンです。３本交換で１本好きなジュースをプレゼント。何本交換しますか？：')
print(drink(int(n)))

#3本で１本追加
#3本。。。4本になる
#11本。。。16本になる
