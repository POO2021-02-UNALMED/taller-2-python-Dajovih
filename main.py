class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    
    def cambiarColor(self,color):
        if ((color=="rojo") or (color=="verde") or (color=="amarillo") or (color=="negro") or (color=="blanco")):
            self.color=color

class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro

    def cantidadAsientos(self):
        CANTIDAD=0
        for i in self.asientos:
            if type(i)==Asiento:
                CANTIDAD+=1
        return CANTIDAD
    def verificarIntegridad(self):
        RESPUESTA="Auto original"
        for i in self.asientos:
            if ((type(i)==Asiento) and self.motor.registro==self.registro==i.registro):
                continue
            else:
                RESPUESTA="Las piezas no son originales"
                break
        return RESPUESTA



class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    
    def cambiarRegistro(self,registro):
        self.registro=registro
    
    def asignarTipo(self,tipo):
        if ((tipo=="gasolina") or (tipo=="electrico")):
            self.tipo=tipo