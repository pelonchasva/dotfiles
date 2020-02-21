import logging
import os, sys
from datetime import datetime

class Logger(object):
    """
    Logger class that writes the messages to a file
    """

    def __init__(self, name):
        """
        """
        self.name = name
        self.logger = logging.getLogger(self.name)
        self.f_handler = logging.FileHandler(self.get_log_file())
        self.f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.f_handler.setFormatter(self.f_format)
        self.logger.addHandler(self.f_handler)

    def debug(self, msg):
        """
        """
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug(msg)

    def info(self, msg):
        """
        """
        self.logger.setLevel(logging.INFO)
        self.logger.info(msg)

    def warn(self, msg):
        """
        """
        self.logger.setLevel(logging.WARN)
        self.logger.warn(msg)

    def error(self, msg):
        """
        """
        self.logger.setLevel(logging.ERROR)
        self.logger.error(msg)

    def critical(self, msg):
        """
        """
        self.logger.setLevel(logging.CRITICAL)
        self.logger.critical(msg)

    def get_log_file(self, path="dotfiles.log"):
        """
        Returns the path of the log file or creates one if needed
        """
        if not os.path.exists(path):
            with open(path, "w+") as f:
                log_date = datetime.today()
                f.write(f"===== Log File Created on: {log_date} =====\n")
            print("Log file created.")

        return path
