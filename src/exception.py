import sys
import logging 
from src.logger import logging
def error_msg_details(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_msg="error occured in python script name [{0}] line number [{1}] error message [{2}]".format(filename,exc_tb.tb_lineno,str(error))
    return error_msg

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_msg_details(error_message,error_details=error_details)

    def __str__(self):
        return self.error_message 
    


if __name__ == "__main__": 
    try:
        a=1/0
    except Exception as e:
        logging.info("An error occurred")
        raise CustomException(e,sys)