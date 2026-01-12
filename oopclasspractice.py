class sports:
    def __init__(self,name,type):
        self.name = name
        self.type = type
volleyball = sports('volleyball','balls')
print("this sport uses", volleyball.type,'to play')