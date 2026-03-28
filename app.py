import sys
from src.end_to_end.logger import logging
from src.end_to_end.exception import EndToEndException



if __name__ == "__main__":
    logging.info("Starting the application........")
    
    try: 
        a=1/0
    except Exception as e:
        logging.info("Exception occurred........")
        raise EndToEndException(e, sys) from e
