def promedio_alumno(p1,p2):
    promedio=(p1+p2)/2
    if promedio<4:
        condicion_alumno=f'Su promedio es {promedio} y su condicion es Libre'
    elif promedio >=4 and promedio<8:
        condicion_alumno=f'Su promedio es {promedio} y su condicion es Regular'
    else:
        condicion_alumno=f'Su promedio es {promedio} y su condicion es Promovido'
    return condicion_alumno


