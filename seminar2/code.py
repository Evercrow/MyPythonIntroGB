









# 7. Программа "Калькулятор кредитов" Рассчитайте месячные выплаты 
# (m) и суммарную выплату (s) по кредиту. 
# О кредите известно, что он составляет n рублей, берется на y лет, под p процентов.
# Месячные выплаты находятся по формуле:
# m = (n * p * (1 + p)y) / (12 * ((1 + p)y – 1)), где p выражается в долях единицы, 
# а не процентах.
# Суммарная выплата представляет собой выплаты за все месяцы каждого года:
# s = (m * 12) * y
# Запросите размер кредита в рублях и копейках, количество целых лет (в годах) 
# и процентную ставку в процентах с точностью до сотых. 
# Распечатайте месячные выплаты и сумму кредита в рублях и копейках.

# *Пример:*

# - Введите сумму кредита (рубли и копейки): 543.25
# - Введите срок кредита в годах (целое число): 2
# - Введите процентную ставку в процентах с точностью до сотых (без знака "%"): 7.45
# Месячные выплаты составят 25.2 руб.
# Суммарная выплата равна 604.68 руб.

# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# Пример:

# Для N = 5: 1, -3, 9, -27, 81

# N = int(input("How many elements needs to be shown? \n"))

# for i in range(N):
#     print(f'{(-3)**i}',end=',')


# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - 
# определять количество вхождений подстроки в строку.

#  *Пример:*

#  "Проснувшись однажды утром после беспокойного сна."

#  "Проснувшись однажды утром"

#  Количество вхождений - 1

# text_init = "Проснувшись однажды утром после беспокойного сна."
# text_to_find = "Проснувшись однажды утром" 
# print(text_init.count(text_to_find) )  


# 5. Пишем "компьютерный вирус". Запросите у пользователя любой текст. 
# Сохраните вторую с начала и третью с конца буквы в отдельные переменные 
# (например a и b). Замените во всём тексте букву из переменной a, на 
# букву из переменной b и выведите зашифрованный текст на экран. 
# Пример до шифровки: "Однажды, в студеную зимнюю пору, я из лесу вышел; 
# был сильный мороз". Пример после шифровки: "Орнажры, в стуреную зимнюю пору, 
# я из лесу вышел; был сильный мороз".

# str = "Однажды, в студеную зимнюю пору, я из лесу вышел;был сильный мороз" 
# a = str[1]
# b = str[-3]
# print(str.replace(a,b))

# 4. На столе стоит две корзины с яблоками. Корзина a и корзина b. 
# Введите количество яблок с клавиатуры. Затем поменяйте содержимое корзин местами 
# и выведите результат.

# Например, если пользователь ввёл 5 и 7, то до обмена a=5, b=7, а после a=7 и b=5.

# a = int(input("Сколько яблок в первой корзине? \n"))
# b = int(input("Сколько яблок в второй корзине? \n"))

# a,b = b,a
# print(f"Опа! Теперь в первой корзине {a} , а во второй {b} яблок")



# 2. Задайте список из целых и вещественных чисел. Отсортируйте его по возрастанию, 
# от меньшего к большему и выведите в консоль. 
# Зеркально разверните его и выведите на строке ниже.
#  *Пример:*
# список -> [1,0.5,15,3.4]
# Сортировка - > [0.5,1,3.4,15] 
# Разворот - > [15,3.4,1,0.5]

# spisok = [1,0.5,15,3.4]
# spisok.sort()
# print(spisok)
# # print(spisok[::-1])
# spisok.sort(False)
# print(spisok)


# 6. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 
# 5 и 10 или 15, но не 30.

num = int(input("Введите проверяемое число"))

if (num%10 ==0 or num%15 ==0) and num%30 !=0 :
    print()
