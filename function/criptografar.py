import pyAesCrypt
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
import getpass
import os

def remove_password_for_folder(encrypted_folder_path, password):
    buffer_size = 64 * 1024
    decrypted_folder_path = os.path.splitext(encrypted_folder_path)[0]
    # Desencriptar todos os arquivos no diretório
    for subdir, _, files in os.walk(decrypted_folder_path):
        for file in files:
            file_path = os.path.join(subdir, file)
            decrypted_file_path = os.path.splitext(file_path)[0]
            pyAesCrypt.decryptFile(
                file_path,
                decrypted_file_path,
                password,
                buffer_size
            )
            os.remove(file_path)
            print(f"Arquivo {file} Descriptografado com sucesso")