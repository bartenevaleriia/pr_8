import math

n = int(input('Введите число n: '))
sum = 0
for i in range (1,n):
    if i % 2 == 1:
        sum = sum + i
    else:
        sum = sum - i

sum = sum + ((-1) ** (n+1)) * n

print(sum)
