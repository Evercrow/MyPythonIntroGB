

def WriteMove(num :int, mark :str, list_game : list):
    match num:
        case 1:
            if list_game[0][0] != ' ': return  False
            else: 
                list_game[0][0] = mark
                return True
        case 2:
            if list_game[0][1] != ' ': return  False
            else: 
                list_game[0][1] = mark
                return True
        case 3:
            if list_game[0][2] != ' ': return  False
            else: 
                list_game[0][2] = mark
                return True
        case 4:
            if list_game[1][0] != ' ': return  False
            else: 
                list_game[1][0] = mark
                return True
        case 5:
            if list_game[1][1] != ' ': return  False
            else: 
                list_game[1][1] = mark
                return True
        case 6:
            if list_game[1][2] != ' ': return  False
            else: 
                list_game[1][2] = mark
                return True
        case 7:
            if list_game[2][0] != ' ': return  False
            else: 
                list_game[2][0] = mark
                return True
        case 8:
            if list_game[2][1] != ' ': return  False
            else: 
                list_game[2][1] = mark
                return True
        case 9:
            if list_game[2][2] != ' ': return  False
            else: 
                list_game[2][2] = mark
                return True
        case _: return False


