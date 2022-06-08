# Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.

#Возьмем функцию создания многочлена из 33-й задачи


def GatherEquations(*nameparts):  #ищет файлы в папке запуска с заданными окончаниями названий
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
    #print(equations)
    return equations

def SumEquations(joined_dict :dict):
    
    max_power = 0
    for eq in joined_dict.values(): 
        if int(eq[0][-1]) > max_power : max_power = int(eq[0][-1])
    
    result_parts = []
    for k in range(max_power,0,-1):
        result_parts.append(0)
        for eq in joined_dict.values(): #цикл по многочленам словаря
            for item in eq: #цикл по членам многочлена
                if int(item[-1]) == k:
                    result_parts[-1] +=int(item[:item.find("*")])
                    break
    result_parts.append(0)
    result_parts[-1] = sum(map(lambda x : int(x[-1]), joined_dict.values()))
    # print(result_parts)
    return result_parts


from  create_random_equation import RandomCoefficients as cr_new

# cr_new(6,'1')  #создаем, при необходимости, новые входные многочлены в файлах.
# cr_new(8,'2') 
## cr_new(5,'1','2','3') #можно сразу несколько одинаковой длины.


from  export_equation import EquationFromCoefficients as eq_export

eq_export(SumEquations(GatherEquations('1','2')))