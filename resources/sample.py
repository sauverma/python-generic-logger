from generic_logging.gen_logger import *

GenLogger.LOGGING_CONFIG = {
    'loggerName': 'listServiceLogger',
    'loggingConfigPath': './conf/logging.yaml'
}

GenLogger.init()

GenLogger.get_logger().info('Sample log')
