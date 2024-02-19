"""
Checks for ending the alarm before time 
"""
from gpiozero import Button

def check_buttons():
    """
    Checks that the wire connected to GPIO 16 is cut and the one to GPIO26 not
    """
    button_true = Button(26)
    button_false = Button(16)

    if button_true.is_pressed and button_false.is_pressed:
        return 0
    if button_true.is_pressed and not button_false.is_pressed:
        return 1
    return 2
