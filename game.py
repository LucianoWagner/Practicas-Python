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
acierto = 0
no_acierto = 0 #cuento la cantidad de aciertos y fallos en los resultados
for i in range(0, times):
  # Se eligen números y operador al azar
  number_1 = randrange(10)
  number_2 = randrange(10)
  operator = choice(operators)
  # Se imprime la cuenta.
  print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
  # Le pedimos al usuario el resultado
  result = int(input("resultado: "))
  if (operator == "+"): #ANALIZO CADA UNO PQ SON STRINGS LOS VALORES QUE PUEDE TOMAR OPERATOR.
    result_correcto= number_1 + number_2
  elif (operator == "-"):
    result_correcto= number_1 - number_2
  elif (operator == "/"):
    result_correcto= number_1 / number_2
  else:
    result_correcto= number_1 * number_2
  print('valor', result_correcto)
  print("valor 2", result)
  if (result == result_correcto): #compruebo el resultado correcto
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
print("La cantidad de aciertos es:",acierto)
print("La cantidad de fallos es:",no_acierto)