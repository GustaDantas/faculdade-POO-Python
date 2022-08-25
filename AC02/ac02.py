class Clube:
    def __init__(self):
        self.socios = []
            
    def associar(self, socio):
        self.socios.append(socio)

    def numero_de_socios(self):
        return len(self.socios)
    
   def mes_associacao(self):
      return len(self.socio.mes)


class Socio:
    def __init__(self, nome, cpf, nascimento, mes, ano):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.mes = mes
        self.ano = ano

