import os
import logging
import functools

from opencensus.ext.azure.log_exporter import AzureLogHandler

class Logger_Base:
    '''
    Base class for logger to app insights
    '''
    def initialize_logger(self, name=None):
        logging.basicConfig(level=logging.INFO)
        if name==None:
            logger_ = logging.getLogger(self.__class__.__name__)
        else:
            logger_ = logging.getLogger(name)
        logger_.setLevel('INFO')
        conn_str = (f'InstrumentationKey={os.environ["APPINSIGHT_KEY"]}') # Environmental Variable

        logger_.addHandler(    
        AzureLogHandler(
            connection_string=conn_str,
            export_interval=1,  
            logging_sampling_rate=1))  

        logger_: logging.Logger = logger_
        return logger_


class Logger_Decorators:
    '''
    Concrete implementation for logging decorator
    '''
    def __init__(self, logger_):
        self.logger_ = logger_

    def send_logs(self):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    args_repr = [repr(a) for a in args]
                    kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
                    signature = ", ".join(args_repr + kwargs_repr)
                    self.logger_.info(f"function {func.__name__} called with args {signature}")
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    self.logger_.exception(f"Exception raised in function {func.__name__}. Exception: {str(e)}")
                    self.logger_.warning(f"function {func.__name__} called with args {signature} and thrown an error {str(e)}")
            return decorator

app_logger = Loggers_Base()
app_logger = app_logger.initialize_logger()
log_decorator = Loggers_Decorators(app_logger)
