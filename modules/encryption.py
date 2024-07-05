from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
import binascii

import os

import json


class Encryption:
    @staticmethod
    def encrypt_string(plain_text, key, iv):
        try:
            plain_text = pad(plain_text, 16)

            aes_instance = AES.new(key, AES.MODE_CBC, iv)

            raw_out = aes_instance.encrypt(plain_text)

            return binascii.hexlify(raw_out)
        except:
            print("ERROR - ENCRYPT")
            os._exit(1)
    @staticmethod
    def decrypt_string(cipher_text, key, iv):
        try:
            cipher_text = binascii.unhexlify(cipher_text)

            aes_instance = AES.new(key, AES.MODE_CBC, iv)

            cipher_text = aes_instance.decrypt(cipher_text)

            return unpad(cipher_text, 16)
        except:
            print("ERROR - ENCRYPT")
            os._exit(1)

    @staticmethod
    def encrypt(message, enc_key, iv):
        try:
            _key = SHA256.new(enc_key.encode()).hexdigest()[:32]

            _iv = SHA256.new(iv.encode()).hexdigest()[:16]

            return Encryption.encrypt_string(message.encode(), _key.encode(), _iv.encode()).decode()
        except:
            print("ERROR - Encrypt")
            os._exit(1)

    @staticmethod
    def decrypt(message, enc_key, iv):
        try:
            _key = SHA256.new(enc_key.encode()).hexdigest()[:32]

            _iv = SHA256.new(iv.encode()).hexdigest()[:16]

            return json.loads(Encryption.decrypt_string(message.encode(), _key.encode(), _iv.encode()).decode())
        except:
            print("ERROR - Decrypt")
            os._exit(1)
