from Vehiculo import Vehiculo

# Automovil hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, precio_base: float, puertas: int):
        super().__init__(marca, modelo, precio_base)
        self._puertas = puertas
    
    @property
    def puertas(self):
        return self._puertas
    
    def impuesto(self) -> float:
        # 8% del precio base; si tiene 5 puertas, restar 1%
        impuesto_base = self.precio_base * 0.08
        
        if self.puertas == 5:
            descuento = self.precio_base * 0.01
            return impuesto_base - descuento
        
        return impuesto_base
    
    def ficha(self) -> str:
        return f"{super().ficha()} - {self.puertas} puertas"
