import random
command = input("введи команду: ")
while command != "выход":
    if command == "бот":
        print("я бедный чат бот :(  Меня создал бедный программист :(  ")
    elif command == "список команд":
        print("бот - пишет иформацию о боте")
        print("текст - напечатать текст от лица бота")
        print("калькулятор - посчитать сумму, разность, произведение или разность двух чисел")
    elif command == "текст":
        text = input("введите текст, чтобы я его напечатал")
        print(text)
    elif command == "калькулятор":
        deystvie = input("выберите действие. +. сложение. -. вычитание. *. умножение. /. деление.")
        firstnumber = input("введите первое число")
        if firstnumber.isdigit() == True:
            secondnumber = (input("введите второе число"))
            if secondnumber.isdigit() == True:
                firstnumber = int(firstnumber)
                secondnumber = int(secondnumber)
                if deystvie == "+" or deystvie == "сложение":
                    print(firstnumber + secondnumber)
                elif deystvie == "-" or deystvie == "вычитание":
                    print(firstnumber - secondnumber)
                elif deystvie == "*" or deystvie == "умножение":
                    print(firstnumber * secondnumber)
                elif deystvie == "/" or deystvie == "деление":
                    if secondnumber != 0
                        print(firstnumber / secondnumber)
                    else:
                        print("на нуль делить нельзя!")
                else:
                    print("несуществуещее действие")
            else:
                print("это не число!")
        else:
            print("это не число")
    elif command == "случайное число":
        minrand = input("минимально")
        if minrand.isdigit() == True:
            maxrand = input("максимально")
            if maxrand.isdigit() == True:
                minrand = int(minrand)
                maxrand = int(maxrand)
                if minrand < maxrand:
                    print(random.randint(minrand, maxrand))
                elif minrand > maxrand:
                    print(random.randint(maxrand, minrand))
            else:
                print("это не число!")
        else:
            print("это не число!")
    else:
        print("неизвестная команда. для списка комманд, введите список команд")
    command = input("введи команду: ")
print("конец проекта")
