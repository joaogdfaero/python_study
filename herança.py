class Animal:
    def __init__(self, name):
        self.name = name
        
    def noise(self):
        pass

class Dog(Animal):
    def noise(self):
        print('Au au')
        

        

    