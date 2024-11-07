## Punto 1|El IMC

def imc(altura, peso):
    resultado= round(peso/(altura**2))
    if resultado<18:
        return "Su IMC es de: " + str(resultado) + " Conclusion: Bajo de Peso"
    elif resultado>25:
        return "Su IMC es de: " + str(resultado) + " Conclusion: Sobrepeso"
    else:
        return "Su IMC es de: " + str(resultado) + " Conclusion: Peso Saludable"



## Punto 2|Años Bisiestos

def bisiestos(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    else:                    
        return False



##Punto 3 | ¿Usted me divide?

def divide(num1, num2):
    
    a, b= num1, num2
    while b:
        a, b = b, a%b
    c = a
    calculo=(num1 * num2) // c
    
    resultados = []
        
    for i in range(1, 101):
            if i % calculo == 0:
                resultados.append(i)
    return(resultados) 
        


##Punto 4 | Clasificando Palabras

def contar(palabras):
    diccionario = {}
    
    for palabra in palabras:
        diccionario[palabra] = len(palabra)
    
    return diccionario

## Pruebas

##Punto 1
print("Resultado Punto 1:")
print(imc(1.70, 80))
##Punto 2
print("Resultado Punto 2:")
print(bisiestos(2020))
##Punto 3
print("Resultado Punto 3:")
print(divide(10, 3))
##Punto 4
print("Resultado Punto 4:")
print (contar(["Muchos", "años", "después", "frente", "al", "perro"]))