# colors = ['red','green','blue']
# data= open('Lecture2/file.txt', 'w') #a - add, добавляет без перезаписи
#                             #w - write  - перезапись.
#                             #r - read , чтение
# data.writelines(colors) #для списков, цикл записи
# data.write('This is next line\n')
# data.close()

# with open('Lecture2/file2.txt', 'w') as data2:  #форма блока кода для работы с файлом. Автоматически закрывает файл по выходу из блока.
#     data2.write('Header')
#     data2.writelines(colors)


# path = 'Lecture2/file2.txt'
# data = open(path, 'r')
# for i in data:#построчная итерация , автоматический перенос строки
#      print(i)
# data.close()     
# exit()

# 1. w+
#     - Позволяет открывать файл для записи и читать из него.
#     - Если файла не существует, он будет создан.
# 2. r+
#     - Позволяет открывать файл для чтения и дописывать в него.
#     - Если файла не существует, программа выдаст ошибку.



# def concatenatio(*params): #звездочка, когда произвольное число аргументов
#     res: str = ""
#     for item in params:
#          res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w'))  # asdw
# print(concatenatio('a', '1'))  # a1
# # print(concatenatio(1, 2, 3, 4)) # TypeError: ...



data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)

res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res) 

import pathlib

print(pathlib.Path(__file__).parent.resolve())
print(pathlib.Path().resolve())