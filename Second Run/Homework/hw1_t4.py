# 4. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
    
#     *Пример:*
    
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21

A_X = int(input("Enter X coordinate of point A: "))
A_Y = int(input("Enter Y coordinate of point A: "))
B_X = int(input("Enter X coordinate of point B: "))
B_Y = int(input("Enter Y coordinate of point B: "))

from math import sqrt
AB_segment = sqrt((A_X-B_X)**2+(A_Y-B_Y)**2)
print('A ({},{}); B ({},{}) -> {:.2f}'.format(A_X,A_Y,B_X,B_Y,AB_segment)) #форматирование использует round(), похоже, так что 5.099 ->5.10
