import socket
import os

host = os.environ.get('HOST', '127.0.0.1')
port = int(os.environ.get('PORT', 80))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

while 1:
    data = client_socket.recv(512)
    if ( data == 'q' or data == 'Q'):
        client_socket.close()
        break;
    else:
        print "RECIEVED:" , data
        data = raw_input ( "SEND( TYPE q or Q to Quit):" )
        if (data <> 'Q' and data <> 'q'):
            client_socket.send(data)
        else:
            client_socket.send(data)
            client_socket.close()
            break;
