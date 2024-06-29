##   https: // youtu.be/YAIF-XsTxEU?si = Y1d3JhHRovmqzbaZ  ##
from os import system

def mi_mazo():
    numeros = list(range(1, 11))
    palos = ['Oros', 'Bastos', 'Espadas', 'Copas']

    mazo = [(str(num), palo) for palo in palos for num in numeros]

    return set(mazo)

def dar(mazo):
    
    import random
    mazo_list = list(mazo)
    carta = random.choice(mazo_list) # tuple
    
    mazo = set(mazo_list)
    carta_set = {carta}
    mazo_sincarta = mazo - carta_set
    
    return carta, mazo_sincarta # tuple, set

def comprovar(mano, total):
    #print('tipo mano_jugador', type(mano_jugador))  # set
    #print('tipo total', type(total))  # tuple
    
    valor = int(mano[len(mano)-1][0])
    match valor:
        case 8 | 9 | 10:
            valor = 0.5
        case _ :
            pass
    total += valor

    if total > 7.5 :
        te_pasate = True
    else:
        te_pasate = False
    
    return te_pasate ,total

def perdiste(nombre, mano, total):
    print(f'{nombre} te has pasado perdiste')
    print()
    
    for i in mano:
        print(f'{i[0]} de {i[1]}')
    
    print()
    print('El total es => ', total)
    print()


def comprobar(nombre, mano, total):
    print(f'{nombre} Tu mamano es')
    for i in mano:
        print(f'{i[0]} de {i[1]}')
    print('El total es => ', total)
    return total


def mostrar(carta_jugador, mano_jugador,nombre_jugador):
    match carta_jugador[0]:
            case '8':
               carta_jugador = ('Sota', carta_jugador[1])
            case '9':
               carta_jugador = ('Caballo', carta_jugador[1])
            case '10':
               carta_jugador = ('Rey', carta_jugador[1])

    mano_jugador.append(carta_jugador)
    
    print('Mano de ' + nombre_jugador + ' es: ',end='')
    for i in mano_jugador:
        print('|' + i[0] + ' de ' + i[1],end='|')
    print()    
    
    return mano_jugador


def mostrar_m(carta_jugador, mano_jugador, nombre_jugador):
    match carta_jugador[0]:
            case '8':
               carta_jugador = ('Sota', carta_jugador[1])
            case '9':
               carta_jugador = ('Caballo', carta_jugador[1])
            case '10':
               carta_jugador = ('Rey', carta_jugador[1])

    mano_jugador.append(carta_jugador)

    return mano_jugador

def menu_j():
    opc = input('¿pedir otra carta? (s/n) : ')
    if opc == 's':
        return True
    else:
        return False


def menu_m(total_m):
    
    if total_m < 6:
        return True
    else:
        return False

############################################################################
def sieteYmedia():
    nombre_jugador = 'Fer'
    nombre_maquina = 'guindi'
    plantarse_jugador = False
    plantarse_maquina = False

    mazo = mi_mazo() #*
    
    mano_jugador = []
    mano_j = []
    mano_maquina = []
    mano_m = []

    
    # Da la carta y devuelve el resto
    carta_jugador, mazo_sin_carta = dar(mazo) ########aqui#########
    carta_maquina, mazo_sin_carta = dar(mazo)
    #print('tipo mazo_sin_carta',type(mazo_sin_carta))  # set
    #print('tipo carta_jugador', type(carta_jugador))  # tuple
    
    total_j = 0
    while True:
        
        mano_j.append(carta_jugador)
        
        system("cls")
        mano_jugador = mostrar(carta_jugador, mano_jugador,nombre_jugador)
        
        ##  https: // tutz.tv/python/copiar-lista ##
        
        te_pasaste, total_j = comprovar(mano_j, total_j) ### aquiiii
        
        if te_pasaste:
            system("cls")
            perdiste(nombre_jugador, mano_jugador, total_j)
            break
        
        if menu_j():
            carta_jugador, mazo_sin_carta =  dar(mazo_sin_carta)
        else:
            system("cls")
            total_j = comprobar(nombre_jugador, mano_jugador, total_j)
            break
############################################################################################
    total_m = 0
    while True:

        mano_m.append(carta_maquina)


        mano_maquina = mostrar_m(carta_maquina, mano_maquina, nombre_maquina)

        ##  https: // tutz.tv/python/copiar-lista ##

        te_pasaste, total_m = comprovar(mano_m, total_m)  # aquiiii

        if te_pasaste:
            print()
            perdiste(nombre_maquina, mano_maquina, total_m)
            break

        if menu_m(total_m):
            carta_maquina, mazo_sin_carta = dar(mazo_sin_carta)
        else:    
            print()
            total_m = comprobar(nombre_maquina, mano_maquina, total_m)
            print()
            break


if __name__ == '__main__':
    sieteYmedia()
    
