import datetime
import time
import os
import shutil
import pathlib
import lib_applogs
import json

print('Starting application')
lib_applogs.logger.warning('Starting application')

def daily():
    def main():

        # # TESTING DATE
        # input_date_str = "17/07/2024"
        # current_date = datetime.datetime.strptime(input_date_str, "%d/%m/%Y")
        # formated_date = current_date.strftime("%d/%m/%Y %H:%M:%S")

        current_date = datetime.datetime.now()
        formated_date = current_date.strftime("%d/%m/%Y %H:%M:%S")

        print("Defined date:", formated_date)
        lib_applogs.logger.warning(f'Defined date:{formated_date}')
        while True:
            def objectsExcluding(object_list, criteria_to_exclude):
                filtered_list = []
                for obj in object_list:
                    if not any(criteria in obj for criteria in criteria_to_exclude):
                        filtered_list.append(obj)
                return filtered_list

            def deleteDirs(subfolders, ExceptionSplit, adjusted_date):
                if subfolders:
                    filteredDirList = objectsExcluding(subfolders, ExceptionSplit)
                    # filtered_list = [item for item in subfolders if not is_excluded(item, ExceptionSplit)]
                    
                    for subfolder in filteredDirList:
                        modification_time = os.path.getmtime(subfolder)
                        modification_date = datetime.datetime.fromtimestamp(modification_time)

                        if modification_date < adjusted_date:
                            modification_formated_date = modification_date.strftime("%d/%m/%Y %H:%M:%S")
                            print("-- Modification date of folder is under of:", modification_formated_date , 'folder deleted!')
                            shutil.rmtree(subfolder)
                            lib_applogs.logger.warning(f'Deleted: {subfolder}')
                            time.sleep(2)
                        else:
                            print(f'-- {subfolder} not matches the deletion date')
                            lib_applogs.logger.warning(f'{subfolder} found, but not matches the deletion date')
                else:
                    time.sleep(2)
                    print('-- There are no subfolders in this path')
                    lib_applogs.logger.warning(f'There are no subfolders in this path.')
            def deleteFiles(files_in, ExceptionSplit, adjusted_date):
                if files_in:
                    filtered_files = objectsExcluding(files_in, ExceptionSplit)
                    # filtered_files = [item for item in files_in if not is_excluded(item, ExceptionSplit)]
                    for file_in in filtered_files:
                        modification_time = os.path.getmtime(file_in)
                        modification_date = datetime.datetime.fromtimestamp(modification_time)
                        if modification_date < adjusted_date:
                            modification_formated_date = modification_date.strftime("%d/%m/%Y %H:%M:%S")
                            
                            os.remove(file_in)
                            print(f"-- Modification date of folder is under of: {modification_formated_date} file {file_in} deleted!")
                            lib_applogs.logger.warning(f'Deleted: {file_in}')
                            time.sleep(1)

            def delete():
                with open('settings.json', 'r', encoding='utf-8') as f:
                    params = json.load(f)

                for param in params:
                    if 'run_pause_time' in param:
                        pass
                    if 'logs_path' in param:
                        pass
                    if 'log_name' in param:
                        pass

                    if 'watchedDir' in param:
                        day_less = int(param['watchedDir']["day_less"])
                        dir_path = param['watchedDir']['folder_path']
                        ExceptExtDir = param['watchedDir']['ExceptExtDir']
                        ExceptionSplit = ExceptExtDir.split(",")

                        try:
                            adjusted_date = current_date - datetime.timedelta(days=day_less)
                            folder_path = dir_path
                            subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
                            files_in = [f.path for f in os.scandir(folder_path) if f.is_file()]

                            print(f'\nDIRECTORY: {folder_path}')
                            lib_applogs.logger.warning(f'DIRECTORY: {folder_path}')

                            deleteDirs(subfolders, ExceptionSplit, adjusted_date)
                            deleteFiles(files_in, ExceptionSplit, adjusted_date)

                        except Exception as e:
                            time.sleep(2)
                            print(e)
                            lib_applogs.logger.warning('There is no object found')
   
            delete()

            # Calculating time to run again
            with open('settings.json', 'r', encoding='utf-8') as file:
                settings  = json.load(file)
            run_pause_time_str = settings[0]['run_pause_time']
            run_pause_time = int(run_pause_time_str)

            if run_pause_time < 60:
                hours = 00
                minutes = 00
                seconds = run_pause_time
            elif run_pause_time < 3600:
                hours = 00
                minutes = run_pause_time // 60
                seconds = run_pause_time % 60
            else:
                hours = run_pause_time // 3600
                remaining_time = run_pause_time % 3600
                minutes = remaining_time // 60
                seconds = remaining_time % 60

            finish = f'Waiting for {run_pause_time} seconds ({hours:.0f}h{minutes:.0f}m{seconds:.0f}s) to execute again.'
            print(finish)
            lib_applogs.logger.warning(finish)
            time.sleep(run_pause_time)

    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print("The service was stopped")   

daily()
print("Process finished")
lib_applogs.logger.warning(f'Process finished.')