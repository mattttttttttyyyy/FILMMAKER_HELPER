
# Filmmaker Folder Organizer

This is a Python script designed to help filmmakers and media producers organize their project files into separate folders for video, audio, graphics, text, and project files. It uses a graphical user interface (GUI) built with Tkinter to facilitate folder organization with a few simple steps.

## Features

- Automatically creates directories for **VIDEO**, **AUDIO**, **GFX**, **TEXT**, and **SFX**.
- Classifies and moves files into the correct folders based on their formats.
- Supports a wide range of video, audio, image, and document file formats.
- Logs all actions in a log file (`folder_organizer.log`).
- Allows users to specify the project name and choose the directory for organizing files.

## File Formats Supported

- **VIDEO**: `3g2`, `avi`, `flv`, `mkv`, `mp4`, `mov`, `mpeg`, `webm`, `wmv`, `yuv`, and others.
- **AUDIO**: `mp3`, `wav`, `flac`, `aac`, `ogg`, `m4a`, and others.
- **IMAGE**: `jpg`, `png`, `gif`, `bmp`, `psd`, `tiff`, `svg`, and others.
- **PROJECT**: Adobe Premiere Pro (`prproj`), After Effects (`aep`), Vegas (`veg`), Final Cut Pro (`fcp`, `fcpx`).
- **TEXT**: `txt`, `docx`, `pdf`, `odt`, `rtf`.

## Installation

To run this script, you need to have Python installed on your machine. The script also requires the following libraries:

- `tkinter` (for GUI)
- `os` (for file system operations)
- `shutil` (for moving files)
- `logging` (for logging events)
- `find_format` (for recognizing file formats)

You can install the necessary dependencies using the following command:

    pip install tk

## Usage

1.  Run the Python script.
2.  A GUI window will appear with a button to organize your project folder.
3.  Click on  **"Organize project folder"**.
4.  A popup window will prompt you to enter the project name.
5.  The script will automatically create the main folder and subdirectories (**VIDEO**,  **AUDIO**,  **GFX**,  **TEXT**,  **SFX**) inside the chosen directory.
6.  Files in the selected directory will be moved to their corresponding subdirectories based on their format.

## Logging

The program logs all actions to a file called  `folder_organizer.log`. The log includes:

-   Folder creation attempts (success or failure).
-   File movement actions (which files were moved and where).
-   Warnings for files that couldn't be recognized.

## Example Log

When you run the script, the log will look something like this:

    2024-11-16 10:00:00 - INFO - Created main folder: /path/to/directory/Test_Project
    2024-11-16 10:00:05 - INFO - Created VIDEO folder inside /path/to/directory/Test_Project
    2024-11-16 10:00:10 - INFO - Moving video: movie.mp4
    2024-11-16 10:00:12 - INFO - Moved video: movie.mp4
    2024-11-16 10:00:15 - WARNING - File not recognized: unknown.xyz
    2024-11-16 10:00:20 - INFO - Files moved.


## Contributing

Feel free to fork the repository and submit pull requests. If you encounter any issues or have suggestions for improvements, open an issue in the GitHub repository.

## License

This project is licensed under the MIT License.