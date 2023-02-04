def victory(list_game):

    check_list = []
    cell_num = 1
    for row in range(3):
        for col in range(3):
            if list_game[row][col] !=' ':
                check_list.append = cell_num
            else:
                check_list[row][col] = list_game[row][col]
        cell_num += 1 
    print(check_list)
    for i in range(3):
        if (check_list[i][0] ==  check_list[i][1] == check_list[i][2])  or (check_list[0][i] ==  check_list[1][i] == check_list[2][i]):
            res = True
            return res
    if (check_list[0][0] ==  check_list[1][1] == check_list[2][2])  or (check_list[-1][-1] ==  check_list[-2][-2] == check_list[-3][-3]):
        res = True
        return res
    else:
        res = False
        return res
    
list_game = [["x", "", ""], ["x", "", ""], ["o", "", ""]]
print(victory(list_game))

