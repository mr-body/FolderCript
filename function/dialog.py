import tkinter as tk
from tkinter import filedialog
import os

def convert_size(size_bytes):
    if size_bytes >= 1099511627776:
        size = round(size_bytes / 1099511627776, 2)
        unit = "TB"
    elif size_bytes >= 1073741824:
        size = round(size_bytes / 1073741824, 2)
        unit = "GB"
    elif size_bytes >= 1048576:
        size = round(size_bytes / 1048576, 2)
        unit = "MB"
    else:
        size = round(size_bytes / 1024, 2)
        unit = "KB"

    return size, unit

def get_folder_info(folder_path):
    folder_name = os.path.basename(folder_path)
    total_size = 0
    num_folders = 0
    num_items = 0

    for root, dirs, files in os.walk(folder_path):
        total_size += sum([os.path.getsize(os.path.join(root, file)) for file in files])
        num_folders += len(dirs)
        num_items += len(files)

    size, unit = convert_size(total_size)

    return [folder_name, folder_path, size, unit, num_folders, num_items]

def SearchFolder():
    try:
        root = tk.Tk()
        root.withdraw()

        # Obter a pasta principal do sistema
        home_folder = os.path.expanduser("~")

        # Definir a pasta principal como a pasta inicial do diálogo
        folder_path = filedialog.askdirectory(initialdir=home_folder)

        folder_info = get_folder_info(folder_path)
        return folder_info
    except Exception as e:
        print("Error:erro")
        return None

