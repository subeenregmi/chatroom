import socket 
import threading
import time

HEADERSIZE = 10 
IP = "localhost"
PORT = 3036

client = socket.socket()
client.connect((IP, PORT))

def sendMessage():
    while True:
        message = input("")
        client.send(message.encode("utf-8"))
        time.sleep(0.01)

def recieveMessage():
    while True:
        message = client.recv(1024).decode('utf-8')
        print(f"{message}")
  
sendMsg = threading.Thread(target=sendMessage)
sendMsg.start()

recieveMsg = threading.Thread(target=recieveMessage)
recieveMsg.start()

