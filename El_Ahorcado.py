# El ahorcado
#from MODULO import VARIABLE

import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual

def obtener_palabra_valida(palabras):
    # seleccionar una palabra al azar de la lista de palabras.
    palabra = random.choice(palabras)
    
#mientras la palabra tenga guion o espacio seguir seleccionando
    while '-' in palabra or ' ' in palabra:
       palabra =random.choice(palabras)
#retornar en mayúscula
    return palabra.upper()
    


def ahorcado():

    print("=========================================")
    print("  ¡Bienvenido(a) al juego del Ahorcado!  ")
    print("=========================================")

    palabra = obtener_palabra_valida(palabras)


    # seguimiento de letras
    # Conjuntos estructura de datos especifico no guarda repeticiones. se usa set
    # set (palabra) para tomar todos los caracteres de la letra, pero no repite letras
    letras_por_adivinar = set(palabra)
    # Actualizar el conjunto. al principio debe estar vacio
    letras_adivinadas = set()
    # Se llama al modulo string y catalogo de caracteres ascii. sin ñ
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    # ciclos para adivinar
    while len(letras_por_adivinar) > 0 and vidas > 0:
        # el metodo join une todos lo elementos de un conjunto o secuencia con el ' '.
        # Letras adivinadas
        #' '.join({'a', 'b', 'c'}) ---> 'A B C'
        print(f"Te quedan {vidas} vidas y has usado estas letras:{''. join(letras_adivinadas)}")
        
        # status de la palabrabra_, list comprensehesion
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]

        # Mostrar estado de la horca
        print(vidas_diccionario_visual[vidas])
        # Mostrar las letras separas por un espacio
        print(f"Palabras: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        # Si  la letra escogida por el usuario esta en el 
        # abecedario y no esta en el conjunto de letras que ya se han ingresado
        # que ya se han ingresado, se añade la letra al conjunto de letras ingresadas
        if letra_usuario  in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            # Si la letra está en la palabra
            # quitar la letra del conjunto de letras por adivinar
            # Si no esta en la palabra, quitar la vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print (' ')
            else:
                vidas -=1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
            
        # si la letra escogida por el usuario ya fue ingresada
        elif letra_usuario in letras_adivinadas:
           print("\nYa escogiste esa letra. Elige otra letra.")
        else:
            print("\nEsta letra no es valida.")


            
            
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. La palabra era: {palabra}")
    else:
        print(f"¡Enhorabuena! ¡Adivinaste la palabra!")

ahorcado()
        
              


    
