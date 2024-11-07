from copa import Copa
from base import Base
from complemento import Complemento
from ingrediente import Ingrediente

class Heladeria:
    def __init__(self):
        self.productos = []  # Lista de productos
        self.ingredientes = []  # Lista de ingredientes
        self.ventas_dia = 0

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)
        print(f"Ingrediente {ingrediente.nombre} agregado correctamente.")

    def agregar_producto(self, producto):
        if len(self.productos) < 4:
            self.productos.append(producto)
            print(f"Producto {producto.nombre} agregado correctamente.")
        else:
            print("Ya hay 4 productos, no se puede agregar más.")

    def producto_mas_rentable(self):
        mas_rentable = max(self.productos, key=lambda producto: producto.calcular_rentabilidad()).nombre
        print(f"El producto más rentable es: {mas_rentable}")

    def vender(self):
        Heladeria.mostrar_productos(self)
        nombre_producto = input("Nombre del producto a vender: ").lower()

        producto = next((p for p in self.productos if p.nombre == nombre_producto), None)
        if producto:
            # Verificar si hay suficientes ingredientes
            for ingrediente in producto.ingredientes:
                if ingrediente.inventario < 1:
                    print(f"No hay suficiente {ingrediente.nombre} para hacer el producto.")
                    return False  # No se puede vender si no hay suficientes ingredientes
            # Actualizar inventario y sumar ventas
            for ingrediente in producto.ingredientes:
                ingrediente.inventario -= 1
            self.ventas_dia += producto.precio_publico
            print(f"Producto {nombre_producto} vendido correctamente.")
            return True
        print(f"Producto {nombre_producto} no encontrado.")
        return False

    def mostrar_ventas_dia(self):
        print(f"Las ventas del día son: ${self.ventas_dia}")
   
    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos disponibles.")
            return
        print("\n--- Productos Disponibles ---")
        for producto in self.productos:
            tipo_producto = "Copa" if isinstance(producto, Copa) else "Malteada"

            if tipo_producto == "Copa":
                print(f"Nombre: {producto.nombre} | Tipo: {tipo_producto} | Precio al Público: {producto.precio_publico} | Tipo de Vaso: {producto.tipo_vaso} | Costo Produccion: {producto.calcular_costo()} | Calorias Totales: {producto.calcular_calorias()} | Rentabilidad: {producto.calcular_rentabilidad()}")
            else:
                print(f"Nombre: {producto.nombre} | Tipo: {tipo_producto} | Precio al Público: {producto.precio_publico} | Volumen: {producto.volumen} oz | Costo Produccion: {producto.calcular_costo()} | Calorias Totales: {producto.calcular_calorias()} | Rentabilidad: {producto.calcular_rentabilidad()}")

            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    def mostrar_ingredientes(self):
        if not self.ingredientes:
            print("No hay ingredientes disponibles.")
            return

        print("\n--- Ingredientes Disponibles ---")
        for ingrediente in self.ingredientes:
            tipo_ingrediente = "Base" if isinstance(ingrediente, Base) else "Complemento"

            if tipo_ingrediente == "Base":
                print(f" - Nombre: {ingrediente.nombre}, Tipo: {tipo_ingrediente}, (Calorías: {ingrediente.calorias}, Precio: {ingrediente.precio}, Calorías: {ingrediente.calorias}, Inventario: {ingrediente.inventario}, Es Vegetariano: {ingrediente.es_vegetariano}, Sabor: {ingrediente.sabor}")
            else:
                print(f" - Nombre: {ingrediente.nombre}, Tipo: {tipo_ingrediente}, (Calorías: {ingrediente.calorias}, Precio: {ingrediente.precio}, Calorías: {ingrediente.calorias}, Inventario: {ingrediente.inventario}, Es Vegetariano: {ingrediente.es_vegetariano}")
          

            print("-------------------------------------------------------------------------------------------------------------------------------------------------")

    def abastecer(self):
        Heladeria.mostrar_ingredientes(self)
        nombre_ingrediente = input("Nombre del ingrediente abastecer: ").lower()
        ingrediente = next((i for i in self.ingredientes if isinstance(i, Ingrediente) and i.nombre == nombre_ingrediente), None)
        if ingrediente:
                ingrediente.abastecer() 
                print(f"----------------------------------------------------------------------------------")
                print(f"Se Abastecio el {ingrediente.nombre}, Nuevo inventario: {ingrediente.inventario}")
                print(f"----------------------------------------------------------------------------------")
        else:
                print(f"No se encontró la base con nombre '{nombre_ingrediente}'.")
      
    def renovar_inventario(self):
        for ingrediente in self.ingredientes:
            tipo_ingrediente = "Complemento" if isinstance(ingrediente, Complemento) else "Base"

            if tipo_ingrediente == "Complemento":
                print(f" - Nombre: {ingrediente.nombre}, Inventario: {ingrediente.inventario}")
                print("-----------------------------------------------")

        nombre_producto = input("Nombre del complemento a renovar inventario: ").lower()
        ingrediente = next((i for i in self.ingredientes if isinstance(i, Complemento) and i.nombre == nombre_producto), None)
        if ingrediente:
            ingrediente.renovar_inventario()
            print(f"Se renovo el {ingrediente.nombre}, Nuevo inventario: {ingrediente.inventario}")
        else:
            print("No existe ingrediente")

    def es_sano(self):
        Heladeria.mostrar_ingredientes(self)
        nombre_sano = input("Nombre del ingrediente para validar si es sano: ").lower()
        ingrediente = next((i for i in self.ingredientes if isinstance(i, Ingrediente) and i.nombre == nombre_sano), None)
        if ingrediente:
            print(f"El ingrediente {ingrediente.nombre} es sano? {ingrediente.es_sano()}")
        else:
            print("No existe ingrediente")