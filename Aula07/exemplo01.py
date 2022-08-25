class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    

class cliente:
    def __init__(self, nome):
        self.nome = nome

class carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for prod in self.produtos:
            print(prod.nome, prod.preco)

    def calcular_total(self):
        soma = 0
        for prod in self.produtos:
            soma += prod.preco
        print('Total da compra: ', soma)

cliente = cliente('paulo')

produto1 = produto('pen drive', 30)
produto2 = produto('1HD EXTERNO', 500)
produto3 = produto('celular', 1400)

carrinho1 = carrinho(cliente)
carrinho1.adicionar_produto(produto3)
carrinho1.adicionar_produto(produto3)
carrinho1.adicionar_produto(produto3)

carrinho1.listar_produtos()
carrinho1.calcular_total()