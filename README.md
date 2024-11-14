# Ejercicio: Implementación de Servidor y Cliente TCP en Python

Este ejercicio implementa un servidor y un cliente TCP que se comunican entre sí en la misma máquina usando el puerto `5000`.

## Instrucciones de Ejecución

1. **Ejecutar el Servidor:**
   - Abre una terminal.
   - Navega hasta el directorio donde se encuentra el archivo `server.py`.
   - Ejecuta el servidor con el siguiente comando:
     ```bash
     python server.py
     ```
   - El servidor estará escuchando conexiones en `localhost:5000`.

2. **Ejecutar el Cliente:**
   - Abre una segunda terminal.
   - Navega hasta el directorio donde se encuentra el archivo `client.py`.
   - Ejecuta el cliente con el siguiente comando:
     ```bash
     python client.py
     ```
   - El cliente intentará conectarse al servidor en `localhost:5000`.

## Pruebas Manuales

1. **Prueba de Mensaje Normal:**
   - En el cliente, ingrese un mensaje de texto cualquiera, como `hola servidor`.
   - El servidor debe responder con el mensaje en mayúsculas, por ejemplo: `HOLA SERVIDOR`.

2. **Prueba de Desconexión:**
   - En el cliente, ingrese el mensaje `DESCONEXION`.
   - El cliente enviará este mensaje al servidor, y la conexión se cerrará en ambos lados.
   - El servidor permanecerá disponible para recibir nuevas conexiones de otros clientes.

