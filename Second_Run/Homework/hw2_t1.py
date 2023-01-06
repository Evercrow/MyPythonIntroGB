# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

#через свойства строки
def FloatToNumSum(num :float)->int:
    num = abs(num)
    sum = 0
    for i in str(num):
        if i == '.' : continue
        sum +=int(i)     
    return sum

#и еще методом с консоли
def ConsoleToNumSum():
    from decimal import Decimal
    print("Чтобы выйти из программы, оставьте ввод пустым \n")
    while True:
        n = input("Введите вещественное число: \n")
        if n == '': break
        n= Decimal(n.replace(',','.'))
        print(sum(n.as_tuple().digits))
    

print(f"Input {6782} -> output {FloatToNumSum(6782)}")
print(f"Input {0.56} -> output {FloatToNumSum(0.56)}")
ConsoleToNumSum()