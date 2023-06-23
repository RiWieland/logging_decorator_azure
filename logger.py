import os
import logging

class Loggers_Base:
    '''
    Logging Class for initialize the logging into Azure Application Insights
    '''
    def initialize_logger(self, name=None):
        logging.basicConfig(level=logging.INFO)
        logger_.setLevel('INFO')
        conn_str = (f'InstrumentationKey={os.environ["APPINSIGHTS_INSTRUMENTATIONKEY"]}')
        logger_: logging.Logger = logger_
        return logger_
