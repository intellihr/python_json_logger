import os
import re
import json
import logging
import uuid
import socket
from datetime import date, datetime, time, timezone

STANDARD_FORMATTERS = re.compile(r'\((.+?)\)', re.IGNORECASE)

default_log_dict = dict(
    service=os.environ.get('APP_NAME'),
    environment=os.environ.get('ENV_TYPE'),
    region=os.environ.get('AWS_DEFAULT_REGION'),
    host=socket.gethostname()
)


class JsonFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        logging.Formatter.__init__(self, *args, **kwargs)

    def format(self, record):
        log_record = self._make_log_record(record)

        return json.dumps(log_record, cls=JsonLogEncoder)

    def _make_log_record(self, record):
        log_record = dict(
            level=record.levelname.lower(),
            timestamp=datetime.fromtimestamp(
                record.created, tz=timezone.utc).isoformat()
        )
        if isinstance(record.msg, dict):
            log_record['data'] = record.msg
        else:
            log_record['message'] = record.getMessage()

        log_record.update(default_log_dict)

        return log_record


class JsonLogEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, datetime, time)):
            return obj.isoformat()
        if isinstance(obj, uuid.UUID):
            return str(obj)

        return json.JSONEncoder.default(self, obj)
