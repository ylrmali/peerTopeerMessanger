import socket
import json
from datetime import datetime

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'fidauth123456789'
ip = open('data.txt', 'a+')
msg = open('msg.txt', 'a+')
json_data = open('json_data.txt', 'a+')

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('192.168.11.214', 5555))
serv.listen(5)
while True:
  conn, addr = serv.accept()
  from_client = ''
  while True:
    data = conn.recv(1024)
    if not data: break
    print(addr[0])
    ''' create block in txt '''
    block = {
      '1' : {
        'ip': addr[0],
        'msg': [str(data)],
        'time': str(datetime.now())
      }
    }

    with open('json_data.txt', 'a+') as json_file:
      json.dump(block, json_file)


    ''' add ip in txt '''
    ip.writelines(f'\n{addr[0]}')
    ip.close()
    ''' add message in txt '''
    msg.writelines(f'\n{data}')
    msg.close()
    # from_client += data.decode('utf8')
    # from_client += data
    print (data) 

    msg = input('message: ').rjust(32).encode()
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_string = cipher.encrypt(pad(msg, AES.block_size))
    decrypted_string = unpad(cipher.decrypt(encrypted_string), AES.block_size)

    

    conn.send(encrypted_string)
  conn.close()
print ('client disconnected and shutdown')