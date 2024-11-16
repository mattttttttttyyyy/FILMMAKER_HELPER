import os
import tkinter as tk
from tkinter import filedialog
from datetime import date
from os import walk
from find_format import recognize_format
import shutil
import logging

log_filename = "folder_organizer.log"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler(log_filename),
    logging.StreamHandler()
])
logger = logging.getLogger(__name__)

root = tk.Tk()
root.withdraw()


class CreateFolders:
    def __init__(self):
        self.main_folder_name = None
        self.project_folders = ["VIDEO", "GFX", "AUDIO", "TEXT", "SFX"]
        self.today = date.today()
        self.year = self.today.year
        self.file_path = 0

    def organize_folder(self, project_name):
        self.file_path = filedialog.askdirectory()
        self.main_folder_name = f"{project_name}"
        main_folder = os.path.join(self.file_path, self.main_folder_name)
        filenames = next(walk(self.file_path), (None, None, []))[2]

        try:
            os.makedirs(main_folder, exist_ok=True)
            logger.info(f"Created main folder: {main_folder}")
        except OSError as e:
            logger.error(f"Failed to create main folder {main_folder}: {e}")

        for folder in self.project_folders:
            main_folder_sub_dir = os.path.join(main_folder, folder)
            try:
                os.makedirs(main_folder_sub_dir, exist_ok=True)
                logger.info(f"Created {folder} folder inside {main_folder}")
            except FileExistsError:
                logger.warning(f"{folder} folder already exists!")

        for file in filenames:
            file_format = recognize_format(file)
            source_path = os.path.join(self.file_path, file)
            if file_format == "PROJECT":
                logger.info(f"Moving project file: {file}")
                shutil.move(source_path, os.path.join(main_folder, file))
                logger.info(f"Moved project file: {file}")
            elif file_format != "UNKNOWN":
                logger.info(f"Moving {file_format}: {file}")
                shutil.move(source_path, os.path.join(main_folder, file_format, file))
                logger.info(f"Moved {file_format}: {file}")
            else:
                logger.warning(f"File not recognized: {file}")

        logger.info("Files moved.")
