"""
Checks for ending the alarm before time 
"""
from time import sleep

TEST_RUN = 0

def check_buttons():
    """
    Fake Checks that the wire connected to GPIO 16 is cut and the one to GPIO26 not
    """
    global TEST_RUN
    TEST_RUN += 1
    if 10 < TEST_RUN < 30:
        return 1
    if TEST_RUN >= 30:
        return 2
    sleep(2)
    return  0
