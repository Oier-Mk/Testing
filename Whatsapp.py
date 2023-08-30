
import requests

url = "https://graph.facebook.com/v17.0/124411164082036/messages"
headers = {
    "Authorization": "Bearer EAAJvTz8sXA8BO53h5dLl5IAvR3q7OK4QNAm3oZBmp1KQe0U8YGoFnMmgynQ3PljsvFcz6CqfwDiPGDj0JUq2f5ZCZCxivDNDyHRZCZCRLdngDnr5H13FmYMYCPhnsXZCFsv9briptbAdxRLvok9m4ZBewpmINjZBQU9nuqcUQNsOATRBzcyR3KXwdc1ewVFfT0bwL5z3JcGxkRSSSlpoRpIZD",
    "Content-Type": "application/json"
}
data = {
    "messaging_product": "whatsapp",
    "to": "",
    "type": "template",
    "template": {
        "name": "hello_world",
        "language": {
            "code": "en_US"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.text)


while True:
    print("Menú:")
    print("1. Enviar mensaje de WhatsApp")
    print("2. Salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        numero_destino = input("Introduce el número de teléfono (con código de país): ")
        mensaje = input("Introduce el mensaje a enviar: ")
        hora_envio = int(input("Introduce la hora de envío (formato 24 horas): "))
        minutos_envio = int(input("Introduce los minutos de envío: "))
        
        #kit.sendwhatmsg(numero_destino, mensaje, hora_envio, minutos_envio)
        print("Mensaje enviado!")
    elif opcion == "2":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
