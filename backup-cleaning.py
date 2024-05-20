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
        # input_date_str = "04/05/2023"
        # current_date = datetime.datetime.strptime(input_date_str, "%d/%m/%Y")
        # formated_date = current_date.strftime("%d/%m/%Y %H:%M:%S")

        current_date = datetime.datetime.now()
        formated_date = current_date.strftime("%d/%m/%Y %H:%M:%S")

        print("Defined date:", formated_date)
        lib_applogs.logger.warning(f'Defined date:{formated_date}')
        while True:

            def delete():
                with open('settings.json', 'r', encoding='utf-8') as f:
                    params = json.load(f)

                for param in params:
                    try:
                        print(f'DIRECTORY: {param["folder_path"]}')
                        lib_applogs.logger.warning(f'DIRECTORY: {param["folder_path"]}')

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
                                    print(f'-- {subfolder} not matches the deletion date')
                                    lib_applogs.logger.warning(f'{subfolder} found, but not matches the deletion date')
                                    
                        else:
                            time.sleep(2)
                            print('-- There are no subfolders in this path')
                            lib_applogs.logger.warning(f'There are no subfolders in this path.')
                    except:
                        time.sleep(2)
                        print('There are no objects found')
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
