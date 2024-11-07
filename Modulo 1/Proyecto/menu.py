from heladeria import Heladeria
from copa import Copa
from malteada import Malteada
from base import Base
from complemento import Complemento
from funciones import *
from ingrediente import Ingrediente
from producto import Producto

def menu():
    heladeria = Heladeria()
  
    ingrediente1 = Base("exquisito", 1200, 120, 5.0, False, "chocolate")
    ingrediente2 = Base("tentacion", 900, 90, 10.5, True, "cainilla")
    ingrediente3 = Base("cremoso", 3500, 50, 7.0, False, "limon")
    ingrediente4 = Base("mezclado", 4200, 160, 18.5, True, "naranja-maracuya")
    ingrediente5 = Complemento("chips", 300, 30, 2.5, False)
    ingrediente6 = Complemento("caramelo", 700, 70, 1.5, True)
    ingrediente7 = Complemento("masmello", 1600, 200, 9.5, False)
    ingrediente8 = Complemento("galleta", 2200, 300, 10.5, True)

    heladeria.agregar_ingrediente(ingrediente1)
    heladeria.agregar_ingrediente(ingrediente2)
    heladeria.agregar_ingrediente(ingrediente3)
    heladeria.agregar_ingrediente(ingrediente4)
    heladeria.agregar_ingrediente(ingrediente5)
    heladeria.agregar_ingrediente(ingrediente6)
    heladeria.agregar_ingrediente(ingrediente7)
    heladeria.agregar_ingrediente(ingrediente8)

  
    producto1 = Copa("la deli", 5300, [ingrediente1, ingrediente6, ingrediente7], "pequeño" )
    producto2 = Copa("la de siempre", 8700, [ingrediente2, ingrediente8, ingrediente5], "mediano" )
    producto3 = Malteada("tornado", 12000, [ingrediente3, ingrediente5, ingrediente6],7  )
    producto4 = Malteada("huracan", 15800, [ingrediente4, ingrediente7, ingrediente8],8 )

    heladeria.agregar_producto(producto1)
    heladeria.agregar_producto(producto2)
    heladeria.agregar_producto(producto3)
    heladeria.agregar_producto(producto4)

    # Switch usando un diccionario
    opciones = {
        "1": heladeria.abastecer,
        "2": heladeria.renovar_inventario,
        "3": heladeria.vender,
        "4": heladeria.producto_mas_rentable,
        "5": heladeria.mostrar_ventas_dia,
        "6": heladeria.mostrar_productos,
        "7": heladeria.mostrar_ingredientes,
        "8": heladeria.es_sano,
        "9": exit
    }

    while True:
        print("\n--- Menu Heladeria ---")
        print("1. Abastecer Ingrediente")
        print("2. Renovar Complemento")
        print("3. Vender Producto")
        print("4. Mostrar Producto más Rentable")
        print("5. Mostrar Ventas del Día")
        print("6. Mostrar Productos")
        print("7. Mostrar Ingredientes")
        print("8. Validar si es sano un ingrediente")
        print("9. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opcion no valida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
    