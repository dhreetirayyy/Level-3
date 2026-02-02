class fruits:
    def __init__(self,name,color,taste):
        self.name = name
        self.color = color
        self.taste = taste
    def intro(self):
        print("Hello I am an",self.taste,self.color,self.name)
apple = fruits('apple','red','sweet')
mango = fruits('mango','yellow','yummy')
kiwi = fruits('kiwi','green','delicious')
apple.intro()
kiwi.intro()
mango.intro()