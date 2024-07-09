print('Введите 3 числа:')
number_1 = int(input('first: '))
number_2 = int(input('second:'))
number_3 = int(input('third: '))

if number_1 == number_2 == number_3:
    print('3')
elif number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
    print('2')
elif number_1 != number_2 != number_3:
    print('0')