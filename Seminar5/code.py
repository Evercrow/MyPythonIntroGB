
#1.расчитать нод двух чисел(быстрый и медленный способ)
from time import time as secs
'''

a = 64
b = 24

def findNODsl(n1,n2):
    nod = min(n1,n2)
    while nod>1 :
        if n1%nod == 0 and n2%nod ==0 : return nod
        else: nod -=1
start=secs()
print(findNODsl(a,b))
print (f'time spent is {(secs()-start):10f}')

def findNODf(n1,n2):
    nod = min(n1,n2)
    top = max(n1,n2)
    while nod>1 :
        if n1%nod == 0 and n2%nod ==0 : return nod
        else: 
            top = top - top%nod
            nod =top
start=secs()
print(findNODf(a,b))
print (f'time spent is {(secs()-start):10f}')
'''
            
a=20
b=60
start=secs()


if a < b :
    a, b = b, a

while b!=0:
    a, b = b, a % b

print(a)
print (f'time spent is {(secs()-start)*10000:20f}')
a=20
b=75
start=secs()
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)
print (f'time spent is {(secs()-start)*10000:20f}')


#2.Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr". 
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.
'''
print('Искомый кусок:',end=' ')
sub_str = 'plr'
print(sub_str)
plr = lambda text : sub_str in text.lower()
print(f"'Polaroid' - > {plr('Polaroid')}")
print(f"'Polaroid' - > {plr('Plroid')}")
'''
#3.Вводится список в виде вещественных чисел в одну строку через пробел. 
# Сначала нужно сформировать список из введенной строки. Затем, все отрицательные значения в этом списке заменить на -1.0. Результат вывести на экран в виде строки чисел через пробел. Программу следует реализовать с использованием функции enumerate.
'''
r_list = list(map(float, input("Введите вещественные числа через пробел: ").split(' ')))
result = ''
for i,num in enumerate(r_list):
    if num < 0:
        num=-1.0
    result +=str(num)+' '
print(r_list)
print(result)
'''


#4.Саша и Галя коллекционируют монетки. Каждый из них решил записать номиналы монеток из своей коллекции. Получилось два списка. 
# Эти списки поступают на вход программы в виде двух строк из целых чисел, записанных через пробел. 
# Необходимо выделить значения, присутствующие в обоих списках и оставить среди них только четные. 
# Результат вывести на экран в виде строки полученных чисел в порядке их возрастания через пробел.

#При реализации программы используйте функцию filter и кое-что еще (для упрощения программы), подумайте что.

sasha = '0.5 1 2 4 5 15 20 50'
galya = '0.1 1 2 4 5 10'

def findBothOdds(col1:str,col2:str)-> list :
    col1 = list(filter(lambda a: float(a)%2 ==0, col1.split()))
    col2 = list(filter(lambda a: float(a)%2 ==0, col2.split()))
    res =[i for i in col1 if i in set(col2)]
    
    return res
print(*findBothOdds(sasha,galya))


# def CheckTrueness():
#     for x in range(2):
#         for y in range(2):
#             if not(not(bool(x) or bool(y)) == (not(bool(x)) and not(bool(y)))):
#                 return False
#     return True            

# print(CheckTrueness())

#Игра с конфетами
'''

def request_user(f):
    user = False
    while f > 0:
        # if user == True:
        #     bot()
        user_request = int(
            input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
        while user_request > 28:
            print(f'Игрок {int(user)+1} повторите ввод!')
            user_request = int(
                input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
        f -= user_request
        print(f'осталось {f}')
        user = not(user)
        if f == 0:
            print(f'Игрок {int(user)+1} победил!')


def bot(f):
    return (f % 29) - 1


full = 100
request_user(full)
'''

