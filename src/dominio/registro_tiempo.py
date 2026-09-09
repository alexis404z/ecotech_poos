class registro_tiempo:
    def __init__ (self,fecha,hora:float):
        self.fecha = fecha
        self.hora = hora

    def registrar_fecha_y_hora(self) -> str:
       return f"{self.fecha,self.hora}"
