class StudentPrivate:

    # def __init__(self, rollno, name):
    #     self.rollno = rollno
    #     self.name = name

    # to make variables as private we will use __
    def __init__(self, rollno, name):
        self.__rollno = rollno
        self.__name = name

    def display(self):
        print(self.__rollno)
        print(self.__name)


s1 = StudentPrivate(1, 'Venkatesh')
# print(s1.rollno, s1.name) # this is giving error
# print(s1.__rollno, s1.__name) # this is also not working.
s1.display()
print(s1._StudentPrivate__rollno)
print(s1._StudentPrivate__name)

