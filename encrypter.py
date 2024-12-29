import os
from cryptography.fernet import Fernet

# Gera uma chave e salva em um arquivo
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

# Carrega a chave existente
def load_key():
    return open("key.key", "rb").read()

# Criptografa todos os arquivos no diretório alvo
def encrypt_files(key, target_dir="test_files"):
    fernet = Fernet(key)
    for root, _, files in os.walk(target_dir):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                data = f.read()
            encrypted_data = fernet.encrypt(data)
            with open(file_path, "wb") as f:
                f.write(encrypted_data)
    print(f"Arquivos no diretório '{target_dir}' foram criptografados.")

if __name__ == "__main__":
    # Gera ou carrega a chave
    if not os.path.exists("key.key"):
        print("Gerando chave...")
        key = generate_key()
    else:
        print("Carregando chave existente...")
        key = load_key()

    # Criptografa os arquivos
    encrypt_files(key)
