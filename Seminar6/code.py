# Дан список чисел. Создать список, в который попадают числа, 
# описываемые возрастающую последовательность.(усложненный вариант - содержащие максимальное
#  количество элементов.)
 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. 
# Порядок элементов менять нельзя




# numbers = [1, 5, 2, 3, 4, 6, 1, 7]
# numbers2 = [10, 5, 123, 23,1,34,65,3,6]
# numbers3 = [39, 52, 82, 86, 78, 72, 89, 28]
# from random import randint
# rand_numbers = [randint(0,100) for x in range(8) ]
# print(rand_numbers)


# def GetRisingList(list_num,first_elem ):
#     result_list=[first_elem]
#     for num in list_num:
#         if num >result_list[-1]:
#             result_list.append(num)
#     return result_list



# def FindAllRisingList(i_list):
#     possible_lists =[]
#     max_size = 0
#     for i,elem in enumerate(i_list):
#         current_elem = elem
#         for j in range(i+1, len(i_list)-max_size):
#             found_list =  GetRisingList(i_list[j:len(i_list)],current_elem)
#             if len(found_list)>max_size: 
#                 max_size = len(found_list)
#             possible_lists.append(found_list)
#         # possible_lists.append(result)   
#     return  possible_lists      

# print(FindAllRisingList(numbers3))

#30. Вычислить число  c заданной точностью d
#30*** , Подумать, что если точность вычисления до 1000 знаков после запятой
# 	Пример: при d = 0.001,  = 3.141. 10-1d10-10

import math
d = float(input("Введите точность: "))
a = int(math.log10(1/d))
pi = 0
for i in range(10000):
    pi += (-1)**i/((2*i) + 1)*4
pi = str(pi)
pi = pi[:a]
print(pi)


