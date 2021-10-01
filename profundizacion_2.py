# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''



print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

numero_primero = float(input("Ingrese el primer número para el calculo\n"))
simbolo = input("ingrese el simbolo de la ecuacion que desea calcular")
numero_segundo = float(input("Ingrese el segundo número para el calculo\n"))

while simbolo != "=":
    if simbolo == "+":
      print("el resultado es =", numero_primero + numero_segundo)
    elif simbolo == "-":
       print("el resultado es =",numero_primero - numero_segundo)
    elif simbolo == "*":
        print("el resultado es =", numero_primero * numero_segundo)
    elif simbolo == "/":
        print("el resultado es =", numero_primero / numero_segundo)
    elif simbolo == "**":
        print("el resultado es =", numero_primero ** numero_segundo)
 
    simbolo = input("Fin de la operacion")


