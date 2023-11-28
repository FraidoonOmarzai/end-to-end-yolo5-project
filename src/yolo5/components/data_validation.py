from yolo5.logger import logging
from yolo5.exception import AppException
from yolo5.entity.config_entity import DataValidationConfig
import sys
import os


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def check_valid(self):
        files = os.listdir(self.config.data_path)

        for file in files:
            if file not in self.config.list_dir:
                validation_status = False
                with open(self.config.status, 'w') as f:
                    f.write(f"file exist: {validation_status}")
                logging.info(f"file exist: {validation_status}")
            else:
                validation_status = True
                with open(self.config.status, 'w') as f:
                    f.write(f"file exist: {validation_status}")
                logging.info(f"file exist: {validation_status}")
