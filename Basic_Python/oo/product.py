class Product:
    def __init__(self, name, price = 1.99, discount = 0):
        self.name = name
        self.__price = price   # two underscores makes the atribute private 
        self.discount = discount

    @property        # Decorator: the method is interpreted as a variable 
    def price(self):
        return self.__price

    @property
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price

    @property
    def final_price(self):
        return (1 - self.discount) * self.__price

p1 = Product('Pen', 4.99, 0.75)  # Product.__init__(p1, ...)
p2 = Product('Notebook', 12.99, 0.2)


print(p1.name, p1.price, p1.discount, p1.final_price)
print(p2.name, p2.price, p2.discount, p2.final_price)
