import os
import logging
import json
from io import StringIO
from collections import namedtuple

import pytest


class LoggerContext(namedtuple('LoggerContext', 'logger buffer')):
    __slots__ = ()

    @property
    def output(self):
        text = self.buffer.getvalue()

        return json.loads(text)


@pytest.fixture
def logger_context():
    os.environ['APP_NAME'] = 'test_app'
    os.environ['ENV_TYPE'] = 'prod'
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'

    from json_logger.formatter import JsonFormatter

    logger = logging.getLogger('logging-test')
    logger.setLevel(logging.DEBUG)
    buffer = StringIO()

    handler = logging.StreamHandler(buffer)
    handler.setFormatter(JsonFormatter())

    logger.addHandler(handler)

    return LoggerContext(logger, buffer)


@pytest.mark.freeze_time('2018-02-14')
def test_simple_info_log(snapshot, logger_context):
    logger_context.logger.info('test simple text message!')

    snapshot.assert_match(logger_context.output)
