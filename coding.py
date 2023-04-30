import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from PyQt5 import QtWidgets
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import logging


class Coding:
    def __init__(self, size: int) -> None:
        self.size = size
        self.settings = {
            'initial_file': 'text.txt',
            'encrypted_file': os.path.join("text", 'encrypted_file.txt'),
            'decrypted_file': os.path.join("text", 'decrypted_file.txt'),
            'symmetric_key': os.path.join("key", 'symmetric_key.txt'),
            'public_key': os.path.join("key", 'public_key.txt'),
            'private_key': os.path.join("key", 'private_key.txt'),
            # 'encrypted_vector': os.path.join(self.way, 'encrypted_vector.txt')
        }

    def generation_key(self):

        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        private_key = keys
        public_key = keys.public_key()

        try:
            with open(self.settings['public_key'], 'wb') as public_out:
                public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                         format=serialization.PublicFormat.SubjectPublicKeyInfo))
        except:
            logging.error(f"error in file")
            #print('path of public key is not found')

        try:
            with open(self.settings['private_key'], 'wb') as private_out:
                private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                            format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                            encryption_algorithm=serialization.NoEncryption()))
        except:
            logging.error(f"error in file")

        symmetric_key = os.urandom(16)
        ciphertext = public_key.encrypt(symmetric_key, padding.OAEP(mgf=padding.MGF1(
            algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
        try:
            with open(self.settings['symmetric_key'], "wb") as f:
                f.write(ciphertext)
        except FileNotFoundError:
            logging.error(f"error in file")


def encryption(self):
    try:
        with open(self.settings['private_key'], "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(), password=None)
    except FileExistsError:
        print(f"{self.settings['private_key']} not found")

    try:
        with open(self.settings['symmetric_key'], "rb") as f:
            encrypted_symmetric_key = f.read()
        symmetric_key = private_key.decrypt(encrypted_symmetric_key, padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    except FileNotFoundError:
        print.error(f"{self.settings['symmetric_key']} not found")
    # случайное значение для инициализации блочного режима, должно быть размером с блок и каждый раз новым
    iv = os.urandom(16)
    cipher = Cipher(algorithms.TripleDES(symmetric_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
   # c_text = sym_padding.PKCS7(128).padder()
    c_text = encryptor.update(padded_text) + encryptor.finalize()
   