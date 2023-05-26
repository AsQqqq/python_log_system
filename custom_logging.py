# IMPORT

import logging
from colorama import Fore, Style
import time


# CONFIG

path_to_logs = ""
saving_logs = True
log_output_delay = 0.05
log_output_to_the_console = True


# MAIN FUNC

def info_(path, text):
    text_ = f"{path} >>> {text}"
    logger.info(text_)
    time.sleep(log_output_delay)

def warning_(path, text):
    text_ = f"{path} >>> {text}"
    logger.warning(text_)
    time.sleep(log_output_delay)

def error_(path, text):
    text_ = f"{path} >>> {text}"
    logger.error(text_)
    time.sleep(log_output_delay)


# MAIN CODE

if log_output_to_the_console == True:
    logging.getLogger().setLevel(logging.INFO)

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s : %(message)s')

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.propagate = False
logger.addHandler(console_handler)

logging.addLevelName(logging.INFO, f"[{Fore.GREEN}{logging.getLevelName(logging.INFO)}{Style.RESET_ALL}]")
logging.addLevelName(logging.WARNING, f"[{Fore.YELLOW}{logging.getLevelName(logging.WARNING)}{Style.RESET_ALL}]")
logging.addLevelName(logging.ERROR, f"[{Fore.RED}{logging.getLevelName(logging.ERROR)}{Style.RESET_ALL}]")

if saving_logs == True:
    logging.basicConfig(filename=f"{path_to_logs}logs.txt",
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)