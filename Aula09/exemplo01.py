class Veiculo:
   def __init__(self, marca, modelo, placa):
      self.marca = marca
      self.modelo = modelo
      self.placa = placa

   def exibir(self):
      print('----------------------------')
      print('Marca: ', self.marca)
      print('Modelo: ', self.modelo)
      print('Placa: ', self.placa)

class Carro(Veiculo):
   def __init__(self, marca, modelo, placa, portas):
      super().__init__(marca, modelo, placa)
      self.portas = portas

   def exibir(self):
      super().exibir()
      print('Portas: ', self.portas)

class Moto(Veiculo):
   def __init__(self, marca, modelo, placa, partida_eletrica):
      super().__init__(marca, modelo, placa)
      self.partida_eletrica = partida_eletrica
      
   def exibir(self):
      super().exibir()
      print('Partida Elétrica: ', self.partida_eletrica)

carro1 = Carro("Ford", "Ka", "AAA-1234", 4)
carro1.exibir()

moto1 = Moto("Honda", "CG", "ABC-333", "Sim")
moto1.exibir()