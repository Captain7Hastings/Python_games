# Adivina el número
import random

def adivina_el_numero(x):

    print("==============")
    print("   ¡Bienvenido(a) al Juego!  ")
    print("==============")
    print("Tu meta es adivinar el número generado por el ordenador.")

    numero_aleatorio = random.randint(1, x) # Número aleatorio entr 1 y x inclusive

    prediccion = 0

    #Es while y no for, porque necesitas repeteir un numero inespecifico de veces

    while prediccion != numero_aleatorio: # Mientras el usuario no adivine el numero debe de seguir el proceso
        #El usuario ingresa un  numero
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("Intetalo otra vez. Este número es muy pequeño")
        elif prediccion > numero_aleatorio:
            print ("Intentalo otra vez . Este numero es muy grande")
    print(f" ¡Felicidades! Adivinaste el número {numero_aleatorio} correctamente.")

    
adivina_el_numero (10)    
        
        
