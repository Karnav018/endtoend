import sys
from src.end_to_end.logger import logging
from src.end_to_end.exception import EndToEndException
from src.end_to_end.components.data_ingestion import DataIngestion
from src.end_to_end.components.data_ingestion import DataIngestionConfig


if __name__ == "__main__":
    logging.info("Starting the application........")
    
    try: 
        # data_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Exception occurred........")
        raise EndToEndException(e, sys) from e
