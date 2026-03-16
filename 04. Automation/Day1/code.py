"""
 Challenge: File Sorter by Type

Goal:
- Scan the current folder (or a user-provided folder)
- Move files into sub-folders based on their type:
    - .pdf → PDFs/
    - .jpg, .jpeg, .png → Images/
    - .txt → TextFiles/
    - Others → Others/
- Create folders if they don't exist
- Ignore folders during the move

Teaches: File system operations, automation, file handling with `os` and `shutil`
"""

import os
import shutil

EXTENSION_MAP = {
    "Images":[".jpg",".jpeg",".png"],
    "Text":[".txt"],
    "PDFs":[".pdf"],
}

def get_destination_folder(filename):
    extension = os.path.splitext(filename)[1].lower()
    for folder, extensions in EXTENSION_MAP.items():
        if extension in extensions:
            return folder
    
    return "Others"
    
def sort_files(folder_path):
    for file in os.listdir(folder_path):
        source_path = os.path.join(folder_path,file)
        
        # Skip Script
        if file == "code.py":
            continue
        
        if os.path.isfile(source_path):
            destination_folder = get_destination_folder(file)
            destination_path = os.path.join(folder_path,destination_folder)
            
            os.makedirs(destination_path, exist_ok=True)
            
            # Move the file 
            shutil.move(source_path,os.path.join(destination_path,file))
            print(f"Moved {file} to {destination_path}")

def main():
    current_directory = os.getcwd()
    sort_files(current_directory)    

if __name__ == "__main__":
    main()
    