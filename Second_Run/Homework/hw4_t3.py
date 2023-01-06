# Задайте последовательность чисел.
#  Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


def ShowUniques(l):
    u_set =set()
    repeat_set = set()
    for i in l:
        # запоминаем, какие числа продублировались
        if i in u_set: repeat_set.add(i)
        # сюда попадают все первые вхождения чисел
        else: u_set.add(i)                     
        #осталось полностью убрать дубликаты из множества чисел списка:
    return sorted(list(u_set-repeat_set))

num_list = [9,10,11,1, 2, 3, 5,7, 1, 5, 3, 10]
print(f'{num_list} => {ShowUniques(num_list)}')