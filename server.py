import socket 
import threading

HEADERSIZE = 10 
IP = "localhost"
PORT = 3036

clients = []
nicknames = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(3)

def handleClient(client_socket, client_address):

    while True:
        message = client_socket.recv(1024).decode('utf-8')
        relayMessage(message, client_address)
        print(f"{client_address}: {message}")


def relayMessage(message, message_sender):
    message = f"{message_sender}: {message}"
    for c in clients:
        if c.getpeername() == message_sender:
            pass
        else:
            c.send(message.encode('utf-8'))

while True:

        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}!")
        clients.append(client_socket)
        clientThread = threading.Thread(target=handleClient, args=(client_socket, client_address))
        clientThread.start()

