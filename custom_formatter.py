from pythonjsonlogger import jsonlogger


class JsonFormatter(jsonlogger.JsonFormatter):
    def parse(self):
        return [
            'asctime',
            'levelname',
            'name',
            'funcName',
            'lineno',
            'threadName',
            'message',
            'created'
        ]

    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        del log_record["taskName"]
