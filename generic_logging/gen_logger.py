import logging
import logging.config
import yaml
from .exceptions import *

class GenLogger():
    initialized = False
    _logger = None
    LOGGING_CONFIG = None

    # this structure is of below form
    #
    # {
    #   'loggerName' : '',
    #   'loggingConfigPath' : '',
    # }

    @staticmethod
    def is_init():
        return GenLogger.initialized

    @staticmethod
    def validate_config():
        if GenLogger.LOGGING_CONFIG is None:
            return False

        return True

    @staticmethod
    def init():
        if GenLogger.initialized:
            raise GenLoggerInitError('ZeoLogger has already been init... use ZeoLogger.get_logger()')

        if GenLogger.validate_config():
            GenLogger.initialized = True
            config = None
            with open(GenLogger.LOGGING_CONFIG['loggingConfigPath'], 'r') as stream:
                config = yaml.load(stream)

            if config is None:
                raise GenLoggerInitError('Invalid logging config passed : %s',
                                         GenLogger.LOGGING_CONFIG['loggingConfigPath'])

            logging.config.dictConfig(config)
            GenLogger._logger = logging.getLogger(GenLogger.LOGGING_CONFIG['loggerName'])

    @staticmethod
    def get_logger():
        if not GenLogger.initialized:
            raise GenLoggerInitError('ZeoLogger has not been init... use ZeoLogger.init() first')

        return GenLogger._logger
