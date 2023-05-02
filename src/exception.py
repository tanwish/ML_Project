import sys 
import logging
import logger

def error_message_detail(error,error_detail:sys):
    # _, _, exc_tb=error_detail.exc_info()
    # # exc_type, exc_obj, exc_tb = error_detail

    # file_name = exc_tb.tb_frame.f_code.co_filename
    # error_message = f"error occured in python script name[{0}] line number [{1}]error_message [{2}]".format(

    #     file_name,exc_tb.tb_lineno,str(error))
    # return error_message
    _,_,exc_tb=error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "error occurred in python script name[{0}] line number [{1}] error_message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    return error_message
    # _, _, exc_tb = error_detail.exc_info()

    # file_name = exc_tb.tb_frame.f_code.co_filename
    # error_message = f"error occured in python script name[{file_name}] line number [{exc_tb.tb_lineno}] error_message [{error}]"
    # return error_message


class CustomException(Exception):
    # def __init__(self, error_message,error_detail:sys):
    #     super().__init__(error_message)
    #     self.error_message = error_message_detail(error_message,error_detail=error_message_detail)

    # def __str__(self):
    #     return self.error_message
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
    

if __name__=="__main__":
    logging.basicConfig(filename=LOG_FILE_PATH,
                        format="[%(asctime)s]%(lineno)d %(name)s - %(levelname)s - %(message)s",
                        level=logging.INFO,)
    try:
        a=1/0
    except Exception as e:
        logging.info("Loggig has started")
        raise CustomException(e,sys)