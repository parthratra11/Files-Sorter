# File Sorting Program

## Description

This Python program is designed to organize and sort files in a specified directory into sub-folders based on file types and extensions. It automatically creates the necessary sub-folders and moves the files into their respective categories. This script can handle a wide range of file types including images, videos, applications, PDFs, ZIP files, and more. Any extra files or folders that do not match the predefined categories are moved into an "Extras" folder.

## Features

- **Automatic Directory Sorting:** Sorts files in the selected directory based on file type.
- **Customizable Filters:** Predefined categories such as Images, Videos, PDFs, Applications, etc.
- **Folder Creation:** Automatically creates sub-folders for file organization if they don't already exist.
- **Duplicate Handling:** Skips files that already exist in the destination folder.
- **Catch-all Category:** Moves any non-specified files or folders into a `Folders + Extras` sub-folder.

## File Type Categories

The files are sorted into the following categories:

- **Images:** `.png`, `.jpg`, `.jpeg`, `.svg`, `.ico`
- **Videos:** `.mp4`
- **Applications:** `.exe`, `.msi`
- **PDFs:** `.pdf`
- **ZIP Files:** `.zip`, `.rar`
- **Word Documents:** `.doc`, `.docx`
- **PPTs:** `.pptx`
- **Excel Sheets:** `.xlsx`, `.csv`
- **Music:** `.mp3`
- **Folders + Extras:** Other files and sub-folders

## How It Works

1. The program prompts you to specify the directory path where the files are stored.
2. The script then checks the directory and creates the necessary sub-folders based on the predefined filters.
3. It scans the directory for files and moves each file to the corresponding sub-folder based on its extension.
4. Any files that do not fit the predefined categories are moved into a `Folders + Extras` sub-folder.
5. If a file with the same name already exists in the destination folder, the file is skipped.

## Usage

1. Clone or download this repository to your local machine.
2. Update the `myPath` variable in the script with the directory path you want to sort.
   ```python
   myPath = r"Path_to_your_directory"
   ```
3. Run the script in your terminal or command prompt:
   ```bash
   python file_sorter.py
   ```
4. The files in the specified directory will automatically be sorted into the corresponding sub-folders.

## Requirements

- Python 3.x
- No external dependencies are required.

## Notes

- Ensure that you have permission to modify and move files in the target directory.
- Before running the script, make sure there are no open files in the directory to prevent errors while renaming.
