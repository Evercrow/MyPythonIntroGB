# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def PrimDivisors(num)->list:
    #первое простое число
    prim = 2
    all_prims = []
    # теперь просто делим на все числа меньше текущего и выделяем множители
    while prim <= num :
        if num % prim == 0:
            all_prims.append(prim)
            num = num/prim
        else :
            prim +=1
    return all_prims
    
if __name__ == 'main':
    print("Чтобы остановить программу, сделайте пустой ввод")
    while True:
        n=(input("Введите натуральное число: "))
        if n =='': break
        print(*PrimDivisors(int(n)))
