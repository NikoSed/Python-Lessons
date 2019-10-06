def Imtdef():
    #предупрждение
    print('вводите целые числа! ')

    #данные
    try:
        w = float(int(input('ваш вес: ')))
    except ValueError:
        print('вы ввели не число')
    try:
        h = float(int(input('ваш рост (в сантиметрах): ')))
    except ValueError:
        print('вы ввели не число')


    #результат
    imt = w / ((h / 100) * (h / 100))
    print(imt)

    #вывод
    if imt < 19:
        print('у вас недовес')
    elif imt > 25:
        print('у вас перевес')
    else:
        print('ваш вес в норме :)')
