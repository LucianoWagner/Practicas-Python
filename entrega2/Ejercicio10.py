nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR','David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo','Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 
'Ignacio', 'Jonathan','Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises','Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

def recopilar_info ():
    lista_nombres=nombres.replace('\'','').replace('\n','').replace(' ','').split(',')
    return list(zip(lista_nombres,notas_1,notas_2))

def promedio_notas (t):
    promedio=sum(t[1:]) / 2 
    return (t[0],promedio)

def promedio_curso (l):
    notas_totales=0
    for elem in l:
        notas_totales+= sum(elem[1:])
    return notas_totales / (len(l) * 2)

def maximo_promedio(lt):
    return max(lt,key=lambda x: x[1])

def minimo_nota(lt):
    return min(lt,key=lambda x:(x[1],x[2]))

#inciso A
lista_tupla= recopilar_info()
print(lista_tupla)
#inciso B
lista_promedio_estudiantes=list(map(promedio_notas,lista_tupla))
print('Promedio de los estudiantes:')
print(lista_promedio_estudiantes)
#inciso C 
print("El promedio general del curso es:", promedio_curso(lista_tupla))
#inciso D
estudiante_max_promedio,promedio_max= maximo_promedio(lista_promedio_estudiantes)
print(f"El estudiante {estudiante_max_promedio} tiene la nota promedio mas alta: {promedio_max}") 
#inciso E
tupla_min=minimo_nota(lista_tupla)
print(f"El estudiante {tupla_min[0]} posee la nota mas baja")