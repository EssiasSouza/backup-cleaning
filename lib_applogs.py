import logging
from logging.handlers import TimedRotatingFileHandler
import configparser
import os
import json


with open('settings.json', 'r') as file:
    settings = json.load(file)

logs_path = ""
log_name = ""
for item in settings:
    if 'logs_path' in item:
        logs_path = item['logs_path']
    if 'log_name' in item:
        log_name = item['log_name']

if logs_path and log_name:
    full_log_path = os.path.join(logs_path, log_name)
    print(f"Full log path: {full_log_path}")
else:
    print("logs_path or log_name is missing in the settings.json")




LogFolder = './logs'

print("-- Checking log directory...")

if os.path.exists(LogFolder):
    print(f"-- The directory {logs_path} exists.")
else:
    print(f"-- The directory {logs_path} does not exist.")
    print(f"-- Directory created.")
    os.mkdir(f'./{logs_path}')


logger = logging.getLogger()    
handler = TimedRotatingFileHandler(full_log_path,
when="d",
interval=1,
backupCount=7)
handler.setFormatter(logging.Formatter(fmt='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S -'))

logger.addHandler(handler)