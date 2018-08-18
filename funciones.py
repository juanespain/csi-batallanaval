def recibir_ataque(coordenada):
    for barco in barcos:  # Marca como no definida Barcos
        resultado = barco.atacar(coordenada)
        if resultado != 'a':
            break
    todos_hundidos = True
    for barco in barcos:  # Marca como no definida Barcos
        if not barco.is_hundido():
            todos_hundidos = False
    if todos_hundidos:
        resultado = 'w'
    return resultado


def crear_mapa():
    mapa = {}
    for x in range(ord('A'), ord('J')+1):
        mapa[chr(x)] = ['×']*10
    return mapa


def imprimir_mapa(mapa):
    print("   1  2  3  4  5  6  7  8  9  10")
    print("  ------------------------------")
    for fila in mapa:
        print('fila+"|", end=''')  # Aca tamien me tira un error el debugger
        for elemento in mapa[fila]:
            print('elemento+' ', end=''')
        print("|")
    print("  ------------------------------")
