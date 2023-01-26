'''
Logging File
'''

import logging
import os
from datetime import datetime
import os

#log file name
'''
Month Date Year _ Hour Minutes Seconds used for Filename
'''
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"

#log directory
'''
Directory with name logs can get created
'''
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")

#create folder if not available
os.makedirs(LOG_FILE_DIR,exist_ok=True)

#log file path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)


'''
Time Line Number Level Name Message

Level      Numeric Value

CRITICAL      50

ERROR         40

WARNING       30

INFO          20

DEBUG         10

NOTSET         0

'''

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)