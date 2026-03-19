"""
 Challenge: Auto File Organizer with Watchdog

Goal:
- Monitor a folder (e.g., Downloads/Desktop)
- When a new file is added:
    - Move PDFs to /PDFs
    - Move Images to /Images
    - Move ZIP files to /Archives
    - Everything else goes to /Others

Teaches: Folder monitoring, real-time automation, event-driven design
Tools: watchdog, shutil, os
"""

import os 
import shutil
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

WATCH_FOLDER = os.path.expanduser("~/Downloads")

FILE_DESTINATIONS = {
    '.pdf': 'PDFs',
    '.jpg': 'Images',
    '.png': 'Images',
    '.zip': 'Archives',
}

class FileMoverHandler(FileSystemEventHandler):
    def on_created(self, event: FileSystemEvent):
        if event.is_directory:
            return
        
        file_path = event.src_path
        ext = os.path.splitext(file_path)[1].lower()
        
        dest_folder = FILE_DESTINATIONS.get(ext, 'Others')
        dest_path = os.path.join(WATCH_FOLDER, dest_folder)
        
        os.makedirs(dest_path, exist_ok=True)
        move_to = os.path.join(dest_path, os.path.basename(file_path))

        try:
            shutil.move(file_path, move_to)
            print(f"Moved {file_path} to {move_to}")
        except Exception as e:
            print(f"Error moving {file_path}: {e}")

if __name__ == "__main__":
    print(f"Watching folder: {WATCH_FOLDER}")
    event_handler = FileMoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    