# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_simple_info_log 1'] = {
    'environment': 'prod',
    'host': 'bca68d5b0a9a',
    'level': 'info',
    'message': 'test simple text message!',
    'region': 'us-east-2',
    'service': 'test_app',
    'timestamp': '2018-02-14T00:00:00+00:00'
}
