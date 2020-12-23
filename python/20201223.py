#九九
n = 10
m = 10
for i in range(1,n):
    for j in range(1,m):
        print(str(i) + 'x' + str(j) + '=' + str(i*j), end=', ' )

#線形探索
def line(data,value):
    for i in range(len(data)):
        if data[i] == value:
            return i
    return -1
data = [20,30,50,60,10]
print(line(data, 10))
print(line(data, 11))

#２分探索
def half(data,value):
  #leftとrightの範囲を設定(配列indexは0start)
  left = 0
  right = len(data) -1
  while left <= right:
      # 範囲の中央値を計算
      center = (left + right) // 2
      #範囲の中央値と比較
      if data[center] == value:
          return center
      #値の方が大きい場合
      elif data[center] < value:
          left = center +1
      #値の方が小さい場合
      else:
          right = center -1
  return -1
data = [11,22,33,44,55,66]
print(half(data,33))

#木構造探索
#幅優先
tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[],[],[],[],[],[]]
#index   0     1      2    3     4     5  6   7  8  9 10
data = [0]
while len(data) > 0:
    post = data.pop(0)
    print(post, end=',')
    for i in tree[post]:
        data.append(i)
# data[0] ...12, [1]... 34, [2]... 56, [3]...78,[4]...910
#深さ優先
#行きがけ
def search(post):
    print(post, end=',')
    for i in tree[post]:
        search(i)
search(0)
#通りがけ
while len(data) > 0:
    post = data.pop()
    print(post, end=',')
    for i in tree[post]:
        data.append(i)
# indexの0を参照tree[1,2]の2を出力、その２から[5,6]を参照、６を出力
# ６がないので5を出力
# ５もないので1を出力…を繰り返す