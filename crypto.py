from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

input_string = "asdsadsadsad".rjust(32).encode()
key = b'fidauth123456789'

cipher = AES.new(key, AES.MODE_ECB)
encrypted_string = cipher.encrypt(pad(input_string, AES.block_size))

decrypted_string = unpad(cipher.decrypt(encrypted_string), AES.block_size)
print(encrypted_string)
print("Original string: ", input_string.decode())
print("Decrypted string: ", decrypted_string.decode())