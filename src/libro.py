class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, ciudad, pais, fecha):
        self._titulo = titulo
        self._autor = autor  # Objeto de la clase Persona
        self._isbn = isbn
        self._paginas = paginas
        self._edicion = edicion
        self._editorial = editorial
        self._ciudad = ciudad
        self._pais = pais
        self._fecha = fecha

    # --- Getters ---
    def get_titulo(self): return self._titulo
    def get_autor(self): return self._autor
    def get_isbn(self): return self._isbn
    def get_paginas(self): return self._paginas
    def get_edicion(self): return self._edicion
    def get_editorial(self): return self._editorial
    def get_lugar(self): return f"{self._ciudad}, {self._pais}"
    def get_fecha(self): return self._fecha

    # --- Setters ---
    def set_titulo(self, v): self._titulo = v
    def set_autor(self, v): self._autor = v
    def set_isbn(self, v): self._isbn = v
    def set_paginas(self, v): self._paginas = v
    def set_edicion(self, v): self._edicion = v
    def set_editorial(self, v): self._editorial = v
    def set_lugar(self, ciudad, pais): 
        self._ciudad = ciudad
        self._pais = pais
    def set_fecha(self, v): self._fecha = v

    # --- Métodos de Información ---
    def leer_informacion(self):
        """Devuelve una tupla con los datos crudos."""
        return (self._titulo, self._autor, self._isbn, self._editorial)

    def mostrar_informacion(self):
        """Muestra la información con el formato bibliográfico solicitado."""
        print(f"Título: {self._titulo}")
        print(f"{self._edicion}ª edición")
        print(f"Autor: {self._autor}")
        print(f"ISBN: {self._isbn}")
        print(f"{self._editorial}, {self._ciudad} ({self._pais}), {self._fecha}")
        print(f"{self._paginas} páginas")