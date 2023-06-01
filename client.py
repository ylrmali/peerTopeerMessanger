import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.11.202', 5555))
client.send("selaaammmm -ali\n".encode())
from_server = client.recv(1024)
client.close()
print (from_server.decode())