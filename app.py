import eel
from function.dialog import *
from function.criptografar import *
import xml.etree.ElementTree as ET
from datetime import datetime
import traceback  # Importing traceback for error details
import os  # Import the os module for file operations

# Initialize Eel
eel.init('web')

# Expose JavaScript function to Python
@eel.expose
def javascriptSay(resposta):
    print(resposta)

# Expose Python function to JavaScript
@eel.expose
def SelectFolder():
    return SearchFolder()

# Function to encrypt files in a folder
@eel.expose
def cript(folder_path, password):
    try:
        buffer_size = 64 * 1024
        encrypted_folder_path = folder_path + ".aes"
        total_files = 0
        encrypted_files = 0

        # Count total number of files in the directory
        for subdir, _, files in os.walk(folder_path):
            total_files += len(files)

        # Encrypt all files in the directory
        for subdir, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(subdir, file)
                encrypted_file_path = os.path.join(subdir, file + ".aes")
                pyAesCrypt.encryptFile(
                    file_path,
                    encrypted_file_path,
                    password,
                    buffer_size
                )
                os.remove(file_path)
                encrypted_files += 1
                progress = int((encrypted_files / total_files) * 100)
                eel.sleep(0.1)  # Simulate the encryption process
                eel.updateName(file[:70] + "...")
                eel.updateProgress(progress)  # Notify progress to JavaScript
    except Exception as e:
        traceback.print_exc()  # Log the exception details

# Function to decrypt files in a folder
@eel.expose
def decrypt(folder_path, password):
    try:
        buffer_size = 64 * 1024
        decrypted_folder_path = folder_path.rstrip(".aes")
        total_files = 0
        decrypted_files = 0

        # Count total number of files in the directory
        for subdir, _, files in os.walk(folder_path):
            total_files += len(files)

        # Decrypt all files in the directory
        for subdir, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(subdir, file)
                decrypted_file_path = os.path.join(subdir, file.rstrip(".aes"))
                pyAesCrypt.decryptFile(
                    file_path,
                    decrypted_file_path,
                    password,
                    buffer_size
                )
                os.remove(file_path)
                decrypted_files += 1
                progress = int((decrypted_files / total_files) * 100)
                eel.sleep(0.1)  # Simulate the decryption process
                eel.updateName(file[:70] + "...")
                eel.updateProgress(progress)  # Notify progress to JavaScript
    except Exception as e:
        traceback.print_exc()  # Log the exception details

# Expose Python function to JavaScript
@eel.expose
def Criptografar(folder, password):
    cript(folder, password)

# Function to create XML file if it doesn't exist
def create_xml_file():
    root = ET.Element("data")
    tree = ET.ElementTree(root)
    tree.write("data.xml")

# Function to append data to XML file
def append_to_xml(path, password, description):
    tree = ET.parse("data.xml")
    root = tree.getroot()

    # Create new entry element
    entry = ET.Element("entry")

    # Add attributes
    if len(root) > 0:
        last_id = int(root[-1].get("id")) + 1
    else:
        last_id = 0

    entry.set("id", str(last_id))
    entry.set("date", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Add subelements
    path_elem = ET.SubElement(entry, "folder_path")
    path_elem.text = path
    password_elem = ET.SubElement(entry, "password")
    password_elem.text = password
    description_elem = ET.SubElement(entry, "description")
    description_elem.text = description

    # Append entry to root
    root.append(entry)

    # Write to file
    tree.write("data.xml")

# Expose Python function to JavaScript
@eel.expose
def save(path, password, description):
    try:
        # Create XML file if it doesn't exist
        if not os.path.exists("data.xml"):
            create_xml_file()

        # Append data to XML file
        append_to_xml(path, password, description)

        print("Data saved successfully.")
    except Exception as e:
        traceback.print_exc()  # Log the exception details
        print("Error:", e)

@eel.expose
def history(value):
    try:
        if not os.path.exists("data.xml") or os.stat("data.xml").st_size == 0:
            return []  # Return empty list if file does not exist or is empty

        # Parse XML file
        tree = ET.parse("data.xml")
        root = tree.getroot()

        # Initialize list to store filtered data
        filtered_data = []

        # Iterate over entries
        for entry in root.findall("entry"):
            folder_path = entry.find("folder_path").text
            if value.lower() in folder_path.lower():
                entry_dict = {}
                # Extract attributes
                entry_dict["id"] = entry.get("id")
                entry_dict["date"] = entry.get("date")
                # Extract subelements
                entry_dict["folder_path"] = folder_path
                entry_dict["password"] = entry.find("password").text
                entry_dict["description"] = entry.find("description").text
                # Append entry to filtered data list
                filtered_data.append(entry_dict)

        return filtered_data
    except Exception as e:
        traceback.print_exc()  # Log the exception details
        print("Error:", e)
        return None


try:
    eel.pythonSay("Servidor python conectado")
    eel.start('app.html', size=(1200, 800))
except Exception as e:
    traceback.print_exc()  # Log the exception details

