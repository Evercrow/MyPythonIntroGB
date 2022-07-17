# Риэлтору поручено выставить объекты недвижимости площадью 65м2 и 154м2 на продажу.
# Риэлтор пришёл к аналитику за советом «какой ценник поставить?»

# Аналитик занялся изучением вопроса и выяснил, что в этом районе
# объект 31м2 стоит $19310
# объект 51м2 стоит $52150
# объект 61м2 стоит $74570

from sympy import *

# Cтепень выводимого линейного полинома = количество точек -1
# f(x) = a2*x^2+a1*x+a0
# a2,a1,a0,x = symbols('a2,a1,a0,x')

# y1 = a2*31**2 + a1*31+a0 -19310
# y2 = a2*51**2 + a1*51+a0 -52150
# y3 = a2*61**2 + a1*61+a0 -74570

# result = nonlinsolve([y1,y2,y3],[a0,a1,a2])
# print(result)
# f=20*x**2+2*x+28

# print(f.subs(x,78))
# print(f.subs(x,61))

# НО желающие могут попробовать найти функцию для набора данных

# (23, 5915450),
# (29, 14811710),
# (31, 19295720),
# (37, 38947650)
# что если к первому набору добавить данные

#  (41, 5856458),
#  (43, 7077323)

def find_progression_f(data_s):
    from sympy import Symbol,symbols,nonlinsolve
    # создадим список коэфициентов от a0 до an, где n -количество точек датасэта
    coef=[]
    for i in range(len(data_s)):
        coef.append(f'a{i}')
    coef=list(map(symbols,coef))
    # print(coef)
    # запишем выражение многочлена символьно, по наибольшей степени
    eq=0
    x = Symbol("x")
    for i in range(len(coef)):
        eq+=coef[i]*(x**i)
    # print(eq)
    # подставим данные из датасэта,чтобы получить список линейных уравнений
    equations =[]
    for item in data_s:
        equations.append(eq.subs(x,item[0])-item[1])
    # print(equations)
    num_coef=tuple(nonlinsolve(equations,coef))
    # print(num_coef[0])
    # print(coef)
    replacements =list(zip(coef,num_coef[0]))
    # print(replacements)
    res_eq=eq.subs(replacements)
    return res_eq



prices3 = [(33, 21874),
(44, 38836),
(55, 60638),
(77, 118762),
(88, 155084),
]

# y = find_progression_f(prices3)
# print("Функция линейного приближения:\n")
# print(y)
