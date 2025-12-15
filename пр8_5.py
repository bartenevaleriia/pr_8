n = int(input('Введите натуральное число n '))

n1 = int(input())
n2 = int(input())

if n1 > n2:
    max1, max2 = n1, n2
else:
    max1, max2 = n2, n1

for i in range(n - 2):
    n_ = int(input())
    if n_ > max1:
        max2 = max1
        max1 = n_
    elif n_ > max2:
        max2 = n_

print('Максимальное число:', max1)
print('Второе по величине:', max2)