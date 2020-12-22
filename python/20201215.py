# 10進数＜ー＞２、８、１６進数変換

# 10進数→２進数
n = 20
# 20/2=10…0
# 10/2=5…0
# 5/2=2…1
# 2/2=1…0
# 1/2=0…1
# 10100
result = ''
while n >0:
    result = str(n % 2) + result
    n //= 2
print(result)

n = 15
# my_answer = 1111
result2 = ''
while n > 0:
    result2 = str(n % 2) + result2
    n //= 2
print(result2)

# 2,8,16進数
n = 14
def shinsu(n, base):
    result3 = ''
    while n > 0:
        result3 = str(n % base) + result3
        n //= base
    return result3
print(shinsu(n, 2))
print(shinsu(n, 8))
print(shinsu(n, 16))

n = 19
def shinsu2(n, num):
    result4 =''

    while n>0:
        result4 = str(n % num) + result4
        n //= num

    return result4
print(shinsu2(n, 2))
print(shinsu2(n, 8))
print(shinsu2(n, 16))

# ２進数→１０進数
n = '10011'
result = 0
for i in range(len(n)):
    result += int(n[i]) * (2 ** (len(n) - i -1))
print(result)
print(i)
print(len(n))
# i      = 01234
# len(n) = 5
# 1*(2 ** (5-0-1))=16
# 0*(2 ** (5-1-1))=0
# 0*(2 ** (5-2-1))=0
# 1*(2 ** (5-3-1))=2
# 1*(2 ** (5-4-1))=1
# 19
n2 = '1111'
result2 = 0
for i in range(len(n2)):
    result2 += int(n2[i]) * (2 ** (len(n2)- i - 1))
print(result2)
# 8進数
n3 = '27'
result3 = 0
for i in range(len(n3)):
    result3 += int(n3[i]) * (8 ** (len(n3)- i - 1))
print(result3)

# bin/int
# 0b 2
# 0o 8
# 0x 16
a=23
print(bin(a))
b='27'
print(int(b,8))
c = 0x1D
print(c)
d=0o7
print(d)