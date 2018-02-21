import logging
import json
from io import StringIO
from collections import namedtuple
from datetime import datetime
import uuid
from unittest.mock import patch

import pytest

from json_logger.utils import to_api_logger


class LoggerContext(namedtuple('LoggerContext', 'logger buffer')):
    __slots__ = ()

    @property
    def output(self):
        text = self.buffer.getvalue()

        return json.loads(text)


@pytest.fixture
def logger_context():
    envs = {
        'APP_NAME': 'test_app',
        'ENV_TYPE': 'prod',
        'AWS_DEFAULT_REGION': 'us-east-2'
    }
    with patch.dict('os.environ', envs), \
            patch('socket.gethostname', return_value='testhost'):
        from json_logger.formatter import JsonFormatter

        logger = logging.getLogger('logging-test')
        logger.setLevel(logging.DEBUG)
        buffer = StringIO()

        handler = logging.StreamHandler(buffer)
        handler.setFormatter(JsonFormatter())

        logger.addHandler(handler)

        yield LoggerContext(logger, buffer)

        logger.removeHandler(handler)


@pytest.mark.freeze_time('2018-02-14')
def test_simple_info_log(snapshot, logger_context):
    logger_context.logger.info('test simple text message!')

    snapshot.assert_match(logger_context.output)


@pytest.mark.freeze_time('2018-02-14')
def test_info_log_with_interpolation(snapshot, logger_context):
    logger_context.logger.info('test simple text: %s', 'test')

    snapshot.assert_match(logger_context.output)


@pytest.mark.freeze_time('2018-02-14')
def test_info_log_with_structured_payload(snapshot, logger_context):
    msg = dict(
        a=1, b=[1, 2, uuid.UUID('fd2ea794-8605-4067-9152-33529ca96807')],
        c=datetime(2017, 1, 2))
    logger_context.logger.info(msg)

    snapshot.assert_match(logger_context.output)


@pytest.mark.freeze_time('2018-02-14')
def test_info_log_with_kwargs(snapshot, logger_context):
    logger_context.logger.info('test message', extra=dict(
        tags=['test'], user=uuid.UUID('fd2ea794-8605-4067-9152-33529ca96807')))

    snapshot.assert_match(logger_context.output)


@pytest.mark.freeze_time('2018-02-14')
def test_info_log_with_data(snapshot, logger_context):
    logger_context.logger.info('test message', extra=dict(
        tags=['test'], data=dict(a=1, b=2)))

    snapshot.assert_match(logger_context.output)


@pytest.mark.freeze_time('2018-02-14')
def test_info_log_exception(snapshot, logger_context):
    try:
        raise ValueError('value issue!')
    except ValueError as e:
        logger_context.logger.exception(e)

    snapshot.assert_match(logger_context.output)


@pytest.mark.freeze_time('2018-02-14')
def test_debug_log(snapshot, logger_context):
    logger_context.logger.debug('debug here!')

    snapshot.assert_match(logger_context.output)


@pytest.mark.freeze_time('2018-02-14')
def test_to_api_logger_log_request(snapshot, logger_context):
    falcon_request = namedtuple(
        'falcon_request', 'path query_string')('/test_route', 'a=1')
    api_logger = to_api_logger(logger_context.logger)
    api_logger.info('test request', request=falcon_request)

    snapshot.assert_match(logger_context.output)


@pytest.mark.freeze_time('2018-02-14')
def test_to_api_logger_log_response(snapshot, logger_context):
    falcon_response = namedtuple('falcon_request', 'status')('200 OK')
    api_logger = to_api_logger(logger_context.logger)
    api_logger.info('test response', response=falcon_response)

    snapshot.assert_match(logger_context.output)
