# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

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

fact_num = int(input("Введите число для факториала: \n"))    
ShowFactorial(fact_num)