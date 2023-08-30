class NumerosArray:
    def __init__(self):
        self.numeros = []

    def mostrar_numeros(self):
        if self.numeros:
            print("Números almacenados:", self.numeros)
        else:
            print("No hay números almacenados.")

    def agregar_numero(self, numero):
        self.numeros.append(numero)
        print(f"Se añadió el número {numero}.")

    def eliminar_numero(self, numero):
        if numero in self.numeros:
            self.numeros.remove(numero)
            print(f"Se eliminó el número {numero}.")
        else:
            print(f"El número {numero} no está en la lista.")

# Crear una instancia de la clase
numeros_array = NumerosArray()

while True:
    print("\n1. Mostrar números")
    print("2. Agregar número")
    print("3. Eliminar número")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == '1':
        numeros_array.mostrar_numeros()
    elif opcion == '2':
        numero = int(input("Ingresa el número que deseas añadir: "))
        numeros_array.agregar_numero(numero)
    elif opcion == '3':
        numero = int(input("Ingresa el número que deseas eliminar: "))
        numeros_array.eliminar_numero(numero)
    elif opcion == '4':
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Elige una opción válida.")
