class Dog:
    animal = "dog"
    def __init__(self,breed,color):
        self.breed = breed
        self.color = color
breed1 = Dog('poodle','typically white')
breed2 = Dog('golden retriever', 'light brown')
print('Breed 1 is a',breed1.breed, 'they are', breed1.color)
print('Breed 2 is a',breed2.breed, 'they are', breed2.color)