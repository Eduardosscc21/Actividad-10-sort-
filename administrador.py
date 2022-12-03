from algoritmos import distancia_euclidiana
from particula import Particula
import json

class Adminisrador:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula: Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula: Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)
            
    def __str__(self):
        return "".join(
            str(particula)+'\n' for particula in self.__particulas
        )
    def guardar(self,ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                print(lista)
                json.dump(lista, archivo, indent=5)
            return 1
        except :
            return 0   

    def abrir(self, ubicacion):
        try:
            with open(ubicacion,'r') as archivo:
                lista=json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0
    
    def __len__(self):
        return len(self.__particulas)
    
    def __iter__(self):
        self.cont=0

        return self
    
    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont+=1
            return particula
        else:
            raise StopIteration
            #En cada metodo se vuelven a convertir a enteros y flotantes para que haga bien la comparacion

    def ordenar_ID(self):  # Sirve para ordenar las particulas en orden ascendente (ID)
        self.__particulas.sort(key=lambda particulas: int(particulas.id))

    # Sirve para ordenar las particulas en orden descendente (Distancia)
    def ordenar_DISTANCIA(self):
        self.__particulas.sort(key=lambda particulas: float(
            particulas.distancia), reverse=True)

    # Sirve para ordenar las particulas en orden ascendente (Velocidad)
    def ordenar_VELOCIDAD(self):
        self.__particulas.sort(
            key=lambda particulas: int(particulas.velocidad))


        

        





