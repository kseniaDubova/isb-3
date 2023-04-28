import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
def key_couple(private_key_path: str,  public_key_path: str, symmetric_key_path: str):
        
  keys = rsa.generate_private_key(
      public_exponent=65537,
      key_size=2048
  )
  private_key = keys
  public_key = keys.public_key()

  try:
    with open(public_key_path, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo))
  except:
       print('path of public key is not found')

  try:
    with open(private_key_path, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                  format=serialization.PrivateFormat.TraditionalOpenSSL,
                  encryption_algorithm=serialization.NoEncryption()))
  except:
      print('path of private key is not found')
        
  symmetric_key = os.urandom(16)
  ciphertext = public_key.encrypt(symmetric_key, padding.OAEP(mgf=padding.MGF1(
      algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
  try:
      with open(symmetric_key_path, "wb") as f:
          f.write(ciphertext)
  except FileNotFoundError:
      print("path of symmetric key is not found")

def encryption(initial_file_path: str, private_key_path: str, encrypted_symmetric_key_path: str, encrypted_file_path: str):
  try:
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(), password=None)
  except FileExistsError:
    print(f"{private_key_path} not found")
  try:
    with open(encrypted_symmetric_key_path, "rb") as f:
        encrypted_symmetric_key = f.read()
    symmetric_key = private_key.decrypt(encrypted_symmetric_key, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
  except FileNotFoundError:
    print.error(f"{encrypted_file_path} not found")
  iv = os.urandom(16) #случайное значение для инициализации блочного режима, должно быть размером с блок и каждый раз новым
  cipher = Cipher(algorithms.TripleDES(symmetric_key), modes.CBC(iv))
  encryptor = cipher.encryptor()
  c_text = sym_padding.PKCS7(128).padder()
  #c_text = encryptor.update(padded_text) + encryptor.finalize()

  print(c_text)