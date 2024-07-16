import os
from cryptography.fernet import Fernet
import base64

# Archivo donde se almacenará la clave
KEY_FILE = "secret.key"

def load_key():
    """Carga la clave desde el archivo KEY_FILE. Retorna None si el archivo no existe o no se puede leer."""
    try:
        if os.path.exists(KEY_FILE):
            with open(KEY_FILE, "rb") as key_file:
                return key_file.read()
    except IOError as e:
        print(f"Error al leer el archivo de clave: {e}")
    return None

def generate_and_save_key():
    """Genera una nueva clave y la guarda en KEY_FILE. Retorna la clave generada."""
    try:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        return key
    except IOError as e:
        print(f"Error al guardar el archivo de clave: {e}")
        raise

# Cargar la clave existente o generar una nueva
key = load_key()
if key is None:
    key = generate_and_save_key()

cipher_suite = Fernet(key)

def encrypt_message(message):
    """Cifra un mensaje usando Fernet y lo codifica en Base64."""
    try:
        cipher_text = cipher_suite.encrypt(message.encode())
        return base64.urlsafe_b64encode(cipher_text).decode()
    except Exception as e:
        print(f"Error al cifrar el mensaje: {e}")
        raise

def decrypt_message(cipher_text):
    """Descifra un mensaje cifrado usando Fernet, que está codificado en Base64."""
    try:
        decoded_cipher_text = base64.urlsafe_b64decode(cipher_text)
        decrypted_message = cipher_suite.decrypt(decoded_cipher_text).decode()
        return decrypted_message
    except Exception as e:
        print(f"Error al descifrar el mensaje: {e}")
        raise
