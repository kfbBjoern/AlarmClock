"""
Tool to tun an alarm clock if not different things happen before the time ends
"""
import argparse
import datetime
import time
import logging
import sys

class AlarmClock:
    """
    Class to manage the alarm clock 
    """
    def __init__(self, args):
        self.log_level = logging.ERROR
        self.alarm_time = ""
        if args:
            self.handle_options(args[1:])
        logger = logging.getLogger()
        logger.setLevel(self.log_level)
        self.log(logging.DEBUG, f"Set alarm to   {self.alarm_time}")

    def run(self):
        while self.checks() is False:
            if self.alarm_time < datetime.datetime.now():
                self.beep()
                exit(0)
            else:
                time.sleep(1)
        self.make_clear()

    def beep(self):
        for i in range(1, 1000):
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    def checks(self):
        return False

    def make_clear(self):
        return

    def handle_options(self, arguments):
        parser = argparse.ArgumentParser(
                    prog='alarm_clock',
                    description='Building AEA Desktop tools')
        parser.add_argument('-v', '--verbose', action='count', dest='verbose', default=0)
        parser.add_argument('-a', '--alarm', action='store', dest='alarm', default="")
        args = parser.parse_known_args(arguments)
        arg = vars(args)
        for key in arg.keys():
            if 'alarm' == key:
                offset = time.strptime(arg[key], "%H:%M")
                td = datetime.timedelta(hours=int(offset.tm_hour), minutes=offset.tm_min)
                self.alarm_time = datetime.datetime.today() + td
            if 'verbose' == key:
                if arg[key] >= 3:
                    self.log_level = logging.DEBUG
                elif arg[key] == 2:
                    self.log_level = logging.INFO
                elif arg[key] == 1:
                    self.log_level = logging.WARNING

    def log(self, level, msg: str):
        logger = logging.getLogger()
        logger.log(level, msg)


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")

    try:
        alarm = AlarmClock(sys.argv)
        alarm.run()
        sys.exit(0)
    except ValueError as error:
        logging.error(error)
