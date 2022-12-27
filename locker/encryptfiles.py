import os
from cryptography.fernet import Fernet

def encrypt_all_files(source_filepath, key_filepath, output_filepath):
    with open(key_filepath, "r") as kf:
        key = kf.read()

        fernet = Fernet(key.encode())
        with open(source_filepath, "r", encoding='cp437') as f:
            data = f.read()
            token = fernet.encrypt(data.encode())

            with open(output_filepath, "w") as of:
                of.write(token.decode())

    os.remove(source_filepath)