class Cancion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        """Devuelve el título de la canción."""
        return self._titulo

    def get_autor(self):
        """Devuelve el autor de la canción."""
        return self._autor

    def set_titulo(self, titulo):
        """Establece un nuevo título para la canción."""
        self._titulo = titulo

    def set_autor(self, autor):
        """Establece un nuevo autor para la canción."""
        self._autor = autor

    def __str__(self):
        """Método opcional para imprimir la canción de forma legible."""
        return f"'{self._titulo}' por {self._autor}"