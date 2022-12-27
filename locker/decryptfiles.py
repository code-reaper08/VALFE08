import os
from cryptography.fernet import Fernet

def decrypt_all_files(encrypted_filepath, key_filepath, decrypted_filepath):
    with open(key_filepath, "r") as kf:
        key = kf.read()
        fernet = Fernet(key.encode())
        with open(encrypted_filepath, "r") as f:
            data = f.read()
            decrypted_text = fernet.decrypt(data.encode())

            with open(decrypted_filepath, "w", encoding='cp437') as df:
                df.write(decrypted_text.decode())
    # os.remove(encrypted_filepath)