class mom:
    def __init__(self,hair_type,eyes):
        self.hair_type = hair_type
        self.eyes = eyes
    def display(self):
        print("She has",self.hair_type)
        print("With", self.eyes, "eyes.")
class daughter(mom):
    def __init__(self,age,height,hair_type,eyes):
        self.age = age
        self.height = height
        mom.__init__(self,hair_type,eyes)
obj = daughter(13,117,'wavy hair','dark brown')
obj.display()
