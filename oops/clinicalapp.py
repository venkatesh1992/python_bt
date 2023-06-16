class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.clinical = []

    def addClinical(self, clinical):
        self.clinical.append(clinical)


class Clinical:
    def __init__(self, testName, testValue):
        self.testName = testName
        self.testValue = testValue


p = Patient('Venkatesh',28)
c1 = Clinical('BP','80/120')
p.addClinical(c1)

c2 = Clinical("Heart rate",'80 pm')
p.addClinical(c2)

print(p.name)
for i in p.clinical:
    print(i.testName, i.testValue)
