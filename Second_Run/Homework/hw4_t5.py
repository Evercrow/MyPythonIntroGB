# Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.

def GatherEquations(*nameparts:str)->dict:  
    """
    ищет файлы equation{}.txt в папке запуска с заданными окончаниями названий.
    cобирает из них словарь многочленов, разбитых по членам в список
    """
    
    import pathlib
    equations = {}
    for i in range(len(nameparts)):                 
        file_path = (
            str(pathlib.Path(__file__).parent.resolve())
            +"\equation"+nameparts[i]+".txt")
        f = open(pathlib.Path(file_path), 'r')
        equations[i] = f.read()
        f.close()
        equations[i] = equations[i][:-4]
        equations[i] = equations[i].replace("x +", "x^1 +")
        equations[i] = equations[i].split(" + ")
    # print(equations)
    return equations

def SumEquations(joined_dict :dict)->list:
    """
    сложение членов всех элементов словаря по разрядам
    """
    
    max_power = 0
    for eq in joined_dict.values(): 
        if int(eq[0][-1]) > max_power : max_power = int(eq[0][-1])
    
    result_parts = []
    for k in range(max_power,0,-1):
        result_parts.append(0)
        for eq in joined_dict.values(): #цикл по многочленам словаря
            for item in eq: #цикл по членам многочлена
                if int(item[-1]) == k: #проверяем по степени, и суммируем
                    result_parts[-1] +=int(item[:item.find("*")])
                    break
    #добавляем хвосты без множителей(все последние элементы)
    result_parts.append(0)
    result_parts[-1] = sum(map(lambda x : int(x[-1]), joined_dict.values()))
    # print(result_parts)
    return result_parts

def EquationFromCoefficients(eq_list : list):
    """
    создаем и записываем в файл многочлен по списку из коэффициентов
    """
    equation = ''
    for i in range(len(eq_list)-1):
        if eq_list[i] == 0: continue
        equation += f'{eq_list[i]}*x^{len(eq_list)-1-i} + '
    equation += str(eq_list[-1])
    #подчищаем выражение    
    equation = equation.replace('x^1 ','x ') 
    equation = equation.replace(' 1*',' ')
    equation = equation.replace(' + 0','') 

    import pathlib 
    file_path = (str(pathlib.Path(__file__).parent.resolve())+"\joined_equation.txt")
    f = open(pathlib.Path(file_path), 'w')
    f.write(equation + " = 0")
    f.close()
    print(f"Result written to %\joined_equation.txt")

EquationFromCoefficients(SumEquations(GatherEquations('0','1')))