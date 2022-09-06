def task1():
    # Дано натуральное число.
    # Напишите программу, которая определяет, является ли
    # последовательность его цифр при просмотре
    # справа налево упорядоченной по убыванию
    flag = 1
    number = input("Введите натуральное число: ")
    for i in range(len(number) - 1, 0, -1):
        if number[i] <= number[i - 1]:
            flag = 0
            break
    if flag == 0:
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
        if input_string[i] in english_vowels or input_string[i] in russian_vowels:
            count_vowel_letter += 1
    if input_string[len(input_string) - 1] in english_vowels or input_string[len(input_string) - 1] in russian_vowels:
        count_vowel_letter += 1
    print("Итого:\n Пар нижнего регистра: ", count_lower, "\n Пар верхнего регистра: ", count_upper,
          "\n Гласных букв: ", count_vowel_letter)


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
    print("Сумма чисел больше нуля: ", summary)
    if is_zero_exists == 0:
        print("Сумму посчитать нельзя, нет ни одного нуля")
    else:
        print("Сумма чисел после нуля: ", summary_after_zero)
    print("Теперь список выглядит так: ", input_list)


def task4():
    # Дана строка в виде случайной последовательности чисел от 0 до 9.
    # Требуется создать словарь, который в качестве ключей будет
    # принимать данные числа (т. е. ключи будут типом int), а в качестве
    # значений – количество этих чисел в имеющейся последовательности
    input_list = list(input("Введите строку: "))
    for i in range(len(input_list)):
        input_list[i] = int(input_list[i])
    length = len(input_list)
    dictionary = dict.fromkeys(input_list, length)
    print("Словарь: ", dictionary)


def description(*dictionary):
    #for i in dictionary:
    #print("Название: ", dictionary[0], "Описание: ")
    #print(dictionary)
    return

def pricelist():
    return

def quantity():
    return

def allInfo():
    return

def purchase():
    return

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
    cake = ['сахар, соль, маргарин', 2.6, 500]
    brownie = ['сахар, соль, яйцо', 1.5, 80]
    confectionery_menu = {'торт': cake, 'пирожное': brownie}
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
                    #print(confectionery_menu.keys())
                case 2:
                    pricelist()
                case 3:
                    quantity()
                case 4:
                    allInfo()
                case 5:
                    purchase()
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
    for i in range(len(input_tuple)):
        if input_tuple[i] > 0:
            counter += 1
    print("Количество положительных элементов: ", counter)


def menu():
    while True:
        print("Список заданий:\n 1. Определение убывания/возрастания\n "
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
