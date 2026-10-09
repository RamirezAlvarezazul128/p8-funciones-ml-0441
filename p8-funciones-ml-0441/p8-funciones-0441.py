# Ramirez Azul NC 0441 NL 48

print("----Ejemplo 1----")
def suma(a, b):
    return a + b

resultado = suma(4, 5)
print(resultado)  # Salida: 9

print("----Ejemplo 2----")
def saludar(nombre):
    mensaje = f"Hola, {nombre}!"  # Código indentado
    print(mensaje)
    # ❌ Código incorrecto: Sin indentado
def suma(a, b):
  print("a + b")  # Error: IndentationError

# ✅ Código correcto: Con indentado
def suma(a, b):
    print(a + b)  # Correcto: El código está indentado

    print("----Ejemplo 3----")
def calcular_area_rectangulo(base, altura):
    area = base * altura  # Calcula el área
    return area           # Devuelve el resultado

# Llamada a la función
resultado = calcular_area_rectangulo(10, 5)
print(f"El área del rectángulo es: {resultado}")
      
print("----Ejemplo 4----")

def Suma(num1=2, num2=3):
    return num1 + num2

# Al no especificar argumentos, toma los valores por defecto (2 y 3)
resultado = Suma()
print(resultado)

print("----Ejemplo 5----")
# Definición de la función con PARÁMETROS
def calcular_area(base, altura):
    return base * altura

# Llamada a la función con ARGUMENTOS
area = calcular_area(5, 3)  # Argumentos: base=5, altura=3
print(f"El área del rectángulo es: {area}")  # Salida: El área del rectángulo es: 15


print("Ramirez Azul NC 0441 NL 48")

