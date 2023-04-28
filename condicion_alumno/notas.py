
import os
import menu_notas
import promedio
import reglas
import saludo

def main():
    primer_vistazo=menu_notas.menu()
    while primer_vistazo!=4:
        confirmacion_de_lectura=input('Presione ENTER para continuar:')
        os.system('clear')
        if primer_vistazo==1:
           print(saludo.saludo())
           confirmacion_de_lectura=input('Presione ENTER para continuar:')
           os.system('clear')
           primer_vistazo=menu_notas.menu()
        elif primer_vistazo==2:
            p1=int(input('Ingrese la nota del primer parcial:'))
            p2=int(input('Ingrese la nota del segundo parcial:'))
            condicion=promedio.promedio_alumno(p1,p2)
            print(condicion)
            confirmacion_de_lectura=input('Presione ENTER para continuar:')
            os.system('clear')
            primer_vistazo=menu_notas.menu()
            
        else: 
            print('Seleccione entre las opciones: Libre, Regular, Promovido, Todas.')
            estado=input('Ingrese la condicion de la cual desea saber las reglas:')
            regla=reglas.reglas_condiciones(estado)
            print(regla)
            confirmacion_de_lectura=input('Presione ENTER para continuar:')
            os.system('clear')
            primer_vistazo=menu_notas.menu()
    print('Saliendo...Hasta la proxima;)')
    
                
main()

    
    

