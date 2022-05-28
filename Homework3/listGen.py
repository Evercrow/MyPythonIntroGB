import random
def CreateIntNumList(elem_count ,upper_r,lower_r = 0):
    num_list =[]
    for i in range(elem_count):
        num_list.append(random.randint(lower_r,upper_r))
    return num_list

def CreateShortFloatList(elem_count ,upper_r,lower_r = 0):
    num_list =[]
    for i in range(elem_count):
        num_list.append(round(random.uniform(lower_r,upper_r),2))
    return num_list

