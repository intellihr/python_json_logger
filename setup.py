import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'json_logger'))
from version import VERSION

long_description = '''
Allow standard python logging to output log data as json objects.
'''

install_requires = [
    "requests>=2.18,<3.0",
    "six>=1.11",
    "PyJWT>=1.5.3",
    "python-dateutil>=2.6"
]

setup(
    name='event_bus_python',
    version=VERSION,
    url='https://github.com/intellihr/python_json_logger',
    author='intellihr',
    author_email='admin@intellihr.com.au',
    maintainer='intellihr',
    packages=['json_logger'],
    install_requires=install_requires,
    description='intellihr standard json logging formatter for python',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6"
    ]
)
