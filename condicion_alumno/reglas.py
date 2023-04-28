def reglas_condiciones(condicion):
    if condicion=='Libre':
        regla='''Si el alumno no ha aprobado ambos parciales (es decir, tiene nota
menor que 4 en alguno de ellos), entonces queda en condición de
libre (es decir, puede rendir un final extendido o recursar)'''
    elif condicion=='Regular':
        regla='''Para estar regular (cursada aprobada, pero debe rendir final), el
alumno debe haber aprobado ambos parciales (nota mayor o igual
a 4)'''
    elif condicion=='Promovido':
        regla='''Para estar promovido (es decir, cursada aprobada y no requiere
rendir final), el alumno debe haber aprobado ambos parciales y
tener un promedio mayor o igual a 8'''
    else:
        regla='''Si el alumno no ha aprobado ambos parciales (es decir, tiene nota
menor que 4 en alguno de ellos), entonces queda en condición de
libre (es decir, puede rendir un final extendido o recursar)

Para estar regular (cursada aprobada, pero debe rendir final), el
alumno debe haber aprobado ambos parciales (nota mayor o igual
a 4)

Para estar promovido (es decir, cursada aprobada y no requiere
rendir final), el alumno debe haber aprobado ambos parciales y
tener un promedio mayor o igual a 8'''
    return regla


