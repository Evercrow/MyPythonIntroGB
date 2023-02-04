#Создайте программу для игры с конфетами человек против человека.

#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#a) Добавьте игру против бота

#b) Подумайте как наделить бота ""интеллектом""

def SweetsGame(all_sweets=100):
    while True:
        ask_player = input("Вы играете с ботом? (y -да, n - нет)")
        if ask_player == 'y': 
            bot = True
            break
        elif ask_player == 'n':
            bot = False
            break
        else :
            print("Вы не выбрали режим игры")
    user = False
    print(f'\nВсего {all_sweets} конфет , проигрывает тот, кто взял последнюю конфету(ы) \n')
    while all_sweets > 0:
        # if bot == True: bot(all_sweets)
            
        user_request = int(
            input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
        while user_request > (28 and all_sweets) or user_request < 1:
            print(f'Игрок {int(user)+1} повторите ввод!')
            user_request = int(
                input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
        all_sweets -= user_request
        print(f'осталось {all_sweets}')
        if all_sweets == 0:
            return input(f'Игрок {int(user)+1} проиграл!')
        if  bot == False:  user = not(user)
        else : 
            bot_move = BotMove(all_sweets)
            print(f"Бот забирает {bot_move}") 
            all_sweets -= bot_move
            print(f'осталось {all_sweets}')
            if all_sweets == 0: return print(f'Бот проиграл!')
        


def BotMove(f):
    if f < 29: return f - 1
    elif f ==1: return f
    else: return (f % 29) + 1
    



SweetsGame()