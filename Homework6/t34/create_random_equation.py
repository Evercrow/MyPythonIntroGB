
def RandomCoefficients(k,*naming):
    for suffix in range(len(naming)):
        from random import randint
        eq_list =[randint(0,100)]
        equation = str(eq_list[0])
        for i in range(1,k+1):
            eq_list.append(randint(0,100))
            if eq_list[-1] == 0 : continue
            equation = f'{eq_list[-1]}*x^{i} + '+ equation
        #подчищаем выражение    
        equation = equation.replace('x^1 ','x ') 
        equation = equation.replace(' 1*',' ')
        equation = equation.replace(' + 0','') 

        import pathlib 
        file_path = (str(pathlib.Path(__file__).parent.resolve())+"\equation"+naming[suffix]+".txt")
        f = open(pathlib.Path(file_path), 'w')
        f.write(equation + " = 0")
        f.close()
    return eq_list

    
        