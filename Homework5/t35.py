# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

from random import randint


def createTaskListFile(N):
    l=[randint(1,10)]
    for i in range(1,N): l.append(l[i-1]+1)
    l[randint(0,N-1)] = 0
    from pathlib import Path
    file_path = Path("Homework5/t35list.txt")
    f = open(file_path, 'w')
    for num in l:
        f.write(str(num) + ' ')
    f.close()

# createTaskListFile(20)

def FindLostElem(file_path):
    from pathlib import Path
    f = open(Path(file_path),'r')
    l = f.read().strip().split(' ')
    f.close()
    l = [int(el) for el in l]
    print(f'read list is: {l}')
    if l[0] != l[1]-1 : return l[1]-1 #проверяем частный случай первого элемента
    else:   #через list comprehension не получается, частные случаи мешают
        # return [l[i+1]-1 for i,el in enumerate(l) if el != l[i-1]+1] 
        for i in range(len(l)):
            if l[i] != l[i+1]-1 : return l[0]+i+1  #в таком формате последний элемент тоже отображается верно

print(f'lost number is {FindLostElem("Homework5/t35list.txt")}')        