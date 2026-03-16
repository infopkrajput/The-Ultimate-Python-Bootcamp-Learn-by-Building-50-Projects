"""
Challenge: Batch Rename Files in a Folder

Goal:
- Scan all files in a selected folder
- Rename them with a consistent pattern:
    e.g., "image_1.jpg", "image_2.jpg", ...
- Ask the user for:
    - A base name (e.g., "image")
    - A file extension to filter (e.g., ".jpg")
- Preview before renaming
- Optional: allow undo (save original names in a file)

Teaches: File iteration, string formatting, renaming, user input
"""

import os

def batch_rename(folder, base_name, extension):
    files = [f for f in os.listdir(folder) if f.lower().endswith(extension.lower())]
    files.sort()
    
    if not files:
        print("There are no files.")
        return
    
    for i,file in enumerate(files, start=1):
        new_name = f"{base_name}_{i}{extension}"
        print(f"{file} => {new_name}")
    
    confirmation = input("Are you sure to do it ? (y/n)").strip().lower()
    
    if confirmation != 'y':
        print("Request cancelled!")
        return
    
    for i,file in enumerate(files, start=1):
        new_name = f"{base_name}_{i}{extension}"
        source = os.path.join(folder,file)
        destination = os.path.join(folder,new_name)
        os.rename(source,destination)
        
    print(f"Renamed {len(files)} are renamed!")
    
    

    return

def main():
    folder = input("Enter folder path or leave blank for current folder: ").strip() or os.getcwd()
    
    if not os.path.isdir(folder):
        print("Invalid folder!")
    else:
        base_name = input("Enter base name for files: ").strip()
        extension = input("Enter the extension for files: ").strip()
        
        batch_rename(folder, base_name, extension)
        print("Rename files successfully!")
    
    

if __name__ == "__main__":
    main()
    