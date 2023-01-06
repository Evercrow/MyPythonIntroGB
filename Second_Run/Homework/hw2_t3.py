
# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

def ShowSequence(n):
    seq_l = []
    for i in range(1,n+1):
        seq_l.append((1+1/i)**i)
    print(seq_l)
    print(f"Сумма членов равна {sum(seq_l):.2f}")

ShowSequence(3)
