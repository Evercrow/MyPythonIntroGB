
# def CheckTrueness():
#     for x in range(2):
#         for y in range(2):
#             if not(not(bool(x) or bool(y)) == (not(bool(x)) and not(bool(y)))):
#                 return False
#     return True            

# print(CheckTrueness())


def request_user(f):
    user = False
    while f > 0:
        # if user == True:
        #     bot()
        user_request = int(
            input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
        while user_request > 28:
            print(f'Игрок {int(user)+1} повторите ввод!')
            user_request = int(
                input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
        f -= user_request
        print(f'осталось {f}')
        user = not(user)
        if f == 0:
            print(f'Игрок {int(user)+1} победил!')


def bot(f):
    return (f % 29) - 1


full = 100
request_user(full)