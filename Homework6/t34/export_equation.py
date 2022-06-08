
def EquationFromCoefficients(eq_list : list):
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