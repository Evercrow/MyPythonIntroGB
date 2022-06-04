# 4. Задайте два целых числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
#НОД(1071,462) = 21

#Используем алгоритм Евклида для нахождения НОД, чтобы от него найти НОК.
#nod = nod//r * r + nod%r

def FindNOD(a:int,b:int):
    if a < b : 
        b = a + b
        a = b - a
        b = b - a
    r = b
    nod = a
    while nod%r !=0:
        q = nod//r
        r = nod%r           
        nod = (nod - r)//(q)
    return r 

def FindNOK(a:int,b:int):
    return a*b//(FindNOD(a,b))

num_a = int(input("Введите первое число: "))
num_b = int(input("Введите второе число: "))
print(FindNOK(num_b,num_a))           
         