import socket


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'fidauth123456789'

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('192.168.11.214', 5555))
serv.listen(5)
while True:
  conn, addr = serv.accept()
  from_client = ''
  while True:
    data = conn.recv(1024)
    if not data: break
    print(data)
    # from_client += data.decode('utf8')
    from_client += data
    print (from_client) 

    msg = input('message: ').rjust(32).encode()
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_string = cipher.encrypt(pad(msg, AES.block_size))
    decrypted_string = unpad(cipher.decrypt(encrypted_string), AES.block_size)

    

    conn.send(encrypted_string)
  conn.close()
print ('client disconnected and shutdown')