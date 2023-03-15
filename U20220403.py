class Fabian (): #Clase padre
    ojosPadre = 'çafe'
    peloPadre = 'negro'
    pielPadre = 'moreno'

    def Herencia(): #primer metodo abstracto
        pass

    def Descripcion(): #segundo metodo abstracto
        pass

class Rachel(Fabian): #Primer clase hija
    
    def __init__(self, nombre,altura):
        self.nombre = nombre
        self.altura = altura

    def Herencia(self): #Implementando el metodo abstracto Herencia
        return '{} herede de su padre el color de ojos {}'.format(self.nombre,self.ojosPadre)
    
    def Descripcion(self): #Implementando el metodo abstracto Descripcion
        return '{} tiene una altura de {} cm'.format(self.nombre, self.altura)
    
class Sara(Fabian): #Segunda clase hija clase hija
    
    def __init__(self, nombre,altura):
        self.nombre = nombre
        self.altura = altura

    def Herencia(self): #Implementando el metodo abstracto Herencia
        return '{} herede de su padre el color piel {}'.format(self.nombre,self.pielPadre)
    
    def Descripcion(self): #Implementando el metodo abstracto Descripcion
        return '{} tiene una altura de {} cm'.format(self.nombre, self.altura)
    

class Osmin(Fabian): #Tercera clase hija
    
    def __init__(self, nombre,altura):
        self.nombre = nombre
        self.altura = altura

    def Herencia(self): #Implementando el metodo abstracto Herencia
        return '{} herede de su padre el color de pelo {}'.format(self.nombre,self.peloPadre)
    
    def Descripcion(self): #Implementando el metodo abstracto Descripcion
        return '{} tiene una altura de {} cm'.format(self.nombre, self.altura)


rachel = Rachel("rachel", 150) #Instancia de la primer clase hija
sara = Sara("sara", 170) #instancia de la segunca clase hija
osmin = Osmin("osmin", 184)

#imprimiendo los datos de la primer clase hija(rachel)
print(rachel.Herencia()) #primer metedodo abstracto
print(rachel.Descripcion()) #sedundo metodo abstracto
print("------------------------------------------------------")

#imprimiendo los datos de la primer clase hija(sara)
print(sara.Herencia()) #primer metedodo abstracto
print(sara.Descripcion()) #sedundo metodo abstracto
print("------------------------------------------------------")

#imprimiendo los datos de la primer clase hija(osmin)
print(osmin.Herencia()) #primer metedodo abstracto
print(osmin.Descripcion()) #sedundo metodo abstracto