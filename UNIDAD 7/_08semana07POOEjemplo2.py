# clase del martes 15 de junio

# clase circulo

import math

class Circulo:
    # Constructor
    def __init__(self, radio = 1):
        self.radio = radio
    
    def setRadio (self, radio):
        self.radio = radio
    
    def getRadio (self):
        return self.radio
    
    def getPerimetro (self):
        p = 2 * self.radio * math.pi
        return p
    
    def getArea (self):
        a = math.pi * self.radio * self.radio
        return a

c1 = Circulo()
print ('radio: ', c1.radio)
print ('radio: ', c1.getRadio())
print ('perimetro: ',c1.getPerimetro())
print ('area: ', c1.getArea())
# radio:  1
# radio:  1
# perimetro:  6.283185307179586
# area:  3.141592653589793


c2 = Circulo (5)
print ('radio: ', c2.radio)
print ('radio: ', c2.getRadio())
print ('perimetro: ',c2.getPerimetro())
print ('area: ', c2.getArea())
# radio:  5
# radio:  5
# perimetro:  31.41592653589793
# area:  78.53981633974483

c3 = Circulo()
c3.setRadio (5)
print ('radio: ', c3.radio)
print ('radio: ', c3.getRadio())
print ('perimetro: ',c3.getPerimetro())
print ('area: ', c3.getArea())
# radio:  5
# radio:  5
# perimetro:  31.41592653589793
# area:  78.53981633974483