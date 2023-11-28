from yolo5.entity.config_entity import ConfigurationManager
from yolo5.components.data_validation import DataValidation
from yolo5.exception import AppException
from yolo5.logger import logging
import sys


STAGE_NAME = 'Data Validation'


class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_validaton_config = config.get_data_validaton_config()
        data_validaton = DataValidation(data_validaton_config)
        data_validaton.check_valid()


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logging.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise AppException(e, sys)
