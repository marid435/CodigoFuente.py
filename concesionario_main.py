from Automovil import Automovil
from moto import Moto

def main():
    # Lista polimórfica de vehículos
    vehiculos = [
        Automovil("Toyota", "Corolla", 80000, 5),
        Automovil("Mazda", "3", 75000, 4),
        Moto("Yamaha", "XTZ", 20000, 250),
        Moto("Kawasaki", "Ninja", 35000, 600)
    ]

    # Mostrar ficha de cada vehículo
    print("🧾 INVENTARIO DEL CONCESIONARIO:\n")
    total = 0
    for v in vehiculos:
        print(v.ficha())
        total += v.precio_final()

    print("\n💰 Total del inventario: $%.2f" % total)

if __name__ == "__main__":
    main()
