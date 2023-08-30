import datetime
import threading

# Lista para almacenar los temporizadores programados
temporizadores = []

def agregar_temporizador(hora):
    temporizadores.append((hora, False))
    print(f"Temporizador para {hora} ha sido agregado.")

def mostrar_temporizadores():
    print("Temporizadores programados:")
    for hora, pasado in temporizadores:
        estado = "X" if pasado else "0"
        print(f"{hora}: {estado}")

def verificar_temporizadores():
    while True:
        ahora = datetime.datetime.now().strftime("%H:%M")
        for i, (hora, pasado) in enumerate(temporizadores):
            if ahora >= hora and not pasado:
                temporizadores[i] = (hora, True)
                print(f"¡Ha pasado la hora programada para {hora}!")
        threading.Timer(60, verificar_temporizadores).start()
        break

# Iniciar el hilo de verificación de temporizadores
verificar_temporizadores()

# Menú principal
while True:
    print("\n1. Agregar temporizador")
    print("2. Mostrar temporizadores")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == '1':
        hora = input("Ingresa la hora del temporizador (HH:MM): ")
        agregar_temporizador(hora)
    elif opcion == '2':
        mostrar_temporizadores()
    elif opcion == '3':
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Elige una opción válida.")
