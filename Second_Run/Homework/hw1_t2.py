# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.


#Пытаюсь сделать двумерный массив, из которого порядно можно было бы брать аргументы для логической функции, как предикаты

#сначала перечисление бинарных чисел
# for i in range(8):
#     print(f'{i:3x}')
#     i = i+1

#Работает, запишем в массив
binarize = lambda i :f'{i:3b}'
predicates= [binarize(i) for i in range(8)]

#теперь разложение бинарных чисел на отдельные биты и запись в двумерный массив
def digitize(a:str)-> list:
    a= a.replace(" ","0")
    return [int(c) for c in a]

predicates=list(map(digitize, predicates))

#получили аргументы со всеми вариантами значений предикатов для 3-х битовых чисел
# print(*predicates, sep='\n')

#запишем функцию предикаты
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
def boolean_equation1(bits:list)-> bool:

    print('x , y , z   P(x,y,z)')
    counter = 0
    eq =  lambda x: ~(x[0] | x[1] | x[2]) == ~x[0] & ~x[1] & ~x[2]

    for row in bits:
        if eq(row) == True:
            counter+=1
        else : counter -=1
        print(f'{row} => {eq(row)}',end='\n')
    
    if counter == 8:
        print("Функция тождественно равна 1")
    if counter == -8:
        print("Функция тождественно равна 0")

boolean_equation1(predicates)





