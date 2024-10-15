import logging


class ErrorFilter(logging.Filter):
    def filter(self, record) -> bool:
        return record.levelno >= logging.ERROR
