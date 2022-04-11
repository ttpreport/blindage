from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import urandom
from hashlib import pbkdf2_hmac
from random import choice
from string import ascii_lowercase
from io import StringIO


class BlindageAESEncoder:
    interface_handler = None
    key = bytes()

    def __init__(self, interface_handler):
        self.interface_handler = interface_handler
        self.key = ''.join(choice(ascii_lowercase) for _ in range(32))

    def encode(self, data):
        self.interface_handler.print_good("Starting AES encoder...")
        encoded_data = b64encode(self._encrypt(self.key, data)).decode()
        return "printf {0} | base64 -d | openssl aes-256-cbc -pbkdf2 -d -k {1} | sh".format(encoded_data, self.key)

    def _encrypt(self, password, data):
        data_stream = StringIO(data)
        bs = AES.block_size
        salt = urandom(bs - len(b'Salted__'))
        pbk = pbkdf2_hmac('sha256', password.encode('utf8'), salt, 10000, 48)
        key = pbk[:32]
        iv = pbk[32:48]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        result = (b'Salted__' + salt)
        finished = False
        while not finished:
            chunk = data_stream.read(1024 * bs).encode()
            if len(chunk) == 0 or len(chunk) % bs != 0:
                padding_length = (bs - len(chunk) % bs) or bs
                chunk += (padding_length * chr(padding_length)).encode()
                finished = True
            result += cipher.encrypt(chunk)
        return result

    def __str__(self):
        return 'AES encoder'
