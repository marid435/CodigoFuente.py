from Vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, precio_base: float, cc: int):
        super().__init__(marca, modelo, precio_base)
        self._cc = cc
    
    @property
    def cc(self):
        return self._cc
    
    def impuesto(self) -> float:
        # Si cc ≤ 250 → 5% del precio base; si cc > 250 → 9%
        if self.cc <= 250:
            return self.precio_base * 0.05
        else:
            return self.precio_base * 0.09
    
    def ficha(self) -> str:
        return f"{super().ficha()} - {self.cc}cc"