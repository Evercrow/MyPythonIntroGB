# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def ShowFullFibo(last):
    if last == 1: return [1,0,1]
    if last == 0: return []
    fib_list =[1,1]
    for n in range(2,last):
        fib_list.append(fib_list[n-1]+fib_list[n-2])
    #получили числа Фибонначи для натуральных k, теперь сделаем "левый" хвост последовательности для отрицательного k
    nega_fib_list = [num if i%2 ==0 else -num for i,num in enumerate(fib_list)  ]

    #склеиваем списки в одну последовательность, не забываем про 0
    nega_fib_list.reverse()
    nega_fib_list.append(0)
    return nega_fib_list + fib_list

#через рекурсию
def fullFibonacci(n):
    fibonacci = [0]
    if n == 0:
        return fibonacci
    elif n == 1:
        fibonacci.insert(0,1)
        fibonacci.append(1)
    elif n > 1:
        fibonacci = fullFibonacci(n - 1)
        fibonacci.append(fullFibonacci(n - 1)[-1] + fullFibonacci(n - 2)[-1])
        fibonacci.insert(0, fibonacci[-1] * ((-1) ** (n + 1)))
    return fibonacci


k = int(input("Введите номер искомого числа Фибонначи: "))
print(ShowFullFibo(k))
print(fullFibonacci(k))