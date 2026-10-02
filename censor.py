from cryptography.fernet import Fernet
import json

with open('censorship.dat', 'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()

fernet = Fernet('xpplx11wZUibz0E8tV8Z9mf-wwggzSrc21uQ17Qq2gg=')

decrypted_data = fernet.decrypt(encrypted_data)

MODERATION_CONFIG = json.loads(decrypted_data)

print(json.dumps(MODERATION_CONFIG, indent=4))