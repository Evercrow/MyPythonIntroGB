# ## Домашняя работа Семинара 2

# 1. Напишите программу, которая принимает на вход вещественное число и показывает 
# сумму его цифр(отсекаем минус, считаем все в плюс).
    
#     *Пример:*
    
#     - 67,82 -> 23
#     - 0,56 -> 11

def FloatToNumSum(num):
    num = abs(num)
    sum = 0
    for i in str(num):
        if i == '.' : continue
        sum +=int(i)     
    return sum




# 2. Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.
    
#     *Пример:*
    
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def ShowFactorial(N):
    print("[", end=" ")
    fact = 1
    multiplier_list=[str(fact)]

    for i in range(1,N+1):
        fact*=i 
        if i!=N:print(fact,end=', ')
        else :print(fact,end=' ')

    print("] (",end="")

    for i in range(1,N):
        multiplier_list.append(multiplier_list[i-1]+"*"+str(i+1))
    print(*multiplier_list , sep =', ', end ='')
    
    print(")")




# 3.    Реализуйте случайное перемешивания списка.

#     *Пример:*

#    Исходный вариант -> ['Веселый пианист', 250, 3.14, 'True ']
#    Результат -> [250, 3.14, 'True ', 'Веселый пианист']


def MixList(mix_list):
    print(f"Initial list is: \n {mix_list}")
    import random
    random.shuffle(mix_list)
    print(f"Now it's like this: \n {mix_list}")





# user_num = float(input('Введите ваше вещественное число, дробная часть через точку:\n'))
# print(f'Cумма цифр введенного числа равна {FloatToNumSum(user_num)}')


fact_num = int(input("Введите число для факториала: \n"))    
ShowFactorial(fact_num)

# user_list = ['Веселый пианист', 250, 3.14,"is", True , "Task", 3]
# MixList(user_list)



