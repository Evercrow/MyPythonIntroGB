
# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
    
#     *Пример:*
    
#     - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def FloatPartDiff(list):
    def floatpart(list):
        return round(list[i] - list[i]//1,2)
    min = round(list[0] - list[0]//1,2)
    max = 0  
    for i in range(len(list)):
        if floatpart(list) > max:
            max = floatpart(list)
        if floatpart(list) < min:
            min = floatpart(list)
    return max-min 


# init_list = [1.1, 1.2, 3.1, 5, 10.01] - из примера
# print(init_list, end=' => ')
# print(FloatPartDiff(init_list)//0.01/100)


#Попробуем со своим списком
from listGen import CreateShortFloatList

my_list = CreateShortFloatList(5,10)
print(my_list, end=' => ')
print(FloatPartDiff(my_list))


#Возникала проблема с неточностью представления float числа, если округлять
#с помощью math.floor или просто через математические операции, как я делаю в print 
a = 0.56-0.08
print(a)
print(a//0.01*0.01)

#вот пример, когда запись с умножением не работает, а с делением нормально 
b = 0.91 - 0.08
print(b)
print(b//0.01*0.01)
print(b//0.01/100)

#Вопрос к вам - какие надежные методы используют, чтобы обрезать число до нужного знака,
#и при этом не получить неточности из-за бинарного математического представления float в питоне?
#trunc не подходит, он дает целое.


