# clase del dia martes 15 de junio
class Television:
    def __init__(self):
        self.canal = 1 # canal 1 por defecto
        self.volumen = 1 # volumen bajito
        self.on = False # televsión apagada
    
    def setCanal (self, canal):
        if (self.on == True and self.canal >= 1 and self.canal <= 120):
            self.canal = canal
        
    def setVolumen (self, volumen):
        if (self.on == True and self.volumen >=1 and self.volumen <= 7):
            self.volumen = volumen
        
    def setOn (self, on):
        self.on = on
    
    def getCanal (self):
        return self.canal
    def getVolumen (self):
        return self.volumen
    def getOn (self):
        return self.on
    
    def encenderTv (self):
        self.on = True
    def apagarTV (self):
        self.on = False
    
    def subirCanal (self):
        if (self.on == True and self.canal >= 1 and self.canal <= 120):
            self.canal +=  1
    def bajarCanal (self):
        if (self.on == True and self.canal >= 1 and self.canal <= 120):
            self.canal -= 1
    
    def subirVolumen (self):
        if (self.on == True and self.volumen >=1 and self.volumen <= 7):
            self.volumen += 1
    def bajarVolumen ( self):
        if (self.on == True and self.volumen >=1 and self.volumen <= 7):
            self.volumen -= 1

tv1 = Television()
tv1.encenderTv () # True
tv1.setCanal (100) # 100
tv1.setVolumen (5) # 5

print (tv1.getOn())  # True
print (tv1.getCanal()) # 100
print (tv1.getVolumen()) # 5

tv2 = Television()
tv2.encenderTv()
tv2.subirCanal()
tv2.subirCanal()
tv2.subirCanal()
tv2.subirCanal()
tv2.subirCanal()
tv2.subirCanal()
tv2.subirCanal()
tv2.subirVolumen()
tv2.subirVolumen()
tv2.subirVolumen()
tv2.subirVolumen()
tv2.subirVolumen()
tv2.subirVolumen()
tv2.apagarTV()

print (tv2.getOn())  # True
print (tv2.getCanal()) # 8
print (tv2.getVolumen()) # 7
print (tv2.getOn())  # false