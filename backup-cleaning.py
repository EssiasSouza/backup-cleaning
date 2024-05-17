import datetime
import time
import os
import shutil
import pathlib
import lib_applogs
import json

print('Starting application')
lib_applogs.logger.warning('Starting application')

# # TESTING DATE
# input_date_str = "04/05/2023"
# current_date = datetime.datetime.strptime(input_date_str, "%d/%m/%Y")
# formated_date = current_date.strftime("%d/%m/%Y %H:%M:%S")

current_date = datetime.datetime.now()
formated_date = current_date.strftime("%d/%m/%Y %H:%M:%S")

print("Defined date:", formated_date)
lib_applogs.logger.warning(f'Defined date:{formated_date}')



def daily():

    with open('settings.json', 'r', encoding='utf-8') as f:
        params = json.load(f)

    for param in params:
        try:
            print(f'DIRECTORY: {param["folder_path"]}')

            day_less = int(param["day_less"])

            adjusted_date = current_date - datetime.timedelta(days=day_less)
                        
            folder_path = param["folder_path"]

            subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

            if subfolders:

                for subfolder in subfolders:
                    modification_time = os.path.getmtime(subfolder)
                    modification_date = datetime.datetime.fromtimestamp(modification_time)
                    modification_formated_date = modification_date.strftime("%d/%m/%Y %H:%M:%S")

                    if modification_date < adjusted_date:
                        print(subfolder)
                        print("-- Modification date of folder is under of:", modification_formated_date , 'folder deleted!')
                        shutil.rmtree(subfolder)
                        lib_applogs.logger.warning(f'Deleted: {subfolder}')
                        time.sleep(2)
                        
            else:
                time.sleep(2)
                print('-- There is nothing to delete')

            lib_applogs.logger.warning(f'End of purge process.')
        except:
            time.sleep(2)
            print('Root path not found')

daily()
print("Process finished")
lib_applogs.logger.warning(f'Process finished.')
