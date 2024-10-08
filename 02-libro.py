class Libro:
    def __init__(self, titulo: str, autor: str, anio_publicacion: int, numero_paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.numero_paginas = numero_paginas

    def mostrar_informacion(self):
        print(f'Título: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Año de publicación: {self.anio_publicacion}')
        print(f'Número de páginas: {self.numero_paginas}')

alice_in_wonderland = Libro('Alice in Wonderland', 'Lewis Carroll', 1865, 200)

alice_in_wonderland.mostrar_informacion()