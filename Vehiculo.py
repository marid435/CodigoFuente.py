from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca: str, modelo: str, precio_base: float):
        self._marca = marca
        self._modelo = modelo
        self._precio_base = max(1.0, precio_base)  # Validación precio mínimo
    
    # Getters públicos (encapsulamiento)
    @property
    def marca(self):
        return self._marca
    
    @property
    def modelo(self):
        return self._modelo
    
    @property
    def precio_base(self):
        return self._precio_base
    
    # Método abstracto (abstracción)
    @abstractmethod
    def impuesto(self) -> float:
        pass
    
    # Método concreto que usa el método abstracto
    def precio_final(self) -> float:
        return self._precio_base + self.impuesto()
    
    def ficha(self) -> str:
        return f"{self.marca} {self.modelo} (${self.precio_final():.2f})"
    
    def __str__(self) -> str:
        return f"{self.ficha()} | Final: ${self.precio_final():.2f}"