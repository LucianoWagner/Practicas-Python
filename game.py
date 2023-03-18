from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-","/","*"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
#variables utilizadas para contar los aciertos y fallos en los resultados
acierto = 0
no_acierto = 0 
for i in range(0, times):
  # Se eligen números y operador al azar
  number_1 = randrange(10)
  number_2 = randrange(10)
  operator = choice(operators)
  # Se tiene en cuenta el caso de la divison por 0.
  if (operator == "/" and number_2 == 0):
    number_2 = randrange(1,10)
  # Se imprime la cuenta.
  print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
  # Le pedimos al usuario el resultado
  result = int(input("resultado: "))
  #ANALIZO, TENIENDO EN CUENTA EL OPERADOR, EL RESULTADO CORRECTO.
  match operator:
    case '+':result_correcto= number_1 + number_2
    case '-':result_correcto= number_1 - number_2
    case '*':result_correcto= number_1 * number_2
    case '/':result_correcto= number_1 / number_2
  #compruebo si el resultado fue correcto.
  if (result == result_correcto): 
    print('EL RESULTADO ES CORRECTO')
    acierto += 1
  else:
    print('EL RESULTADO ES INCORRECTO')
    no_acierto += 1
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
#imprimo la cantidad de aciertos y fallos.
print(f"La cantidad de aciertos es:",{acierto})
print(f"La cantidad de fallos es:",{no_acierto})