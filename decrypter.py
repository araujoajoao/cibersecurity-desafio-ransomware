import os
from cryptography.fernet import Fernet

# Carrega a chave existente
def load_key():
    return open("key.key", "rb").read()

# Descriptografa todos os arquivos no diretório alvo
def decrypt_files(key, target_dir="test_files"):
    fernet = Fernet(key)
    for root, _, files in os.walk(target_dir):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                encrypted_data = f.read()
            decrypted_data = fernet.decrypt(encrypted_data)
            with open(file_path, "wb") as f:
                f.write(decrypted_data)
    print(f"Arquivos no diretório '{target_dir}' foram descriptografados.")

if __name__ == "__main__":
    # Carrega a chave
    key = load_key()

    # Descriptografa os arquivos
    decrypt_files(key)
