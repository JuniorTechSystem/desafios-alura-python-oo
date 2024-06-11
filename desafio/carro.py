from desafio.veiculo import Veiculo

class Carro (Veiculo):
    def __init__ (self, marca, modelo, cor):
        super().__init__ (marca,modelo)
        self.cor = cor

