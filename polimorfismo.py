class Shape:
        pass
    
class Rectangle(Shape):
    def __init__ (self, altura, largura):
        self.altura = altura
        self.largura = largura
        
class Circle(Shape):
    def __init__ (self, raio):
        self.raio = raio


def area(shape):
    if isinstance(shape, Rectangle):
        return shape.altura * shape.largura
    elif isinstance(shape, Circle):
        return 3.1416 * (shape.raio**2)
    else:
        raise ValueError("Unsupported shape")
    
retangulo = Rectangle(2,3)
circulo = Circle(4)

print(area(retangulo))
print(area(circulo))


    
    
