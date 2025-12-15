import random
number = random.randint(1,10)

for tries in range(3):
    guess = int(input('Как думаете, какое число загадано? '))
    if guess == number:
        print('Угадали!')
        break
    else:
        print('Неверно')
        if guess < number:
            print('Больше')
        else:
            print('Меньше')

        if tries == 2:
            print (f'Загаданное число: {number}')

