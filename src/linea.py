class Linea:
    def __init__(self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b
    
    def mueve_derecha(self, distancia):
        self.punto_a.x += distancia
        self.punto_b.x += distancia
    
    def mueve_izquierda(self, distancia):
        self.punto_a.x -= distancia
        self.punto_b.x -= distancia

    def mueve_arriba(self, distancia):
        self.punto_a.y += distancia
        self.punto_b.y += distancia

    def mueve_abajo(self, distancia):
        self.punto_a.y -= distancia
        self.punto_b.y -= distancia

    def __str__(self):
        """Representación visual de la línea para facilitar el debug."""
        return f"Línea de {self._punto_a.impresion()} a {self._punto_b.impresion()}"
