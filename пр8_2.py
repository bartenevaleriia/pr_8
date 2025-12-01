print('Введите 10 чисел')

num1 = int(input('Первое число: '))
num2 = int(input('Второе число: '))
num3 = int(input('Третье число: '))
num4 = int(input('Четвертое число: '))
num5 = int(input('Пятое число: '))
num6 = int(input('Шестое число: '))
num7 = int(input('Седьмое число: '))
num8 = int(input('Восьмое число: '))
num9 = int(input('Девятое число: '))
num10 = int(input('Десятое число: '))
j=0

for i in [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]:
    if i % 2 == 0:
        j=j+1
    else:
        continue

if j != 10:
    print('NO')
else:
    print('YES')



