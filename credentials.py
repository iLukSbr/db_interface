import os
import cryptography
import json

from cryptography.fernet import Fernet

# Criar ou recuperar uma chave de criptografia
def get_key(page):
    if not page.client_storage.get("key"):
        key = Fernet.generate_key()
        page.client_storage.set("key", key.decode())
    else:
        key = page.client_storage.get("key").encode()
    return Fernet(key)

# Recuperar as credenciais do usuário
def get_credentials(page):
    cipher_suite = get_key(page)

    if not page.client_storage.get("credentials"):
        credentials = None
    else:
        cipher_text = page.client_storage.get("credentials").encode()
        decrypted = cipher_suite.decrypt(cipher_text)
        credentials = json.loads(decrypted)
    return credentials

# Gravar as credenciais do usuário
def save_credentials(page, usr_credentials):
    cipher_suite = get_key(page)
    cipher_json = json.dumps(usr_credentials)
    cipher_bytes = cipher_json.encode('utf-8')
    cipher_text = cipher_suite.encrypt(cipher_bytes) # Encrypt the credentials
    page.client_storage.set("credentials", cipher_text.decode())
