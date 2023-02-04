# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#напишем функцию
def OddIndexSum(list):
    sum = 0
    print(f"Sum of elements with odd position with FOR loop is",end=' ')
    for i in range(len(list)):
        if i%2 != 0:
            sum += list[i]
    return sum


#with slices
def SliceSum(l):
    print('with slices:',end=' ')
    return sum(l[1::2])

init_list = [2, 3, 5, 9, 3]
print(init_list)
print(OddIndexSum(init_list))
print(SliceSum(init_list))
print()
#Попробуем со своим списком
import main as lg
my_list = lg.CreateIntNumList(8,10)
print(my_list)

print(OddIndexSum(my_list))
print(SliceSum(my_list))
