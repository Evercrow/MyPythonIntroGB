# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def RandomCoefficients(k):
    from random import randint
    #сразу добавляем коэффициент нулевой степени
    eq_list =[randint(0,100)]
    equation = str(eq_list[0])
    for i in range(1,k+1):
        eq_list.append(randint(0,100))
        if eq_list[-1] == 0 : continue #не пишем члены равные 0
        equation = f'{eq_list[-1]}*x^{i} + '+ equation
    #подчищаем выражение  от 1 и 0  
    equation = equation.replace('x^1 ','x ') 
    equation = equation.replace(' 1*',' ')
    equation = equation.replace(' + 0','') 

    from pathlib import Path
    #здесь немного заморочусь с автонаименованием записываемого файла, чтобы использовать было проще в следующей задачке
    import glob
    parent_path = str(Path(__file__).parent.resolve())
    count =len(glob.glob(parent_path+"\equation*"))
    file_path = Path(parent_path+f"\equation{count}.txt")
    f = open(file_path, 'w')
    f.write(equation + " = 0")
    f.close()
    return eq_list


k_user = int(input("Введите степень многочлена: "))
# print(f"список коэффициэнтов,начиная с нулевой степени:\n{RandomCoefficients(k_user)}") 
print(f"список коэффициэнтов,начиная с высшей степени:\n{RandomCoefficients(k_user)[::-1]}") #так проще сравнивать с файлом
