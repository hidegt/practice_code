q = []
q.append(2)
q.append(3)
q.append(5)
q.append(6)
q.append(7)
print(q)
temp = q.pop(0)   #引数を指定すると、その要素が取り出される
print(temp)
print(q)
# スタック実装（LIFO）の場合、上記のやり方で問題ないが
# temp = q.pop()で末尾の要素を取得する
# キュー実装（FIFO）の場合だと要素の移動が発生する。
# queueモジュールを使用する
