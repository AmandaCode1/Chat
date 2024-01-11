import socket

Host = '172.20.10.13'
Puerto = 5005

#Crear socket
clienteAmanda = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clienteAmanda:
clienteAmanda.connect((Host,Puerto)) #Nos conectamos al servidor
while True:
    mensaje = input('Introduce un mensaje:')
    clienteAmanda.sendall(mensaje.encode())