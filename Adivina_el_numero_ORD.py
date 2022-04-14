import random


def adivina_el_numero_computadora(x):

    print("==========================")
    print(" ¡Bienvenido(a) al Juego! ")
    print("==========================")
    print(f"Seleciona un número entre 1 y {x} para el ordenador intente adivinarlo")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
      #ciclo while porque no sabemos cuantos intentos se van a necesitar
    while respuesta != "c" :
    #Generar prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior # también podria ser el límite superior, porque son iguales.

        #Obtener una respuesta del usuario. con lower se evita el error de minúsculas y mayusculas.convierte todo a minuscula.

        respuesta = input(f"Mi predicción es {prediccion}. Si es muy alta, ingresa (A).\
                          Si es muy baja, ingresa (B). Si es correcta, ingresa (C)").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
        else:
            print (f"!Tu número es {prediccion}!")

adivina_el_numero_computadora(10) # se cierra llamando llamando a la funcion y definiendo x
                    
        
        
