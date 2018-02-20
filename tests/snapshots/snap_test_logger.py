# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

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
