class fruit:
    taste = 'sweet'
    def __init__(self, name, color):
        self.name = name
        self.color = color
apple=fruit('apple','red')
print("the name of the fruit is",apple.color,apple.name)
print(apple.taste)