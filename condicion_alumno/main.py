
import os
import menu_notas
import promedio
import reglas
import saludo


def confirmacion_lectura():
    return input('Presione ENTER para continuar:')
def limpiar_pantalla():
    return os.system('clear')
def pedir_nota():
    nota=input('Ingrese la nota del parcial:')
    while not(nota.isdigit() and (int(nota)>=0) and (int(nota)<=10)):
        print("Dato invalido, por favor ingrese su nota teniendo en cuenta que solo se pueden ingresar datos numericos desde el 0 al 10.")
        nota=input('Ingrese la nota del parcial:')
    nota=int(nota)
    return nota
def validar_option():
    option=input('Seleccione alguna de las opciones:')
    option=option.upper()
    while not((option.isalpha()) and (option=='L' or option=='R' or option=='P' or option=='T')):
        print('Dato invalido, solo ingrese alguna de las opciones marcadas.')
        option=input('Seleccione alguna de las opciones:')
    return option        
    
    
    
    
def main():
    menu=menu_notas.menu()
    while menu!=4:
        confirmacion_lectura()
        limpiar_pantalla()
        if menu==1:
           print(saludo.saludo())
           confirmacion_lectura()
           limpiar_pantalla()
           menu=menu_notas.menu()
        elif menu==2:
            p1=pedir_nota()
            p2=pedir_nota()
            condicion=promedio.promedio_alumno(p1,p2)
            print(condicion)
            confirmacion_lectura()
            limpiar_pantalla()
            menu=menu_notas.menu()
        else: 
            print('Seleccione entre las opciones: \nL-Libre\nR-Regular\nP-Promovido\nT-Todas')
            valid_option=validar_option()
            regla=reglas.reglas_condiciones(valid_option)
            print(regla)
            confirmacion_lectura()
            limpiar_pantalla()
            menu=menu_notas.menu()
    print('Saliendo...Hasta la proxima;)')
    
                
main()

    
    

