
def vigenere_encrypt(text, key):
    encrypted_text = ""
    key_index = 0
    key = key.lower()

    english = "abcdefghijklmnopqrstuvwxyz"
    russian = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    for char in text:
        lower_char = char.lower()

        if lower_char in english:
            alphabet = english
        elif lower_char in russian:
            alphabet = russian
        else:
            encrypted_text += char
            continue

        key_char = key[key_index % len(key)]

        if key_char in english:
            shift = english.index(key_char)
        elif key_char in russian:
            shift = russian.index(key_char)
        else:
            shift = 0

        shift = shift % len(alphabet)

        position = alphabet.index(lower_char)
        encrypted_position = (position + shift) % len(alphabet)
        encrypted_char = alphabet[encrypted_position]

        if char.isupper():
            encrypted_char = encrypted_char.upper()

        encrypted_text += encrypted_char
        key_index += 1

    return encrypted_text


def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_index = 0
    key = key.lower()

    english = "abcdefghijklmnopqrstuvwxyz"
    russian = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    for char in encrypted_text:
        lower_char = char.lower()

        if lower_char in english:
            alphabet = english
        elif lower_char in russian:
            alphabet = russian
        else:
            decrypted_text += char
            continue

        key_char = key[key_index % len(key)]

        if key_char in english:
            shift = english.index(key_char)
        elif key_char in russian:
            shift = russian.index(key_char)
        else:
            shift = 0

        shift = shift % len(alphabet)

        position = alphabet.index(lower_char)
        decrypted_position = (position - shift) % len(alphabet)
        decrypted_char = alphabet[decrypted_position]

        if char.isupper():
            decrypted_char = decrypted_char.upper()

        decrypted_text += decrypted_char
        key_index += 1

    return decrypted_text


print("Шифр Виженера")
print("1 — Зашифровать")
print("2 — Расшифровать")

choice = input("Выберите действие: ")
text = input("Введите текст: ")
key = input("Введите ключ: ")

key = "".join(
    char.lower() for char in key
    if char.lower() in
    "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
)

if not key:
    print("Ошибка: ключ должен содержать хотя бы одну букву.")
elif choice == "1":
    print("Результат:", vigenere_encrypt(text, key))
elif choice == "2":
    print("Результат:", vigenere_decrypt(text, key))
else:
    print("Ошибка: выберите 1 или 2.")
