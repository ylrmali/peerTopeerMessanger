import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


IP = input('what is the IP: ')
HOST = int(input('what is the host: '))
key = b'fidauth123456789'


while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, HOST))

    MSG = input("what is your message(for quit 'q'): ").rjust(32).encode()
    if MSG == 'q':
        client.close()
        break
    else:
        try:
            cipher = AES.new(key, AES.MODE_ECB)
            encrypted_string = cipher.encrypt(pad(MSG, AES.block_size))
            decrypted_string = unpad(cipher.decrypt(encrypted_string), AES.block_size)
            client.send(encrypted_string)

            from_server = client.recv(1024)
            print (from_server.decode())
            client.close()
        except OSError as error:
            print(error)
# client.close()
