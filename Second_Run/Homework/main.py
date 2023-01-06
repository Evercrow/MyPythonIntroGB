def CreateNewHW(hw_num,tasks_num):
    spec_path = "/Second_Run/Homework/"
    for i in range(1,int(tasks_num)+1):
        open(spec_path+'hw'+hw_num+'_t'+str(i)+'.py','x')

if __name__ == "__main__":
    n1 = (input("Введите номер семинара: "))
    n2 = (input("Введите общее число задач: "))
    CreateNewHW(n1,n2)



import random
def CreateIntNumList(elem_count ,upper_r,lower_r = 0):
    """
    эта функция генерирует список размера elem_count с рандомными целыми числами в диапазоне (lower_r=0,upper_r)
    """
    num_list =[]
    for i in range(elem_count):
        num_list.append(random.randint(lower_r,upper_r))
    return num_list

def CreateShortFloatList(elem_count ,upper_r,lower_r = 0):
    """
    эта функция генерирует список размера elem_count с рандомными вещественными числами в диапазоне (lower_r=0,upper_r),
    с округлением до 2-го знака после запятой
    """
    num_list =[]
    for i in range(elem_count):
        num_list.append(round(random.uniform(lower_r,upper_r),2))
    return num_list