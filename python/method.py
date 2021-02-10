# 様ざまなメソッド

# format
# {}の中にformat()の引数が入る
n = 5
word = '数字は{}'.format(n)
print(word)
m = 9
a =  '数字は{}と{}'.format(n,m)
print(a)

# upper,lower
# upper 大文字、lower 小文字
s = 'AAAaaaa'
print(s.upper())
print(s.lower())

# strip
# 空白を消す
w = '     aaaaaaa      '
print(w.strip()) #全空白を消す
print(w.lstrip()) #左空白を消す
print(w.rstrip()) #右空白を消す

#zfill
# zfill()の引数に桁数を指定。（文字列）
print('5'.zfill(4))
print('15'.zfill(4))
print('115'.zfill(4))

# replace
# 指定文字の置き換え
print('hello world'.replace('e','u'))
print('hello world'.replace('l',''))