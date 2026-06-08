"""
This file is raise exception for project
"""

import sys
from networksecurity.logging.logger import logging

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = (error_message,)
        _, _, exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno  ## get line number
        self.file_name = exc_tb.tb_frame.f_code.co_filename  ## get file name

    def __str__(self):
        return f" Error occured in python script name [{self.file_name}] line number [{self.lineno}] error message[{self.error_message}]"




if __name__ == "__main__":
    try:
        logging.info("Enter the try block")
        a = 10/0
        print(a)
    except Exception as e:
        raise NetworkSecurityException(e,sys)        