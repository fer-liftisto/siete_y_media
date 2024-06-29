import copy
def mi_mazo():
    numeros = list(range(1, 11))
    palos = ['Oros', 'Bastos', 'Espadas', 'Copas']
    
    mazo = [(str(num), palo) for palo in palos for num in numeros]

    return mazo

def dar(mazo):
    import random
    # print(dir(random))
    n_carta = random.choice(mazo) # Es una lista
    num  = n_carta[0]
    palo = n_carta[1]
    # mejor devolver una tupla
    match num:
        case '8':
            num = 'Sota'
        case'9':
            num = 'Caballo'
        case '10':
            num = 'Rey'

    carta = (num , palo) # para devolver una tupla
   
    mazo.remove(n_carta)
  
    return carta, mazo

def comprovar(mano, total):
    mano = copy.deepcopy(mano)  # para pasarle una copia
    if not mano[len(mano)-1][0].isnumeric():   
        mano[len(mano)-1] = ('0.5', [len(mano)-1][0])
                                                
    total += float(mano[len(mano)-1][0])
    
    print(f'El total es {total}')
    if total >  7.5:
        return True, total
    else:
        return False,  total

#########################################################################
def sieteYmedia():
    nombre_jugador = 'fer'
    #nombre_maquina = 'guindi'
    plantarse_jugador = False
    plantarse_maquina = False
    
    mazo = mi_mazo()

    mano_jugador = []
    mano_maquina = []
    carta_jugador, mazo_sin_carta = dar(mazo) # Da la carta y devuelve el resto
    # carta_maquina, mazo_sin_carta = dar(mazo)
    
    total = 0   
    while True:
        mano_jugador.append(carta_jugador)
        print(f'Mano de {nombre_jugador} es {mano_jugador}')
        print(carta_jugador)  #
        ##  https: // tutz.tv/python/copiar-lista ##
        
        te_pasaste, total = comprovar(mano_jugador, total)
        if te_pasaste:
            print(f'{nombre_jugador} te has pasado perdiste')
            for i in mano_jugador: 
                print(f'{i[0]} de {i[1]}')
            break
        else:
            opc = input('¿pedir otra carta?: ')
            if opc == 's':       
                carta_jugador, mazo_sin_carta = dar(mazo_sin_carta)
                
            else:
                break
        '''
            mano_maquina.append(maquina)
            if not comprovar(mano_maquina[len(mano_maquina)][0], nombre_maquina):
                print(f'{nombre_maquina} te has pasado perdiste')
            else:
                input('¿pedir otra carta?')
                maquina, mazo = dar(mazo)
        '''
        
    print(mazo) #
######################################################################
if __name__ == '__main__':
    sieteYmedia()
    print('prueba')