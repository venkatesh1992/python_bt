class Product:
    def __init__(self):
        self.name = 'Iphone'
        self.description = 'It is awesome'
        self.price = 700

    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)


p1 = Product()
print(p1.name)
print(p1.description)
print(p1.price)

p2 = Product()
print(p2.name)
print(p2.description)
print(p2.price)


# instead of writing multiple print statements, we can go with instance method.
p3 = Product()
p3.display()
