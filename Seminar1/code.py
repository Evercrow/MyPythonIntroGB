# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
    
#     *Примеры:* 
    
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

# first_num = int(input('Enter first number: '))
# sec_num = int(input('Enter second number: '))

# if first_num/sec_num == sec_num :
#     print('first number is the second squared')
# elif sec_num/first_num == first_num :
#     print('second number is the first squared')
# else : print('none of them is square of another')   

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# max = int(input("Enter first number:"))
# for i in range(4):
#     a = int(input("Enter next number: "))
#     if a> max:
#         max = a
# print(f"Max number is  {max}")

# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# N = int(input('Enter N: \n'))
# for i in range(-N,N):
#     print(i,end= ",") #string separator variable
# print(N)    


# a = float(input())
# a= (a*10) % 10
# print(a)


# 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# a = input("Enter checked number: ")
# if (a%30 != 0): print('This number is not ')

# X = bool(input())
# Y = bool(input())
# if (not (X or Y) ) == (not(X and Y)):
#     print("True")
# else:
#     print("false")    
import math

a = 9
b = 3
print(math.sqrt(a))
