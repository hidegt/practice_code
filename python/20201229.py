data = [4,19,2,3]
min = 0
for i in range(1, len(data)):
    if data[i] < data[min]:
        min = i
print(min)
# min = 0(4)
# i = 1(19)   19<4  x
# i = 2(2)   2<4  o
# min = 2(2)
# i = 3(3)   3<4  x
# min = 2

for i in range(len(data)):
    min = i
    for j in range(i + 1, len(data)):
        if data[min] > data[j]:
            min = j
    data[i],data[min] = data[min], data[i]
print(data)

# (min)i = 0(4)
# j = 1(19)
# 4>19 x
# j=2(2)
# 4>2 o
# min = 2
# j=3(3)
# 2>3 x
# data[i],data[min] = 2,4
# [2,?,?,?]
# min = 1(4)
# j=2(19)
# 4>19 x
# j=3(3)
# 4>3 o
# data[i],data[min] = 3,4
# [2,3,?,?]
# min = 2(4)
# j=3(19)
# 4>19 x
# [2,3,4,?]
# min = 3(19)
# j=3(19)
# 19>19 x
# [2,3,4,19]

for i in range(1, len(data)):
    skip = data[i]
    j = i-1
    while(j >= 0) and (data[j] > skip):
        data[j +1] =data[j]
        j -= 1
    data[j +1] = skip
print(data)

# i = 1, skip=19
# j = 0
# j>=0 & 4>19  X
# j[4,19,?,?]
# i = 2, skip=2
# j = 1
# j >=0 & 19 >2 o
# data[1+1] = data[1]   copy
# j[4,19,19,?]
# j -=1  j =0
# 4>2 o
# data[0+1] = data[0]   copy
# j[4,4,19,?]
# j -=1 j =-1 leave while
# data[-1 + 1](0) = skip(2)
# j[2,4,19,?]
# ....
j[2,3,4,19]