class Barco:
    def __init__ (self,coordenadas):
        self.coordenadas_vivas = coordenadas
        self.coordenadas_tocadas = []

    def atacar (self,coordenada):
        if coordenada in self.coordenadas_vivas:
            self.coordenadas_vivas.remove(coordenada)
            self.coordenadas_tocadas.append(coordenada)
            if len(self.coordenadas_vivas)==0:
                return 'h'
            return 't'
        elif coordenada in self.coordenadas_tocadas:
            return 't'
        return 'a'
    def print (self):
        print("coord vivas  :",self.coordenadas_vivas)
        print("coord tocadas:",self.coordenadas_tocadas)
    def is_hundido (self):
        if len(self.coordenadas_vivas)==0:
            return True
        return False
        
            
