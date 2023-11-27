from src.yolo5.entity.config_entity import ConfigurationManager
from src.yolo5.components.data_ingestion import DataIngestion
from src.yolo5.exception import AppException
from src.yolo5.logger import logging
import sys


STAGE_NAME = 'Data Ingestion'


class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise AppException(e, sys)
