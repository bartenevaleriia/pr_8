m = int(input('Стартовое число организмов: '))
p = int(input('Среднесуточное увеличение в процентах: '))
n = int(input('оличество дней для размножения: '))

for i in range (1, n+1):
    if i == 1:
        print (i, m)
    else:
        m = m * (1 + p / 100)
        print (f'{i} {m:.0f}')