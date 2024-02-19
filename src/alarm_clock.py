"""
Tool to tun an alarm clock if not different things happen before the time ends
"""
import argparse
import datetime
import time
import logging
import sys

try:
    from modules import beep as myBeep
except ImportError:
    from modules import beep_win as myBeep

try:
    from modules import checks as myCheck
except ImportError:
    from modules import checks_win as myCheck

class AlarmClock:
    """
    Class to manage the alarm clock 
    """
    def __init__(self, args):
        """
        setup the alarm clock class with logger check 
        """
        self.log_level = logging.ERROR
        self.alarm_time = ""
        if args:
            self.handle_options(args[1:])
        logger = logging.getLogger()
        logger.setLevel(self.log_level)
        self.log(logging.DEBUG, f"Set alarm to   {self.alarm_time}")

    def run(self):
        """
        running the alarmclock and check for probes
        """
        while self.checks() is False:
            if self.alarm_time < datetime.datetime.now():
                self.beep()
                sys.exit(0)
            else:
                time.sleep(1)
        self.make_clear()

    def beep(self):
        """
        Oh, oh, the bell is ringing 
        """
        myBeep.beep()


    def checks(self):
        """
        check ever probe and return status
        """
        button =  myCheck.check_buttons()
        if button == 2:
            self.log(logging.DEBUG, "Wrong wire Boom")
            self.beep()
        if button == 1:
            self.log(logging.DEBUG, "checks done")
            return True
        self.log(logging.DEBUG, "checks failed")
        return False

    def make_clear(self):
        """
        clean up every thing
        """
        return

    def handle_options(self, arguments):
        """
        takes all arguments an read the options out of it
        """
        parser = argparse.ArgumentParser(
                    prog='alarm_clock',
                    description='Building AEA Desktop tools')
        parser.add_argument('-v', '--verbose', action='count', dest='verbose', default=0)
        parser.add_argument('-a', '--alarm', action='store', dest='alarm', default="")
        args, remainder = parser.parse_known_args(arguments)
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
        for r in remainder:
            print(f"unknown option {r}")

    def log(self, level, msg: str):
        """
        write log to
        """
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
