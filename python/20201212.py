def calc(x):
    x -= 1
    return x
x = 3
calc(x)
print(calc(x))
print(x)

def calc2(a):
    a[0] -= 1
    return a
a = [4,5,6]
print(calc2(a))
print(a)

n = 10
def number():
    m = 5
    print(n)
    print(m)
    return
number()  #print(n),print(m)を呼び出し
print(n)
# print(m)  関数の中で変数を定義しているので、関数外では使用できない

y = 20
if True:
    b = 20
    print(y)
    print(b)
print(y)
print(b)

# z = 10
# def update():
#     z += 5     zは関数の外で定義されているので関数内では変更できない。読み取り専用
#     print(z)

z = 10
def num():
    z = 200   #同じzで変数定義
    print(z)
num()     #関数内の200が呼び出される
print(z)   #関数外の10が呼び出される

# 非推奨
num = 200
def reset():
    global num     #global変数を使うと関数内外で値の受け渡しができる
    num = 40
    print(num)
reset()
print(num)

def add(a,b):
    return a + b
a = 4
b = 9
print(add(a,b))
def hiku(c, d):
    return c-d
c = 7
d = 6
print(hiku(c,d))