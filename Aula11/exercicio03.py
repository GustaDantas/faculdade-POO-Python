from abc import ABC, abstractmethod

class Funcionario:
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario():
        pass

class Gerente(Funcionario):

    def calcular_salario(self):
        return self.salario_base * 2

class Assistente(Funcionario):

    def calcular_salario(self):
        return self.salario_base

class Vendedor(Funcionario):

    def calcular_salario(self):
        return self.salario_base * 1.1

gerente = Gerente("Gilberto", 12543, 2000)
assistente = Assistente("Adalberto", 51423, 2000)
vendedor = Vendedor("Ronaldo", 54637, 2000)

print(gerente.calcular_salario())
print(assistente.calcular_salario())
print(vendedor.calcular_salario())
