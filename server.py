import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(5)
    print("Servidor TCP escuchando en el puerto 5000...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Cliente conectado desde {client_address}")

        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            print(f"Mensaje recibido del cliente: {message}")

            if message == "DESCONEXION":
                print("Desconectando cliente...")
                client_socket.close()
                break


            response = message.upper()
            client_socket.send(response.encode())

if __name__ == "__main__":
    start_server()
