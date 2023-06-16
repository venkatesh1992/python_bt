class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    class Engine:
        def __init__(self, enumber):
            self.enumber = enumber

        def start(self):
            print('Engine started')


c = Car('BMW', 2020)
e = c.Engine(123)
e.start()
print(c.model)
