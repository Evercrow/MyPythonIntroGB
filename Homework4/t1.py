# 1. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    
#     *Пример:*
    
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

dec_num = int(input("Введите десятичное число: \n"))
bin_num = ''
from math import trunc
temp = dec_num          
while abs(temp/2) > 0 :
    if temp%2 == 0 : bin_num += '0'
    else : bin_num += '1'
    temp = trunc(temp/2)
bin_num =  bin_num[::-1]
if dec_num == 1: bin_num = '0'+ bin_num
elif dec_num == 0: bin_num = '00'
elif dec_num < 0: bin_num = '1,' +bin_num  #добавим обозначение отрицательного знака, при необходимости
print(bin_num)   