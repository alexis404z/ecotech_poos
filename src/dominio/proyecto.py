class proyecto:
    def __init__ (self,nombre:str):
        self.nombre = nombre

    def mostrar_nombre_proyecto(self) -> str:
        return f"{self.nombre}"