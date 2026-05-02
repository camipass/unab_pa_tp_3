class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y
    
    def impresion(self):
        return f"Punto({self.x}, {self.y})"

    def opuesto(self):
        return Punto(-self.x, -self.y)

""" Ejemplo de Uso
# Crear un punto en la coordenada (3, 4)
p1 = Punto(3, 4)

print(f"Coordenadas originales: {p1.impresion()}") 
# Salida: Punto(3, 4)

# Obtener el opuesto
p_opuesto = p1.opuesto()
print(f"Punto opuesto: {p_opuesto.impresion()}") 
# Salida: Punto(-3, -4)

# Calcular distancia
dist = p1.distancia_al_origen()
print(f"Distancia al origen: {dist}") 
# Salida: 5.0 (un clásico triángulo 3-4-5)
"""