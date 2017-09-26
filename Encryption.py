#Simple encryption code
from Crypto.Cipher import AES
from Crypto import Random
key = b'Sixteen byte key'
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)
user_Keys = input('input string to encrypt: ')
msg = iv + cipher.encrypt(b, user_Keys)
print(msg)
