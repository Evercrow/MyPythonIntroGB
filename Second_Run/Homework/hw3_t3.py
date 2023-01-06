# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (если получаются длинные числа после запятой, это нормально и особенность данного языка программирования.
#  ваш ответ может не совпадать с примером(может получитя 0,20))

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def FloatPartDiff(li):
    
    min = 0.999 #так как все равно округляем до 2-го знака, такого "минимума" должно быть достаточно
    max = 0  
    
    for i in range(len(li)):
        floatpart = lambda x: x[i] - x[i]//1
        if floatpart(li) > max and type(li[i]) != "<class 'int'>": #отбрасываем целые, как в примере
            max = floatpart(li)
        if floatpart(li) < min and type(li[i]) != "<class 'int'>": #floatpart(li) != 0:
            min = floatpart(li)
    return max-min 

# Запуск по условиям из примера
init_list = [1.1, 1.2, 3.1, 5, 10.01] 
# init_list = [4.73, 2.53, 2.07, 4.46, 0.25]
print(init_list, end=' => ')
print(FloatPartDiff(init_list)//0.01/100)


#Попробуем со своим списком
from main import CreateShortFloatList

# my_list = CreateShortFloatList(5,10)
# print(my_list, end=' => ')
# print('%.2f'%FloatPartDiff(my_list))


