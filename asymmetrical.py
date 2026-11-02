import os
import base64
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
# Генерация ключевой пары
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()
# Сохранение ключей в файлы
with open('private_key.pem', 'wb') as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))
with open('public_key.pem', 'wb') as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))
# Загрузка ключей из файлов
with open('private_key.pem', 'rb') as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )
with open('public_key.pem', 'rb') as f:
    public_key = serialization.load_pem_public_key(f.read())
# Шифрование сообщения открытым ключом
message = input("Введите сообщение: ").encode('utf-8')
encrypted_message = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Зашифрованное сообщение:", base64.b64encode(
    encrypted_message
).decode('utf-8'))
# Сохранение зашифрованного сообщения
with open('encrypted_message.txt', 'wb') as f:
    f.write(encrypted_message)
print("Зашифрованное сообщение сохранено в файл.")
# Расшифрование сообщения из файла
if os.path.exists('encrypted_message.txt'):
    with open('encrypted_message.txt', 'rb') as f:
        encrypted_message = f.read()
    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("Расшифрованное сообщение:", decrypted_message.decode('utf-8'))
else:
    print("Ошибка: файл с зашифрованным сообщением не найден.")