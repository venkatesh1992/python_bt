class ObjectCounter:
    counter = 0

    def __init__(self):
        ObjectCounter.counter += 1

    @staticmethod
    def display():
        print(ObjectCounter.counter)
        

o1 = ObjectCounter()
o2 = ObjectCounter()

ObjectCounter.display()  # static methods we can call by class name
