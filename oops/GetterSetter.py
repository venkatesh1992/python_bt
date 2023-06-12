class GetterSetter:
    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def setSalary(self, sal):
        self.salary = sal

    def getSalary(self):
        return self.salary

    def setTechnologies(self, techs):
        self.technologies = techs

    def getTechnologies(self):
        return self.technologies


g1 = GetterSetter()
g1.setName("Venki")
print(g1.getName())
g1.setSalary(100)
print(g1.getSalary())
g1.setTechnologies(['Java', 'Python', 'Spark'])
print(g1.getTechnologies())
