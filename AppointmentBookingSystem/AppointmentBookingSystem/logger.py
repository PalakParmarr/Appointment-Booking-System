import logging
from concurrent.futures.thread import ThreadPoolExecutor
# from AppointmentBookingSystem.settings import DEBUG, LOGS_PATH
from logging.handlers import RotatingFileHandler
import logging


class AppLogger:
    """
    App Logger will maintain all logs of this project. Handles two types of logging.

    a.  `StreamHandler`: Used for stderr error or stdout.
    b.  `RotatingFileHandler`: Used for enter logs in log file.
    """
    # LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    #
    # # logging.basicConfig(filename=LOGS_PATH, format=LOG_FORMAT, datefmt='%m/%d/%Y %I:%M:%S %p')
    logger = logging.getLogger(__name__)
    #
    # # File Handler
    # rotating_file_handler = RotatingFileHandler(
    #     filename=LOGS_PATH, maxBytes=10 * 1024, backupCount=2, mode='a'
    # )
    # # set format of log - how you want your logs to be formatted
    # formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt='%m/%d/%Y %I:%M:%S %p')
    # # set format to formatter
    # rotating_file_handler.setFormatter(formatter)
    # logger.addHandler(rotating_file_handler)
    #
    # # Console Handler
    # console_handler = logging.StreamHandler()
    # console_handler.setFormatter(formatter)
    # logger.addHandler(console_handler)

    def __init__(self):
        super().__init__()


    def data_formatter(self, e):
        data = dict(
            class_name=e['class_object'].__class__.__name__,
            method_name=e['class_object'].request.method,
            errors=e['error']
        )
        return data

    def log_error(self, e, *args, **kwargs):
        """
        This method will be use for `logging.error`.

        :param e: error
        :param kwargs:  exc_info: True
        :return:
        """
        self.async_logger(func=self.logger.error, msg=self.data_formatter(e))

    def log_debug(self, e, *args, **kwargs):
        """
        This method will be use for `logging.debug`. Will work only if `DEBUG = True`.
        :param e: error
        :param kwargs:  exc_info: True
        :return:
        """
        self.async_logger(func=self.logger.debug, msg=self.data_formatter(e))

    def log_info(self, e, *args, **kwargs):
        """
        This method will be use for `logging.info`.

        :param e: error
        :param kwargs:  exc_info: True
        :return:
        """
        self.async_logger(func=self.logger.info, msg=self.data_formatter(e))

    def log_warning(self, e, *args, **kwargs):
        """
        This method will be use for `logging.warning`.

        :param e: error
        :param kwargs:  exc_info: True
        :return:
        """
        self.async_logger(func=self.logger.warning, msg=self.data_formatter(e))

    def log_critical(self, e, *args, **kwargs):
        """
        This method will be use for `logging.critical`.

        :param e: error
        :param kwargs:  exc_info: True
        :return:
        """
        self.async_logger(func=self.logger.critical, msg=self.data_formatter(e))

    def log_exception(self, e, *args, **kwargs):
        """
        This method will be use for `logging.exception`.
        :param e: error
        :param kwargs:  exc_info: True
        :return:
        """
        self.async_logger(func=self.logger.exception, msg=self.data_formatter(e))

    def async_logger(self, func, **kwargs):
        """
        This method handles asynchronous calls for logging.

        :param func: Function name that we are going to execute.
        :param kwargs:
        :return:
        """
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(func(**kwargs))
