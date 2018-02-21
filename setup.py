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

install_requires = []

setup(
    name='python_json_logger',
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
