class vechicle:
    def __init__(self,milage,max_speed):
        self.milage = milage
        self.max_speed = max_speed
lexus = vechicle(18,150)
print('Lexus has a limitation for its max speed which is', lexus.max_speed)