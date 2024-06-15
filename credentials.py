import os
import cryptography
import json

from cryptography.fernet import Fernet


def get_key(page):
    if page.client_storage.get("key") is None:
        key = Fernet.generate_key()
        page.client_storage.set("key", key.decode())
    else:
        key = bytes(page.client_storage.get("key"), 'utf-8')
    return Fernet(key)

def get_credentials(page):
    cipher_suite = get_key(page)

    if page.client_storage.get("credentials") is None:
        credentials = {
            "user": "",
            "password": ""
        }
    else:
        cipher_text = bytes(page.client_storage.get("credentials"), 'utf-8')
        credentials = json.loads(cipher_suite.decrypt(cipher_text))
    return credentials

def save_credentials(page, usr_credentials):
    cipher_text = get_key(page).encrypt(json.dumps(usr_credentials).encode())
    page.client_storage.set("credentials", cipher_text.decodee())
