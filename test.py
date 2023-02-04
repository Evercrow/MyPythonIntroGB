

# from random import randint
# from operator import length_hint 
# def create_list(n):
#     list = []
#     for i in range(0,n):
#         list.append(randint(1,11))
#     print(list)
#     return list

# def sum_odd_elem(some_list):
#     sum = 0
#     size = length_hint(some_list)
#     for i in range(0,size):
#         if i%2 != 0:
#             sum += some_list[i]
#     return sum

# len = randint(1,11)
# list = create_list(len)
# # print(type(list))
# print(f'Список чисел: {list}')
# # list = [2, 3, 5, 9, 3]

# sum = sum_odd_elem(list)
# print(f'Сумма эл-тов с нечетным индексом: {sum}')



# from random import randint
# def create_list(n):
#     list = []
#     for i in range(n):
#         list.append(randint(1,11))
#     print(list)
#     return list

# def sum_odd_elem(some_list):
#     sum = 0
#     for i in range(len(some_list)):
#         if (i//2 != 0):
#             sum = sum + some_list[i]
#     return sum

# size = randint(1,11)
# list = create_list(size)
# print(f'Список чисел: {list}')
# # list = [2, 3, 5, 9, 3]

# sum = sum_odd_elem(list)
# print(f'Сумма эл-тов с нечетным индексом: {sum}')


# 2) Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def fibonacci(n):
    
    
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return (-1)**(n+1)*((fibonacci(abs(n)-1) + fibonacci(abs(n)-2)))

# def fibonacci(n):
    
#     if n > -1:
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return fibonacci(n-1) + fibonacci(n-2)
#     if n <= -1:
#             return int((-1)**(n+1))*(fibonacci(-n))


# num = int(input("Введите число: "))
# for i in range(-num,num+1):
#     print (fibonacci(i), end=",")



# data = [5, 6, 3, 3]
# j = 0
# enc_string = ["1", "a", "b", "c"]
# i = 0
# decoded = ''
# for n in range( len(enc_string)):
#     decoded += enc_string[i]*data[j]
#     j+=1
#     i+=1
# print(decoded)

# nabor = {0 : "5 + 6 + 8",1 : "4 + 3 + 1"}

# nabor = { key: value.split(" + ") for key, value in nabor.items()}
# print(nabor)

# from pathlib import Path
# import glob
# count =len(glob.glob(".\\*otion*"))
# print(str(Path(__file__).parent.resolve())+"\\"+"notion.txt")
# print(count)
