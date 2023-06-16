class ProductGarbage:
    def __init__(self):
        self.name = 'Iphone'
        self.description = 'It is awesome'
        self.price = 700

    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)

    def __del__(self):
        print("calling destruction")


p1 = ProductGarbage()
print(p1.name)
print(p1.description)
print(p1.price)

p2 = ProductGarbage()
print(p2.name)
print(p2.description)
print(p2.price)

# instead of writing multiple print statements, we can go with instance method.
p3 = ProductGarbage()
p3.display()

# whenever an object doesn't have a reference,
# In python it will be automatically garbage collected and memory will be freed up.
p1 = None
# it will automatically call destructor method(__del__) and free the space.
p2 = None
p3 = None
