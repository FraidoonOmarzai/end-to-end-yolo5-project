from dataclasses import dataclass
from pathlib import Path

from yolo5.constant import *
from yolo5.logger import logging
from yolo5.utils.main_utils import read_yaml, create_directories


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: str
    unzip_dir: Path


@dataclass
class DataValidationConfig:
    root_dir: Path
    data_path: Path
    list_dir: list
    status: str


class ConfigurationManager:
    def __init__(self, config=CONFIG_PATH) -> None:
        self.config = read_yaml(config)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        logging.info("get_data_ingestion_config")
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config

    def get_data_validaton_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])

        data_validaton_config = DataValidationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            list_dir=config.list_dir,
            status=config.status
        )
        return data_validaton_config
