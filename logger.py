import os
import logging

class Loggers_Base:
    '''
    Logging Class for initialize the logging into Azure Application Insights
    '''
    def initialize_logger(self, name=None):
        
        logging.basicConfig(level=logging.INFO)
        logger_.setLevel('INFO')
        conn_str = (f'InstrumentationKey={os.environ["XXX"]}') # Environmental Variable

        logger_.addHandler(    
        AzureLogHandler(
            connection_string=conn_str,
            export_interval=1,  # Small interval to make sure all metrics are exported
            logging_sampling_rate=1))  # Highest possible sampling rate to be safe

        logger_: logging.Logger = logger_
        return logger_


class Loggers_Decorators:
    '''
    Class for a decorator for logging
    '''
    def __init__(self, logger_):
        self.logger_ = logger_

