class Dog:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(f'Au au ({self.name} acuando)')
        
Chumbinho = Dog('Chumbinho', 10)
Chumbinho.bark()
        

    