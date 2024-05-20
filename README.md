# Backup cleaning
### Purpose of the application
The **Backup cleaning** allows to purge folders of backups in a server. The parameters of time (in days), locations and logs configurations can be set through a file named settings.json.

The settings.json file uses some examples to config:
- First configurations is about the time that the application should run again. This time is set in seconds.
- Log folder and name, you can choose the best name and location for that.
- Days to count before the current computer date to purge folders and its files.
- Root path that the application needs to look for subfolders with data modifications under the date of purge. You can define the value for that if today is 2024/05/20 and you set the value as 15, the application will delete only folders that was modificated under or equal 2024/05/04.

### Required dependences
You can run this application in a **Linux** server with **Python 3.6** installed
- You just need to run the command: python ./backup-cleaning.py

Or if your server uses a Windows operational system you can do that compiling the application using the following steps.
- Install in your computer the **Python 3.6**
- Install the PyInstaller (pip install pyinstaller)
- Download these project files on your computer
- Open the project folder in the same terminal
- **Type the command**: pyinstaller --onefile .\backup-cleaning.py
- Copy the file backup-cleaning.exe saved from the **dist** folder on a folder on the target computer.
- Also copy the settings.json to the same folder on the target computer.
- You can create a service using NSSM application, or a task on the Windows or just run the backup-cleaning.exe

## How to run tests?
For varius tests you can use another application of mine called FoldersCreatorForTests !"https://github.com/EssiasSouza/FoldersCreatorForTests"
Used technologies
How to run the application
Possibles problems / Faced problems
Next steps
