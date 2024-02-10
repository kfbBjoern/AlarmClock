"""
This module is running the acoustic signal if the alarm clock was not stopped before
can only run on the raspberry because it uses GPIOs
"""

from datetime import datetime, timedelta
import logging
import time

from  gpiozero import PWMOutputDevice


def beep():
    """ 
    run the piezo on the raspberry pi
    """
    buzzer=PWMOutputDevice(21, active_high=True, initial_value=1, frequency=400,
                            pin_factory=None)
    buzzer.pulse(1,1)
    end_time = datetime.now() + timedelta(minutes=6)
    logging.getLogger().info("end at %s", end_time)

    while end_time > datetime.now():
        time.sleep(10)

    logging.getLogger().info("clear up")
    buzzer.off()
    buzzer.close()
