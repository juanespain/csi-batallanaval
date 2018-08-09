# variables globales
from enum import Enum

port = 9950
ip_local = "192.168.1.22"
ip_enemiga = ""
mapa_propio = []
mapa_enemigo = []
barcos = []
# barcos_reglamento = [5,4,3,2,2,1,1]
barcos_reglamento = [2]


def recibir_ataque(coordenada):
    for barco in barcos:
        resultado = absbarco.atacar()
        if resultado!= 'a':
            break
    todos_hundidos = True
    for barco in barcos:
        if not barco.is_hundido():
            todos_hundidos = False
    if todos_hundidos:
        resultado = 'w'
    return resultado

class Barco:
    def __init__(self, coordenadas):
        self.coordenadas_vivas = coordenadas
        self.coordenadas_tocadas = []

    def atacar(self, coordenada):
        if coordenada in self.coordenadas_vivas:
            self.coordenadas_vivas.remove(coordenada)
            self.coordenadas_tocadas.append(coordenada)
            if len(self.coordenadas_vivas) == 0:
                return 'h'
            return 't'
        elif coordenada in self.coordenadas_tocadas:
            return 't'
        return 'a'
    def print_barco(self):
        print("coord vivas  :", self.coordenadas_vivas)
        print("coord tocadas:", self.coordenadas_tocadas)
    def is_hundido (self):
        if len(self.coordenadas_vivas)==0:
            return True
        return False


'''
class Resultado(Enum):
    AVERIDADO = 1
    AGUA = 2
    HUNDIDO = 3
    TODOS_HUNDIDOS = 4
    ERROR =5
    '''

def crearMapaVacio():
    pass

'''
por| ahora 10x10 luego variable
   mapa {'a'=['','','','','','','','',''],
         'b'=['','','','','','','','',''], ....
'''


def imprimirMapas():
    print("Base")
    imprimirMapas(mapa_propio);
    print("Enemigo")
    imprimirMapas(mapa_enemigo)
def getInitPos(pos, size):
    initNum =int(pos.split(",")[1])
    initLetra = pos.split(",")[0]
    sentido = pos.split(",")[2]
    esVertical = sentido.upper() == 'V'

    lista =[]
    for i in range(size):
        if esVertical:
                 lista += [(chr(ord(initLetra.upper + i)), initNum)]
        else:
                 lista += [(initLetra, initNum+i)]


    print (lista)
    return lista
def isValidaInitPos(pos):
    if pos.count(",") != 2:
        return False
    letra=pos.split(",")[0]
    num = pos.split(",")[1]
    sentido = pos.split(",")[2]
    if sentido.upper() != 'H' and sentido.upper() != 'V':
        print ("sentido")
        return False
    if ord(letra.lower()) < 97 or ord(letra.lower()) >117:
        print ("letra")
        return False
    if int(num) <1 or int(num)>10:
        print ("nnumero")
        return False
    return True

def setupBarcos():
    print ("Definiendo Barcos")
    i=0
    while  (True):
        print("barco numero " ,i)
        size = barcos_reglamento[i]
        pos  = input("insertar un barco de " + str(size) + ". Ej b,2,h en la posicion b2 horizontal o vertical: ")
        if isValidaInitPos(pos):
            barcos.append(Barco(getInitPos(pos,size)))
            i+=1
            if i >= len(barcos_reglamento):
                break




'''
 setupbarcos()
          llenar lista de barcos
          i=0
          while  ()
              input barco de size coordenada , v u h
si es valido y entra en el mapa
              barcos              new  barco()
llenar mapa propio con barcos


setupbarcos()
i=0;
while  ()
size = barcos_reglamento[i]
             pos =  input ("ingrese  un barco de size") coordenada , v u h
             if pos no entra en el mapa o toca otro barco
                 imprime error
                 continue


            else
                    barco =  new  barco()
                    barco.coordenadas_vivas <---
                    barco.size = size
                    barcos.append barco
                    i=1
                    si i = barcos_reglamento.size
                            break;
                    continue


'''


def iniciar():
    '''
    if Resultado.AGUA == Resultado(1):
        print("agua")
    if Resultado.AVERIDADO == Resultado(1):
        print("averiado")
        '''
    print ("Iniciado")
    crearMapaVacio()
    setupBarcos()
    #si mi ip es mas grande attacar else defender
    atacar()
def atacar():
    '''
    input keyboard devuelve coordenada valida
    sendattack y receive response,
                                     a=agua
                                     t=tocado
                                     h=hundido
                                     g=ganador
             si g corta con mensaje

    llena mapa enemigo
    quita diagonales
    imprime mapas
    defender
    '''
    print ("Atacamos")
    defender()

def defender():
    print("Recibimos ataque")
    '''
    socket listen
        check barcos
        estado si final mostrar
        llenar barco propio
        atacar
printmapa(mapa)
'''





#levantar argumentos "ip_local" , "ip enemiga"
#tomar ip_local
print ("inicio")
iniciar()

'''

class barco
   size
   coordenadas_vivas[]
   coordenadas_averiadas[]

'''
