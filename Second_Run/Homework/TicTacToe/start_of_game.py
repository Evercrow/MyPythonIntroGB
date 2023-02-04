

def start_of_tic_tac_toe_game():
    
    mark = input('Вы будете играть крестиками (X) или ноликами (O)? ')
    mark = mark.upper()
    
    while mark != 'X' and 'O':
            mark = input('Вы ввели не те знаки. Выберите х или о: ') 
            mark = mark.upper()
    # import random
    # mark = ['X', 'O']       # если хотим быстрее начать играть :)
    # mark = random.choice(mark)
    # print(f'Вы ввели не то, поэтому выбор сделан за вас. Вы играете за {mark}')

    bot = bool(input('Вы будете играть c ботом? (введите что-нибудь -"да",иначе ''  - "нет")'))

    return mark,bot

# print(start_of_tic_tac_toe_game())

