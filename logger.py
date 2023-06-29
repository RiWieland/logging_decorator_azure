import os
import logging

class Loggers_Base:
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


class Loggers_Decorators:
    '''
    Concrete implementation for logging decorator
    '''
    def __init__(self, logger_):
        self.logger_ = logger_

