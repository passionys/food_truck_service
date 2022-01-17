from configparser import ConfigParser
import logging
from logging.handlers import RotatingFileHandler


class LoggerFactory:
    """
    Logger Factory keeping one logger per each log file
    """
    log_config_properties = None

    def __init__(self, log_properties_file_name):

        config_parser = ConfigParser()
        config_parser.read(log_properties_file_name)
        LoggerFactory.log_config_properties = dict(config_parser.items('log_config'))

    @classmethod
    def get_logger(cls) -> object:
        log_config_properties = cls.log_config_properties
        log_file_name = log_config_properties['log_file']
        my_logger = logging.getLogger(log_file_name)
        log_level = log_config_properties['log_level']
        file = '{0}/{1}'.format(log_config_properties['log_path'], log_config_properties['log_file'])
        handler = RotatingFileHandler(file,
                                      maxBytes=int(log_config_properties['log_max_bytes']),
                                      backupCount=int(log_config_properties['log_count']))
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s [%(process)s] [%(filename)s:%(lineno)d] - %(message)s')

        handler.setFormatter(formatter)
        my_logger.addHandler(handler)
        if log_level == 'DEBUG':
            my_logger.setLevel(logging.DEBUG)
        elif log_level == 'WARN':
            my_logger.setLevel(logging.WARN)
        else:
            my_logger.setLevel(logging.INFO)

        return my_logger
