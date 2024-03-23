import os
import shutil

def scan_directory(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def identify_file_type(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension in ('.jpg', '.png', '.gif'):
        return 'Images'
    elif file_extension in ('.doc', '.pdf', '.txt'):
        return 'Documents'
    elif file_extension in ('.mp4', '.avi', '.mkv'):
        return 'Videos'
    else:
        return 'Others'

def organize_files(directory):
    files = scan_directory(directory)
    for file in files:
        file_type = identify_file_type(file)
        if file_type != 'Others':
            destination_folder = os.path.join(directory, file_type)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            shutil.move(file, destination_folder)

def main():
    directory = input("Enter the directory to organize: ")
    organize_files(directory)
    print("Files organized successfully.")

if __name__ == "__main__":
    main()
