
from modulo import calcularCuadrado

def main():

    try:
        
        lado = float(input("Ingrese la longitud del lado del cuadrado: "))

        if lado <= 0:
            print("El valor del lado debe ser un número positivo.")
        else:
            areaSombreada = calcularCuadrado(lado)

            print(f"El área de la región sombreada es: {areaSombreada}")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")

if __name__ == "__main__":
    main()