class Student:
    major = 'ECE'  # class variable or static variable

    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name


s1 = Student(1, 'Venkatesh')
s2 = Student(2, 'Ravi')
print(s1.major, s1.rollno, s1.name) # constructor variables we need to call with object
print(s2.major, s2.rollno, s2.name)
print(Student.major)  # we can call static variable by using class name itself
