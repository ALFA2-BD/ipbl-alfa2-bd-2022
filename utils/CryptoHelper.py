from cryptography.fernet import Fernet
import secrets

class CryptoHelper:
    def __init__(self) -> None:
        super().__init__()

    def generate_key_to_file(self):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

    def load_key(self):
        return open("secret.key", "rb").read()

    def encrypt_message(self, message):
        key = self.load_key()
        encoded_message = message.encode()
        f = Fernet(key)
        encrypted_message = f.encrypt(encoded_message)

        return encrypted_message.decode()

    def decrypt_message(self, encrypted_message):
        key = self.load_key()
        f = Fernet(key)
        if str(type(encrypted_message)) == "<class 'str'>":
            decrypted_message = f.decrypt(encrypted_message.encode())
        elif str(type(encrypted_message)) == "<class 'bytes'>":
            decrypted_message = f.decrypt(encrypted_message)

        return decrypted_message.decode()