import os
from cryptography.fernet import Fernet
import os

def generate_key(key_file):
    key = Fernet.generate_key()
    with open(key_file, "w") as f:
        f.write(key.decode())
