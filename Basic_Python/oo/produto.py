class Produto:
    def __init__(self, nome, preco = 1.99, desconto = 0):
        self.nome = nome
        self.__preco = preco
        self.desconto = desconto

    @property
    def preco(self):
        return self.__preco

    @property
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco

    @property
    def preco_final(self):
        return (1 - self.desconto) * self.preco

p1 = Produto('Caneta', 4.99, 0.75)  # Produto.__init__(p1, ...)
p2 = Produto('Caderno', 12.99, 0.2)


print(p1.nome, p1.preco, p1.desconto, p1.preco_final)
print(p2.nome, p2.preco, p2.desconto, p2.preco_final)
