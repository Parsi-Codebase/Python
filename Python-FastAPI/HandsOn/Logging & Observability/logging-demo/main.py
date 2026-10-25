import logging # logging module is used to log messages in Python. It provides a way to configure different log levels and output formats. In this code snippet, we are setting up basic logging configuration and logging messages at different severity levels.
#configuring the logging module to log messages at the DEBUG level and above. This means that all messages with a severity level of DEBUG, INFO, WARNING, ERROR, and CRITICAL will be logged.
logging.basicConfig(
    level=logging.DEBUG
)
# Creating a logger object with the name of the current module. This allows us to log messages specific to this module and helps in identifying the source of the log messages when analyzing logs.
logger=logging.getLogger(__name__)
logger.debug('debug message')
logger.info('Application started')
logger.warning('low disk space')
logger.error('database connection failed')
logger.critical('application can not start')
