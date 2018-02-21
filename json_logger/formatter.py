import os
import json
import logging
import uuid
import socket
import traceback
from datetime import date, datetime, time, timezone
from inspect import istraceback, isclass

JSON_LOG_INDENT = int(os.environ.get('JSON_LOG_INDENT')) \
    if os.environ.get('JSON_LOG_INDENT') else None

RESERVED_ATTRS = (
    'args', 'asctime', 'created', 'exc_info', 'exc_text', 'filename',
    'funcName', 'levelname', 'levelno', 'lineno', 'module',
    'msecs', 'message', 'msg', 'name', 'pathname', 'process',
    'processName', 'relativeCreated', 'stack_info', 'thread', 'threadName')

TOP_LEVEL_ATTRS = ('level', 'service', 'user', 'environment',
                   'host', 'tags', 'message', 'tenant', 'timestamp',
                   'path', 'status')

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

        return json.dumps(log_record,
                          cls=JsonLogEncoder, indent=JSON_LOG_INDENT)

    def _make_log_record(self, record):
        log_record = dict(
            level=record.levelname.lower(),
            timestamp=datetime.fromtimestamp(
                record.created, tz=timezone.utc).isoformat()
        )
        if isinstance(record.msg, dict):
            log_record['data'] = record.msg
        elif isinstance(record.msg, Exception):
            if record.exc_info is None:
                log_record['message'] = 'exception: %s' % str(record.msg)
        else:
            log_record['message'] = record.getMessage()

        log_record.update(default_log_dict)

        # merge extra.attrs into top level attrs
        for key, value in record.__dict__.items():
            if key in RESERVED_ATTRS:
                continue
            if key in TOP_LEVEL_ATTRS:
                log_record[key] = value

        data = log_record.get('data', {})

        # merge extra.data into main data body
        if hasattr(record, 'data'):
            data.update(getattr(record, 'data'))

        # include exception detail when available
        if record.exc_info is not None:
            data['_exc_info'] = dict(
                exception=record.exc_info[0],
                msg=record.exc_info[1],
                traceback=record.exc_info[2]
            )

        # provide extra code context detail in debug mode
        if record.levelname == 'DEBUG':
            data['_code'] = dict(
                pathname=record.pathname,
                lineno=record.lineno,
                func_name=record.funcName
            )

        if data:
            log_record['data'] = data

        return log_record


class JsonLogEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, datetime, time)):
            return obj.isoformat()
        elif isclass(obj):
            return obj.__name__
        elif isinstance(obj, Exception):
            return 'exception: %s' % str(obj)
        elif istraceback(obj):
            tb = ''.join(traceback.format_tb(obj))
            return tb.strip()
        elif isinstance(obj, uuid.UUID):
            return str(obj)

        return json.JSONEncoder.default(self, obj)
