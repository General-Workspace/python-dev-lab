import os
import shutil

desktop_path = os.path.expanduser("~/Desktop")

folders = {
    "images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
    "videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "audio": [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "documents": [".pdf", ".doc", ".docx", ".rtf", ".txt", ".odt", ".wpd", ".xls", ".xlsx", ".ods", ".ppt", ".pptx", ".odp"],
    "archives": [".zip", ".7z", ".rar", ".tar", ".gz", ".dmg", ".iso"],
}

for folder_name in folders:
    # folder_path = os.path.join(desktop_path, folder_name)
    # os.makedirs(folder_path, exist_ok=True)
    os.makedirs(os.path.join(desktop_path, folder_name), exist_ok=True)

for file_name in os.listdir(desktop_path):
    original_file_path = os.path.join(desktop_path, file_name)
    if os.path.isfile(original_file_path):
        for folder_name, extensions in folders.items():
            for extension in extensions:
                if file_name.endswith(extension):
                    # shutil.move(os.path.join(desktop_path, file_name), os.path.join(desktop_path, folder_name, file_name))
                    destination_folder = os.path.join(desktop_path, folder_name)
                    shutil.move(original_file_path, destination_folder)
                    break