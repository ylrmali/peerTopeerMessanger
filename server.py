import socket


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('192.168.11.214', 5555))
serv.listen(5)
while True:
  conn, addr = serv.accept()
  from_client = ''
  while True:
    data = conn.recv(1024)
    if not data: break
    from_client += data.decode('utf8')
    print (from_client) 
  conn.close()
print ('client disconnected and shutdown')