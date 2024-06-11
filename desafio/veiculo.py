from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__ (self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

def ligar(self):
        print(f"O carro {self.modelo} está ligado.")
