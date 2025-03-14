#criando classe
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, quantidade):
        self.velocidade += quantidade
        print(f"Velocidade atual: {self.velocidade} km/h")
    
    def frear(self, quantidade):
        self.velocidade -= quantidade
        if (self.velocidade < 0):
            self.velocidade = 0
        print(f"Velocidade atual: {self.velocidade} km/h")


primeiro_carro = Carro('Honda', 'Civic')

primeiro_carro.acelerar(60)
primeiro_carro.frear(20)