#Piedra papel o tijera
import random


def jugar():
    usuario = input("Escoge una opción: 'pi' para piedra,'pa' para papel, 'ti' para tijera, 'sp' para Spock, 'li' para lagarto.\n").lower()
    ordenador = random.choice(['pi', 'pa', 'ti', 'sp','li'])
    print(f"Ordenador: {ordenador}")
    if usuario == ordenador:
        return '¡Empate!'

    if gano_el_jugador(usuario, ordenador):
        return'¡Ganaste!'

    return '¡Perdiste!'


def gano_el_jugador(jugador, oponente):
    #Retorna True si gana el jugador
    if (( jugador == 'pi' and oponente =='ti')
        or (jugador =='ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')
        or (jugador == 'li' and oponente == 'sp')
        or (jugador == 'sp' and oponente == 'ti')
        or (jugador == 'pi' and oponente == 'li')
        or (jugador == 'ti'and oponente == 'li')
        or (jugador == 'li' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'sp')
        or (jugador == 'sp' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())
