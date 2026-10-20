
import os
from cryptography.fernet import Fernet

# Генерация ключа
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Шифрование файла
with open('call.txt', 'rb') as f:
    file_data = f.read()

encrypted_data = cipher_suite.encrypt(file_data)

with open('call.txt.enc', 'wb') as f:
    f.write(encrypted_data)


# Удаление оригинального файла 
if os.path.exists('call.txt') and os.path.exists('call.txt.enc'):
    os.remove('call.txt')
    print("Файл 'call.txt' зашифрован и безопасно удален.")
