# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_simple_info_log 1'] = {
    'environment': 'prod',
    'host': 'testhost',
    'level': 'info',
    'message': 'test simple text message!',
    'region': 'us-east-2',
    'service': 'test_app',
    'timestamp': '2018-02-14T00:00:00+00:00'
}

snapshots['test_info_log_with_interpolation 1'] = {
    'environment': 'prod',
    'host': 'testhost',
    'level': 'info',
    'message': 'test simple text: test',
    'region': 'us-east-2',
    'service': 'test_app',
    'timestamp': '2018-02-14T00:00:00+00:00'
}

snapshots['test_info_log_with_data 1'] = {
    'data': {
        'a': 1,
        'b': 2
    },
    'environment': 'prod',
    'host': 'testhost',
    'level': 'info',
    'message': 'test message',
    'region': 'us-east-2',
    'service': 'test_app',
    'tags': [
        'test'
    ],
    'timestamp': '2018-02-14T00:00:00+00:00'
}

snapshots['test_info_log_with_structured_payload 1'] = {
    'data': {
        'a': 1,
        'b': [
            1,
            2,
            'fd2ea794-8605-4067-9152-33529ca96807'
        ],
        'c': '2017-01-02T00:00:00'
    },
    'environment': 'prod',
    'host': 'testhost',
    'level': 'info',
    'region': 'us-east-2',
    'service': 'test_app',
    'timestamp': '2018-02-14T00:00:00+00:00'
}

snapshots['test_info_log_with_kwargs 1'] = {
    'environment': 'prod',
    'host': 'testhost',
    'level': 'info',
    'message': 'test message',
    'region': 'us-east-2',
    'service': 'test_app',
    'tags': [
        'test'
    ],
    'timestamp': '2018-02-14T00:00:00+00:00',
    'user': 'fd2ea794-8605-4067-9152-33529ca96807'
}

snapshots['test_info_log_exception 1'] = {
    'data': {
        '_exc_info': {
            'exception': 'ValueError',
            'msg': 'exception: value issue!',
            'traceback': '''File "/usr/src/app/tests/test_logger.py", line 96, in test_info_log_exception
    raise ValueError('value issue!')'''
        }
    },
    'environment': 'prod',
    'host': 'testhost',
    'level': 'err',
    'region': 'us-east-2',
    'service': 'test_app',
    'timestamp': '2018-02-14T00:00:00+00:00'
}

snapshots['test_debug_log 1'] = {
    'data': {
        '_code': {
            'func_name': 'test_debug_log',
            'lineno': 105,
            'pathname': '/usr/src/app/tests/test_logger.py'
        }
    },
    'environment': 'prod',
    'host': 'testhost',
    'level': 'debug',
    'message': 'debug here!',
    'region': 'us-east-2',
    'service': 'test_app',
    'timestamp': '2018-02-14T00:00:00+00:00'
}

snapshots['test_to_api_logger_log_request 1'] = {
    'environment': 'prod',
    'host': 'testhost',
    'level': 'info',
    'message': 'test request',
    'path': '/test_route?a=1',
    'region': 'us-east-2',
    'service': 'test_app',
    'timestamp': '2018-02-14T00:00:00+00:00'
}

snapshots['test_to_api_logger_log_response 1'] = {
    'environment': 'prod',
    'host': 'testhost',
    'level': 'info',
    'message': 'test response',
    'region': 'us-east-2',
    'service': 'test_app',
    'status': 200,
    'timestamp': '2018-02-14T00:00:00+00:00'
}

snapshots['test_warning_log 1'] = {
    'environment': 'prod',
    'host': 'testhost',
    'level': 'warning',
    'message': 'warning here!',
    'region': 'us-east-2',
    'service': 'test_app',
    'timestamp': '2018-02-14T00:00:00+00:00'
}

snapshots['test_critical_log 1'] = {
    'environment': 'prod',
    'host': 'testhost',
    'level': 'crit',
    'message': 'critical here!',
    'region': 'us-east-2',
    'service': 'test_app',
    'timestamp': '2018-02-14T00:00:00+00:00'
}
