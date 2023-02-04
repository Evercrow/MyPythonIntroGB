

def ConsoleTicTac():
    from start_of_game import start_of_tic_tac_toe_game as Start
    from field_print import field_drawing as FieldPrint
    from player_move import player_move as PlayerMove
    from win_check import victory as IsWin
    import bot_mod as bot
    # from writemove import WriteMove
    player_choice = Start()
    use_bot = False # - пока без бота
    if player_choice[1] == True : use_bot == True #подключаем потом модуль бота от этого флага.
    if player_choice[0] == 'X': 
        player_num = 1 #Если будем поздравлять конкретного игрока в выходе,используем эту переменную
        bot_turn = 2
    else:
        player_num = 2
        bot_turn = 1
    player_mark = "X"
    move_count = 0
    list_game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    game_end = False
    while move_count < 9 :
        if use_bot == True:
            if bot_turn == 1:
                bot.BotMove(list_game,player_mark)
                bot_turn = 2
            else :
                FieldPrint(list_game)
                PlayerMove(list_game,player_mark)
                bot_turn = 1
        else:
            FieldPrint(list_game)
            PlayerMove(list_game,player_mark)
        
        move_count +=1
        if move_count >= 5:
            game_end = IsWin(list_game)
            if game_end == True:
                FieldPrint(list_game)
                return print(f"Победили {player_mark}-ики!")
        if player_mark == 'X' : player_mark = 'O'
        else: player_mark = 'X'
        
    FieldPrint(list_game)
    return print(f"Игра закончилась, ничья!")

ConsoleTicTac()

    
