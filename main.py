def exercise1():
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


def exercise2():
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


def exercise3():
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

def exercise4():
    # Дана строка в виде случайной последовательности чисел от 0 до 9
    # Требуется создать словарь, который в качестве ключей будет
    # принимать данные числа (т. е. ключи будут типом int), а в качестве
    # значений – количество этих чисел в имеющейся последовательности
    return 0


def exercise5():
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
    return 0


def exercise6():
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
                    exercise1()
                case 2:
                    exercise2()
                case 3:
                    exercise3()
                case 4:
                    exercise4()
                case 5:
                    exercise5()
                case 6:
                    exercise6()
                case 0:
                    break
                case _:
                    print("Ошибка!")
                    return -1
    return 0


menu()
