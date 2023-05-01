def menu():
    print('**********MI PRIMER PROGRAMA MODULAR**********')
    print()
    print('1-Saludar')
    print('2-Ingresar notas')
    print('3-Reglas')
    print('4-Salir')
    print()
    option=input('Ingrese una opcion entre 1 y 4:')
    while not(option.isdigit()and (int(option)>0) and (int(option)<5)):
        print('Opcion invalida. Por favor solo ingrese un numero entre 1 y 4.')
        option=input('Ingrese una opcion entre 1 y 4:')
    option=int(option)
    return option
    

    