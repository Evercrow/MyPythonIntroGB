
def player_move(field,player_mark):
    from writemove import WriteMove
    while True:
        player_choice = input(f'Введите номер ячейки, чтобы поставить {player_mark}: ')
        try:
            player_choice = int(player_choice)
        except:
            print('Нужно ввести номер цифрой!')
            continue
        if player_choice >= 1 and player_choice <= 9:
            players_move = WriteMove(player_choice, player_mark,field)
            if players_move == True:
                break   # ход сделан успешно, выхоим из функции
            else:
                print('Ячейка занята, будьте внимательней! ')
        else:
            print('У нас всего 9 ячеек, выберите одну из них')
