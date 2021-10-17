import base64
import os
from cryptography.fernet import Fernet

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = base64.urlsafe_b64encode(os.urandom(32))
iv = base64.urlsafe_b64encode(os.urandom(32))

data = 'hello'

c = Cipher(
    algorithms.AES(key), modes.CBC(iv), data
)

