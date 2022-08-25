class Motor:
   def __init__(self, cilindrada, potencia):
      self.cilindrada = cilindrada
      self.potencia = potencia

class Veiculo:
   def __init__(self, ano, preco, motor):
      self.ano = ano
      self.preco = preco
      self.motor = motor

   def exibir_dados(self):
      print('----------------')
      print('Ano: ', self.ano)
      print('Preço: ', self.preco)
      print('Cilindrada do Motor: ', self.motor.cilindrada)
      print('Potência do Motor: ', self.motor.potencia)


class Carro(Veiculo):
   def __init__(self, ano, preco, motor, cor, modelo):
      super().__init__(ano, preco, motor)
      self.cor = cor
      self.modelo = modelo

   def exibir_dados(self):
      super().__init__(ano, preco, motor)

class Caminhao(Veiculo):
   def __init__(self, ano, preco, motor, comprimento):
      super().__init__(ano, preco, motor)
      self.comprimento = comprimento
