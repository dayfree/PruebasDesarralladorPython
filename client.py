import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))
    print("Conectado al servidor TCP en localhost:5000")

    while True:
        message = input("Ingrese el mensaje para enviar al servidor (o 'DESCONEXION' para salir): ")
        client_socket.send(message.encode())

        if message == "DESCONEXION":
            print("Cerrando conexión con el servidor...")
            client_socket.close()
            break

        response = client_socket.recv(1024).decode()
        print(f"Respuesta del servidor: {response}")

if __name__ == "__main__":
    start_client()
