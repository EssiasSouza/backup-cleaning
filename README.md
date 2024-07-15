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

