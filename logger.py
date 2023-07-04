import os
import logging
import functools

class Logger_Base:
    '''
    Base class for logger to app insights
    '''
    def initialize_logger(self, name=None):
        
        logging.basicConfig(level=logging.INFO)
        logger_.setLevel('INFO')
        conn_str = (f'InstrumentationKey={os.environ["XXX"]}') # Environmental Variable

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
       
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            self.logger_.info(f"function {func.__name__} called with args {signature}")
            result = func(*args, **kwargs)
            return result
        return decorator
