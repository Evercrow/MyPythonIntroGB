
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].

def Task4(n:int,pos:list)->int:
    from random import randrange
    #использую list comprehension для создания списка
    seq = [randrange(-n,n+1) for _ in range(n)]
    print(seq)
    multi = 1
    for item in pos:
        multi *= seq[item]
    # from math import prod
    # print(f"произведение всех элементов равно {prod(seq)}")
    print(f"произведение указанных элементов равно {multi}")

lst1=[3,1]
lst2 = [0,-1]
num = int(input("Введите число N для границ списка(по стандартному списку позиций, берите >=4):"))
Task4(num , lst1)
Task4(num , lst1)
