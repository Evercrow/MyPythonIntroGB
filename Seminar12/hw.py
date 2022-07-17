prices2=[(23, 5915450),
(29, 14811710),
(31, 19295720),
(37, 38947650),
(41, 5856458),
(43, 7077323)]

prices1=[(23, 5915450),
(29, 14811710),
(31, 19295720),
(37, 38947650)]
from sem_code import find_progression_f
from sympy import *
y = find_progression_f(prices1)
print("Функция линейного приближения для датасета 4-х точек:\n")
print(y)
x = Symbol("x")
# num=int(input("Введите значение первого столбца:"))
# print(y.subs(x,num))

y = find_progression_f(prices1)
print("Функция линейного приближения для датасета 6-и точек:\n")
print(y)
num=int(input("Введите значение первого столбца:"))
print(y.subs(x,num))