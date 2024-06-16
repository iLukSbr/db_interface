import os
import cryptography
import json

from cryptography.fernet import Fernet


def get_key(page):
    if page.client_storage.get("key") is None:
        key = Fernet.generate_key()
        Fernet(key)
        page.client_storage.set("key", key)
    else:
        key = page.client_storage.get("key")
    return key

def get_credentials(page):
    cipher_suite = get_key(page)

    if page.client_storage.get("credentials") is None:
        credentials = {
            "host": None,
            "user": None,
            "password": None,
            "database": None
        }
    else:
        cipher_text = page.client_storage.get("credentials")
        credentials = json.loads(cipher_suite.decrypt(cipher_text))
    return credentials

def save_credentials(page, usr_credentials):
    cipher_text = get_key(page).encrypt(json.dumps(usr_credentials))
    page.client_storage.set("credentials", cipher_text)
