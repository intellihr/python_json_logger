# Overview

This library is designed for providing JSON logging for python micro services.
It is an opinionated framework and assume certain environment variables to exist.

# Installing

Pip:

```
    pip install https://github.com/intellihr/python_json_logger/archive/v0.0.3.zip
```


# Usage

## Required Environment variables

- *APP_NAME* - mapped to `service`
- *ENV_TYPE* - mapped to `environment`
- *AWS_REGION* or *AWS_DEFAULT_REGION* - mapped to `region`

## Integrating with Python's logging framework

Json outputs are provided by the JsonFormatter logging formatter. You can add the customer formatter like below:

```python
    import logging
    from json_logger.formatter import JsonFormatter

    logger = logging.getLogger()

    logHandler = logging.StreamHandler()
    formatter = JsonFormatter()
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
```

## Using a Config File

To use the module with a config file using the [`fileConfig` function](https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig), use the class `json_logger.formatter.JsonFormatter`. Here is a sample config file.

```ini
[loggers]
keys = root,custom

[logger_root]
handlers =

[logger_custom]
level = INFO
handlers = custom
qualname = custom

[handlers]
keys = custom

[handler_custom]
class = StreamHandler
level = INFO
formatter = json
args = (sys.stdout,)

[formatters]
keys = json

[formatter_json]
class = json_logger.formatter.JsonFormatter
```

## Example Output

```json
{
  "data": {
    "a": 1,
    "b": [
      1,
      2,
      "fd2ea794-8605-4067-9152-33529ca96807"
    ],
    "c": "2017-01-02T00:00:00"
  },
  "environment": "prod",
  "host": "testhost",
  "level": "info",
  "region": "us-east-2",
  "service": "test_app",
  "timestamp": "2018-02-14T00:00:00+00:00"
}
```

For more examples, please refer to: https://github.com/intellihr/python_json_logger/blob/master/tests/snapshots/snap_test_logger.py


## Logging Adapter

`json_logger.utils.adapt_logger` provides an utility logging adapter to map logging parameters
into special field. For more detail please refer to the `json_logger.utils.to_api_logger` as example.

# Build and Run Test

```bash
docker-compose run --rm local make
```


# Version and JSON Logging Format Standard Mapping

Based on: https://intellihr.atlassian.net/wiki/spaces/DG/pages/284983300/Logging+Format

- `v0.0.1` (mapped to format standard version `0.0.1`)
- `v0.0.2` (mapped to format standard version `0.0.1`)
  - add support for JSON_LOG_INDENT (basically json prettify)
- `v0.0.3` (mapped to format standard version `0.0.1`)
  - support both AWS_REGION and AWS_DEFAULT_REGION
- `v0.0.4` (mapped to format standard version `0.0.1`)
  - change log level from error to err
- `v0.0.5` (mapped to format standard version `0.0.1`)
  - support log set type
- `v0.0.6` (mapped to format standard version `0.0.1`)
  - fix bug for non-scriptable exc_info
