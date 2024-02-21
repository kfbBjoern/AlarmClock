"""
Checks for ending the alarm before time 
"""
from os import path
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

def read_temperature_device(dev):
    """read from sensore type D18S20"""
    master = "/sys/bus/w1/devices/w1_bus_master1"
    file = path.join( master, dev, "w1_slave")
    with open(file, encoding='utf-8') as file_temp:
        string_value = file_temp.read().split("t=")[1]
        temperature = int(string_value.strip())/1000.0
    return temperature

def check_temperature():
    """checks that a flame is near the nail"""
    slave = '10-000803b33dd1'
    temp = read_temperature_device(slave)
    if temp > 32:
        return True, temp
    return False, temp
