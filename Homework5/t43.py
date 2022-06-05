# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

num_list = [9,10,11,1, 2, 3, 5,7, 1, 5, 3, 10]

def ShowUniques(l):
    u_set =set()
    repeat_set = set()
    for i in l:
        if i in u_set: repeat_set.add(i)
        else: u_set.add(i)                     
    return sorted(list(u_set-repeat_set))

print(f'{num_list} => {ShowUniques(num_list)}')