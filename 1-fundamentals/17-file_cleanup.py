import os

original_folder_path = 'C:/Users/leebo/Desktop'
folder_destination = 'C:/Users/leebo/Desktop/OrganizedFiles/'

os.mkdir(folder_destination)

for entry in os.scandir(original_folder_path):
    if entry.is_file():
        file_path = entry.path
        file_name, file_extension = os.path.splitext(file_path)
        file_extension = file_extension.lower()

        if file_extension:
            destination_folder = folder_destination + file_extension[1:]

            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)

            os.rename(file_path, destination_folder + '/' + os.path.basename(file_path))