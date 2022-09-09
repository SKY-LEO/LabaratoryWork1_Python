def task1():
    # Дано натуральное число.
    # Напишите программу, которая определяет, является ли
    # последовательность его цифр при просмотре
    # справа налево упорядоченной по убыванию
    flag = True
    number = input("Введите натуральное число: ")
    if number.isdigit() is False:
        print("Строка состоит не из цифр!")
        return
    for i in range(len(number) - 1, 0, -1):
        if number[i] <= number[i - 1]:
            flag = False
            break
    if flag is False:
        print("Не убывает")
    else:
        print("Убывает")


def task2():
    # Посчитать, сколько пар (стоят рядом) верхнего и нижнего
    # регистра находится в веденном с клавиатуры слове. (Пример HjkLM- 1
    # пара нижнего, 1 пара верхнего), а также сколько гласных букв в слове.
    count_lower = count_upper = count_vowel_letter = 0
    english_vowels = ('e', 'y', 'u', 'i', 'o', 'a')
    russian_vowels = ('у', 'е', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё', 'ы')
    input_string = input("Введите строку: ")
    for i in range(len(input_string) - 1):
        if input_string[i].islower() and input_string[i + 1].islower():
            count_lower += 1
        elif input_string[i].isupper() and input_string[i + 1].isupper():
            count_upper += 1
        if input_string[i].lower() in english_vowels or input_string[i].lower() in russian_vowels:
            count_vowel_letter += 1
    if input_string[len(input_string) - 1].lower() in english_vowels \
            or input_string[len(input_string) - 1].lower() in russian_vowels:
        count_vowel_letter += 1
    print("Итого:\n Пар нижнего регистра:", count_lower, "\n Пар верхнего регистра:", count_upper,
          "\n Гласных букв:", count_vowel_letter)


def task3():
    # Найдите сумму положительных элементов списка.
    # Найдите сумму элементов списка после первого нуля.
    # Если нулевых элементов нет в списке, то выведите «Сумму посчитать нельзя».
    # Удалить из списка все отрицательные элементы
    summary = summary_after_zero = 0
    is_zero_exists = 0
    input_list = []
    count = int(input("Сколько чисел Вы хотите добавить? "))
    for i in range(count):
        input_list.append(int(input("Введите число: ")))
    i = 0
    while i < len(input_list):
        if is_zero_exists == 1:
            summary_after_zero += input_list[i]
        if int(input_list[i]) > 0:
            summary += input_list[i]
        elif int(input_list[i]) == 0 and is_zero_exists == 0:
            is_zero_exists = 1
        else:
            input_list.pop(i)
            continue
        i += 1
    print("Сумма чисел больше нуля:", summary)
    if is_zero_exists == 0:
        print("Сумму посчитать нельзя, нет ни одного нуля")
    else:
        print("Сумма чисел после нуля:", summary_after_zero)
    print("Теперь список выглядит так:", input_list)


def task4():
    # Дана строка в виде случайной последовательности чисел от 0 до 9.
    # Требуется создать словарь, который в качестве ключей будет
    # принимать данные числа (т. е. ключи будут типом int), а в качестве
    # значений – количество этих чисел в имеющейся последовательности
    input_list = input("Введите строку: ")
    if input_list.isdigit() is False:
        print("Строка состоит не из цифр!")
        return
    input_list = [int(n) for n in input_list]
    dictionary = dict.fromkeys(input_list)
    for key_name, val in dictionary.items():
        counter = 0
        for k in input_list:
            if k == key_name:
                counter += 1
        dictionary[key_name] = counter
    print("Словарь: ", dictionary)


def description(dictionary):
    for key_name, val in dictionary.items():
        print(key_name, "->", "".join(val[0]))


def price_list(dictionary):
    for key_name, val in dictionary.items():
        print(key_name, "->", val[1], "руб.")


def quantity(dictionary):
    for key_name, val in dictionary.items():
        print(key_name, "->", val[2], "грамм")


def all_info(dictionary):
    for key_name, val in dictionary.items():
        print(key_name, " -> ", "".join(val[0]), ", ", val[1], " руб., ", val[2], " грамм", sep='')


def purchase(dictionary):
    product = input("Введите название продукции: ")
    var = dictionary.get(product)
    if var is None:
        print("Нет такого наименования!")
        return
    amount = int(input("Введите количество в граммах: "))
    if amount <= 0:
        print("Отрицательное количество!")
        return
    if amount > var[2]:
        print("Нет в наличии столько продукции!\nЕсть только", var[2], "грамм!")
        return
    summary = var[1] * amount / 100
    var[2] -= amount
    print("Приобретено продукции на", summary, "руб.")


def task5():
    # Реализуйте программу «Кондитерская», которая будет включать
    # в себя шесть пунктов меню. У вас есть словарь, где ключ – название
    # продукции (торт, пирожное, маффин и т.д.). Значение – список,
    # который содержит состав, цену (за 100гр) и кол-во (в граммах).
    # 1. Просмотр описания: название – описание
    # 2. Просмотр цены: название – цена.
    # 3. Просмотр количества: название – количество.
    # 4. Всю информацию.
    # 5. Покупка
    # В пункте «Покупка» необходимо совершить покупку, с
    # клавиатуры вводите название продукции и его кол-во, n – выход из
    # программы. Посчитать цену выбранных товаров и сколько товаров
    # осталось в изначальном списке
    # 6. До свидания
    cake = [["сахар, соль, маргарин"], 2.6, 500]
    brownie = [["сахар, соль, яйцо"], 1.5, 80]
    confectionery_menu = {"торт": cake, "пирожное": brownie}
    while True:
        print("Выберите действие:\n 1. Просмотр описания: название - описание\n "
              "2. Просмотр цены: название – цена\n "
              "3. Просмотр количества: название – количество\n 4. Просмотр всей информации\n 5. Покупка\n "
              "0. Выход из кондитерской")
        variant = int(input("Выберите задание: "))
        if variant > 5 or variant < 0:
            print("Ошибка, введите число в заданном интервале!")
        else:
            match variant:
                case 1:
                    description(confectionery_menu)
                case 2:
                    price_list(confectionery_menu)
                case 3:
                    quantity(confectionery_menu)
                case 4:
                    all_info(confectionery_menu)
                case 5:
                    purchase(confectionery_menu)
                case 0:
                    print("До свидания!")
                    break
                case _:
                    print("Ошибка!")
                    return -1


def task6():
    # Дан кортеж чисел. Определить количество положительных элементов
    counter = 0
    input_list = []
    count = int(input("Сколько чисел Вы хотите добавить? "))
    for i in range(count):
        input_list.append(int(input("Введите число: ")))
    input_tuple = tuple(input_list)
    for element in input_tuple:
        if element > 0:
            counter += 1
    print("Количество положительных элементов: ", counter)


def menu():
    while True:
        print("Список заданий:\n 1. Определение убывания\n "
              "2. Определение количества пар букв верхнего и нижнего регистра\n "
              "3. Найти сумму положительных элементов списка\n 4. Создать словарь\n 5. Кондитерская\n "
              "6. Кортеж чисел\n 0. Выход")
        variant = int(input("Выберите задание: "))
        if variant > 6 or variant < 0:
            print("Ошибка, введите число в заданном интервале!")
        else:
            match variant:
                case 1:
                    task1()
                case 2:
                    task2()
                case 3:
                    task3()
                case 4:
                    task4()
                case 5:
                    task5()
                case 6:
                    task6()
                case 0:
                    break
                case _:
                    print("Ошибка!")
                    return -1
    return 0


menu()
