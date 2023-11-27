from dataclasses import dataclass
from pathlib import Path

from src.yolo5.constant import *
from src.yolo5.logger import logging
from src.yolo5.utils.main_utils import read_yaml, create_directories


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: str
    unzip_dir: Path


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
