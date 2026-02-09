class Employee:
    def __init__(self):
        print("employee created")
    def __del__(self):
        print("descrutor created")
def Createobj():
    obj = Employee()
    return obj
obj = Createobj()