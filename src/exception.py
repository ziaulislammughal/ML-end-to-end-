import sys
import logging
import traceback
from src.logger import logging 

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error Occurred in Python Script name [{file_name}] line number [{exc_tb.tb_lineno}] : {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        self.error_traceback = traceback.format_exc()

    def __str__(self):
        return f"{self.error_message}\n{self.error_traceback}"

