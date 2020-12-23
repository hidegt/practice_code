# フィボナッチ数列を求める
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
      return fib(n-1)+fib(n-2)
print([fib(n) for n in range(1,10)])

# ○番目の値を求める
def fib2(m):
    if m<=2:
        return 1
    return fib2(m-2)+fib2(m-1)
print(fib2(5))

# メモ化
# memoに終了条件を代入
memo = {1:1, 2:1}
def fib_memo(n):
    # memoに値がある場合、それを返す
    if n in memo:
        return memo[n]
    # memoになければ計算して、その値をmemoに登録
    memo[n] = fib_memo(n-2)+fib_memo(n-1)
    return memo[n]
num = int(input('フィボナッチ関数で遊びましょう。数字を入力してください。：'))
print(fib_memo(num))
