class Course:
    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings

    def average(self):
        numOfRatings = len(self.ratings)
        averageRatings = sum(self.ratings) / numOfRatings
        print("Average rating of ", self.name, "is ", averageRatings)


c1 = Course('Java', [1, 2, 3, 4, 5])
print(c1.name)
print(c1.ratings)
c1.average()

c2 = Course('Python', [5, 5, 5, 5, 5])
print(c2.name)
print(c2.ratings)
c2.average()
