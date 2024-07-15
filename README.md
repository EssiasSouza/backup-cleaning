<<<<<<< HEAD
# Daily Cleanup application

This Python application performs daily cleanup operations on specified directories, removing files and subfolders that are older than a given number of days. The application logs its actions and can be configured via a `settings.json` file.

## Table of Contents
- [Overview](#overview)
- [Setup](#setup)
- [Configuration](#configuration)
- [Usage](#usage)
- [Details](#details)

## Overview

The application:
1. Reads configuration parameters from `settings.json`.
2. Defines the current date and formats it.
3. Iterates over specified directories to delete files and subfolders older than a specified number of days.
4. Logs all actions using `lib_applogs`.
5. Sleeps for a configurable amount of time before running again.

## Setup

1. Ensure you have Python installed on your system.
2. Install necessary dependencies (if any, like `lib_applogs`).
3. Place the application and `settings.json` in the same directory.

## Configuration

Create a `settings.json` file with the following structure:

```json
[
    {
        "folder_path": "path/to/your/folder",
        "day_less": 30,
        "run_pause_time": 3600
    }
]
```

- `folder_path`: The path of the directory to clean up.
- `day_less`: The number of days to subtract from the current date to determine which files/folders to delete.
- `run_pause_time`: The time in seconds to wait before running the application again.

## Usage

Run the application using the command:

```sh
python your_application_name.py
```

To stop the application, press `Ctrl+C`.

## Details

### application Breakdown

- **Imports**: The application imports necessary libraries, including `datetime`, `time`, `os`, `shutil`, `pathlib`, and `json`.
- **Logging**: Uses `lib_applogs` for logging important actions and messages.
- **Main Function**: The `main()` function is where the core logic resides.
  - **Current Date**: Defines and formats the current date.
  - **Delete Function**: Deletes files and subfolders older than the specified number of days.
  - **Sleep and Repeat**: Sleeps for the specified amount of time before repeating the process.

### Main Function

The `main()` function executes the following steps:
1. **Define Date**: Gets the current date and formats it.
2. **Delete Old Files/Folders**: Reads the `settings.json` and deletes files/folders older than the specified number of days.
3. **Pause and Restart**: Calculates the sleep time from `settings.json` and pauses before the next run.

### Delete Function

The `delete()` function performs the following actions:
1. **Read Settings**: Opens and reads the `settings.json` file.
2. **Iterate Over Parameters**: For each parameter set in the settings, it:
   - Prints and logs the directory path.
   - Calculates the date threshold.
   - Deletes subfolders and files older than the threshold.
3. **Log and Sleep**: Logs actions and sleeps for 2 seconds between deletions.

### Error Handling

The application includes basic error handling:
- **Try/Except Block**: Catches and logs errors if no objects are found for deletion.

### application Termination

The application can be terminated gracefully using `KeyboardInterrupt` (Ctrl+C).

=======
# Backup Cleaning 🧹
### Purpose of the application
The **Backup Cleaning** allows to purge folders of backups in a server. The parameters of time (in days), locations and logs configurations can be set through a file named settings.json.

The settings.json file uses some examples to config:
- The first setting is the time at which the application should be run again. This time is defined in seconds.
- Log folder and name. You can choose the best name and location for that.
- Days to count before the current computer date to purge folders and its files.
- Root path that the application needs to search for subfolders with modification date below the maximum purge date. For example, if you set the value to 15 and the current date is 2024/05/20, the application will only delete folders that were modified on dates less than or equal to 2024/05/04.

### Required dependences
You can run this application in a **Linux** server with **Python 3.6** installed
- You just need to run the command: python ./backup-cleaning.py

Or if your server uses a Windows operating system you can do this by compiling the application following these steps below.
- Install on your computer the **Python 3.6**
- Also install the PyInstaller (pip install pyinstaller)
- Download these project files on your computer
- Open the project folder on the same terminal
- **Type the command**: pyinstaller --onefile .\backup-cleaning.py
- Copy the file **backup-cleaning.exe** saved from the **dist** folder on a folder on the destination computer.
- Also copy the settings.json file to the same folder on the target computer.
- You can create a service using NSSM application, or a task on the Windows or just run the backup-cleaning.exe

### How to run tests?
For varius tests you can use another application of mine called [FoldersCreatorForTests](https://github.com/EssiasSouza/FoldersCreatorForTests").
FoldersCreatorForTests creates folders and files by changing the modification date, which allows you to test various backup file scenarios.

### Used technologies
The **Backup-Cleaning** was created only in python using some libraries:
- datetime (To work the data modification time information)
- time (To allow tests and wait states)
- os (To access OS directories)
- shutil (To manage OS directories)
- lib_applogs (Also created by me to configure the logs files when I create any applications)
- json

### How to run the application
To run the application you need to follow the **Required dependences**.
**For Linux just run**:
- python ./backup-cleaning.py
**For Windows you can only run the same command or:**
- Compile the application
- Run backup-cleaning.exe

### Possibles problems / Faced problems
I faced no problems in building this, you just need to be awake to the time of purging and the true path you need to purge.

### Next steps
Implement the purging of logs generated by the application and copying the logs for sending via EDI.
>>>>>>> 835cbd936c6495b5f76e825d00cac68e73645322
