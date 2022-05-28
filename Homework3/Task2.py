# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Если остается 1 элемент без пары - умножаем его самого на себя.
    
#     *Пример:*
    
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

def ProductListPairs(list):
    product = []
    for i in range((len(list)+1)//2):
        product.append(list[i]*list[len(list)-1-i])
    return product


init_list = [2, 3, 4, 5, 6]
print(init_list, end=' => ')
print(ProductListPairs(init_list))

#Попробуем со своим списком, заодно осваиваю синтаксис импорта
import listGen as lg
my_list = lg.CreateIntNumList(6,10)
print(my_list, end=' => ')

print(ProductListPairs(my_list))