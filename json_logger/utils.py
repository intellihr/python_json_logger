PATCHED_LOGGER_METHODS = ('debug', 'info', 'warning', 'error', 'critical')


class LoggerAdapter:
    def __init__(self, logger, args_adapter):
        self.logger = logger
        self.args_adapter = args_adapter

    def __getattr__(self, name):
        method = getattr(self.logger, name)

        if name not in PATCHED_LOGGER_METHODS:
            return method

        return _wrap_logger_method(method, self.args_adapter)


def adapt_logger(logger, args_adapter):
    return LoggerAdapter(logger, args_adapter)


def to_api_logger(logger):
    """
    this utility assumes request and response are coming from falcon.
    e.g. http://falcon.readthedocs.io/en/stable/api/request_and_response.html
    """
    def api_logger_adapter(msg, *args, **kwargs):
        extra = {}
        request = kwargs.pop('request', None)
        if request:
            path = request.path
            if request.query_string:
                path += '?' + request.query_string
                extra['path'] = path

        response = kwargs.pop('response', None)
        if response and response.status:
            extra['status'] = int(response.status.split()[0])

        extra.update(kwargs.get('extra', {}))
        kwargs['extra'] = extra

        return msg, args, kwargs

    return adapt_logger(logger, api_logger_adapter)


def _wrap_logger_method(base_method, args_adapter):
    def wrapped(msg, *args, **kwargs):
        msg, args, kwargs = args_adapter(msg, *args, **kwargs)

        return base_method(msg, *args, **kwargs)

    return wrapped
