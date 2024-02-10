"""
running the signal if the alarm clock was not stopped before
"""

from datetime import datetime, timedelta
import logging
import time


def beep():
    """ 
    textual replacement for testing pc
    """
    end_time = datetime.now() + timedelta(minutes=6)
    logging.getLogger().info("end at %s", end_time)

    while end_time > datetime.now():
        print(".", end="", flush=True)
        time.sleep(1)
    print(".", end="\n")
    logging.getLogger().info("clear up")
