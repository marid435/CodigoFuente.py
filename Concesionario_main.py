from Automovil import Automovil
from Moto import Moto


def main():
    # Crear lista de Vehiculo (polimorfismo)
    vehiculos = [
        Automovil("Toyota", "Yaris", 40000, 5),
        Automovil("Mazda", "Civic", 25000, 4),
        Moto("Honda", "MT-03", 20000,  190),
        Moto("BMW", "CBR125", 34000, 350)
    ]
    
    # Recorrer la lista e imprimir cada vehículo
    print("=== INVENTARIO DEL CONCESIONARIO ===")
    total_inventario = 0
    
    for vehiculo in vehiculos:
        print(vehiculo)
        total_inventario += vehiculo.precio_final()
    
    print(f"\nTOTAL DEL INVENTARIO: ${total_inventario:.2f}")
    
    # Demostración adicional de polimorfismo
    print("\n=== FICHAS DETALLADAS ===")
    for vehiculo in vehiculos:
        print(f"Ficha: {vehiculo.ficha()}")
        print(f"Precio base: ${vehiculo.precio_base:.2f}")
        print(f"Impuesto: ${vehiculo.impuesto():.2f}")
        print(f"Precio final: ${vehiculo.precio_final():.2f}")
        print("-" * 40)

if __name__ == "__main__":
    main()
