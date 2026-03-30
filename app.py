import sys
from src.end_to_end.logger import logging
from src.end_to_end.exception import EndToEndException
from src.end_to_end.components.data_ingestion import DataIngestion
from src.end_to_end.components.data_transformation import (
    DataTransformationConfig,
    DataTransformation,
)

if __name__ == "__main__":
    logging.info("Starting the application........")

    try:
        # # data_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        # data_transformation_config = DataTransformationConfig()
        data_transformation.initiate_data_transformation(
            train_path=train_data_path, test_path=test_data_path
        )

    except Exception as e:
        logging.info("Exception occurred........")
        raise EndToEndException(e, sys) from e
