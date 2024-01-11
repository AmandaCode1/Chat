import socket

HOST = ""
PORT = 5055

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #crea objeto sevidor socket

servidor.bind((HOST,PORT))  
servidor.listen()
conexion,direccion = servidor.accept()


#rec = servidor.accept()
#conexion = rec[0]
#direccion = rec[1]

while True:
    print("Mensaje")
    mensaje = conexion.recv(2000)
    if not mensaje:
        break;
    print(f'Mensaje: {mensaje.decode()}')