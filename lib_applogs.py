import logging
from logging.handlers import TimedRotatingFileHandler
import configparser
import os

LogFolder = './logs'

print("-- Checking log directory...")

if os.path.exists(LogFolder):
    print(f"-- The directory {LogFolder} exists.")
else:
    print(f"-- The directory {LogFolder} does not exist.")
    print(f"-- Directory created.")
    os.mkdir('./logs')

# Log name of application
logFileName = LogFolder + "/backup-cleanning.log"

logger = logging.getLogger()    
handler = TimedRotatingFileHandler(logFileName,
when="d",
interval=1,
backupCount=7)
handler.setFormatter(logging.Formatter(fmt='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S -'))

logger.addHandler(handler)