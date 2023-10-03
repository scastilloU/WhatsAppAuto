print("Este es un ejercicio de estructuras de datos simples en python")


nombre = "Juan"  # La variable "nombre" almacena una cadena de texto.
edad = 30        # La variable "edad" almacena un número entero.
precio = 19.99
numero_texto = "42"
numero = int(numero_texto)  # Convierte la cadena en un número entero


print("------------------if -------------------------------")


edad = 18
if edad >= 18:
    print("Eres mayor de edad.")

print("----------------if else---------------------------------")


edad = 15
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


print("----------------------IF else agrupado ---------------------------")


puntaje = 85
if puntaje >= 90:
    print("Aprobaste con A.")
elif puntaje >= 80:
    print("Aprobaste con B.")
elif puntaje >= 70:
    print("Aprobaste con C.")
else:
    print("No aprobaste.")



print("------------------- while y for ------------------------------")


contador = 1999999
valor =  contador
print(valor)
while contador <= 5:
    print(contador)
    contador += 1

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)



def saludar(nombre):
    print("Hola, " + nombre + "!")

saludar(nombre)


def suma(a, b,e):
    resultado = a + b + e
    return print("El resultado es "+str(resultado))
suma(10,25,5)



