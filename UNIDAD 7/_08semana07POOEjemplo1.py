# sesion del dia lunes 14 de junio de 2021
# poo

class Empleado:
    def __init__(self):
        self.nombre = str(input('Nombre: '))
        self.sueldo = float (input('sueldo'))
    
    def imprimir (self):
        print ('nombre', self.nombre)
    
    def paga_impuesto (self):
        if (self.sueldo  > 3000):
            print ('Debe pagar impuesto')
        else:
            print ('No paga impuestos')


empleado1 = Empleado()

empleado1.paga_impuesto()

empleado1.imprimir()