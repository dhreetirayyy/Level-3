class fruit:
    def __del__(self):
        print('Object destroyed')
    
apple = fruit()