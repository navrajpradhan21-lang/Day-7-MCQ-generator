import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(),"logs")  #joins log in current working directory 
# returns D:\LANGCHAIN\Day-7 MCQ generator\logs

os.makedirs(log_path,exist_ok= True)  # makes a log folder and skips if already exist 

LOG_FILEPATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(level=logging.INFO,
        filename = LOG_FILEPATH,
        format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s- %(message)s"
)
