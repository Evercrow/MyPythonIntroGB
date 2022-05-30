
# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
    
#     *Пример:*
    
#     - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def FloatPartDiff(list):
    def floatpart(list):
        return list[i] - list[i]//1
    min = list[0] - list[0]//1
    max = 0  
    for i in range(len(list)):
        if floatpart(list) > max and type(list) != "<class 'int'>": #отбрасываем целые, как в примере
            max = floatpart(list)
        if floatpart(list) < min and type(list) != "<class 'int'>": #floatpart(list) != 0:
            min = floatpart(list)
    return max-min 


init_list = [1.1, 1.2, 3.1, 5, 10.01] # из примера
print(init_list, end=' => ')
print(FloatPartDiff(init_list)//0.01/100)


#Попробуем со своим списком
from listGen import CreateShortFloatList

my_list = CreateShortFloatList(5,10)
my_list = [7.83, 0.07, 5.06, 1.28, 0.63]
print(my_list, end=' => ')
print('%.2f'%FloatPartDiff(my_list))


# #Возникала проблема с неточностью  числа, если округлять
# #с помощью math. или просто через математические операторы, как я делаю в print 
# a = 0.56-0.08
# print(a)
# print(a//0.01*0.01)

# #вот пример, когда запись с умножением не работает, а с делением нормально 
# b = 0.91 - 0.08
# print(b)
# print(b//0.01*0.01)
# print(b//0.01/100)

#Вопрос к вам - какие надежные методы используют, чтобы обрезать число до нужного знака,
#и при этом не получить неточности из-за бинарного математического представления float в питоне?
#trunc не подходит, он дает целое.


