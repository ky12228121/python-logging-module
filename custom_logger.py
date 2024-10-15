import logging
import logging.config
import yaml
from typing import Self


class CustomLogger:
    def __init__(self, name: str, filepath: str):
        self._load_logconfig(filepath)
        self.logger = logging.getLogger(name)

    def _load_logconfig(self, filepath: str):
        with open(filepath, "r") as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)

    @classmethod
    def get_logger(cls, name: str, filepath: str) -> Self:
        return cls(name, filepath).logger
