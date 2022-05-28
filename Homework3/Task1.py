# ## Домашняя работа после Семинара 3
# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
    
#     *Пример:*
    
#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


#напишем функцию
def OddIndexSum(list):
    sum = 0
    for i in range(len(list)):
        if i%2 != 0:
            sum += list[i]
    return sum


init_list = [2, 3, 5, 9, 3]
print(init_list)
print(f"Sum of elements with odd position is {OddIndexSum(init_list)}")

#Попробуем со своим списком
import listGen as lg
my_list = lg.CreateIntNumList(8,10)
print(my_list)

print(f"Sum of elements with odd position is {OddIndexSum(my_list)}")
