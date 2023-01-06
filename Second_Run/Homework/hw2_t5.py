# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)

def MixList(mix_list):
    print(f"Initial list is: \n {mix_list}")
    import random
    random.shuffle(mix_list)
    print(f"Now it's like this: \n {mix_list}")

user_list = ['Веселый пианист', 250, 3.14,"is", True , "Task", 3]
MixList(user_list)