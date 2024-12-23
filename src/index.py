import socket
import os

host = os.environ.get('HOST', '127.0.0.1')
port = int(os.environ.get('PORT', 80))

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
serversocket.listen(5)

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        print(buf)
        connection.sendall(buf)
