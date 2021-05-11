import logging
from config import conf
import os


class LoggerHandler:
    """ 日志操作 """

    def __init__(self, log_name, file_name):
        self.log_name = log_name
        self.file_name = file_name
        # 创建日志对象
        self.logger = logging.getLogger(self.log_name)
        # 设置日志级别o
        # self.logger.setLevel(self.logger_level)
        if not self.logger.handlers:
            # 设置日志输出流
            f_stream = logging.StreamHandler()
            f_file = logging.FileHandler(self.file_name, encoding='utf-8')
            # # 设置输出流级别
            # f_stream.setLevel(self.stream_level)
            # f_file.setLevel(logging.INFO)
            # 设置日志输出格式
            formatter = logging.Formatter(
                "%(asctime)s %(name)s %(levelname)s %(message)s"
            )
            f_stream.setFormatter(formatter)
            f_file.setFormatter(formatter)
            # 给logger添加handler
            self.logger.addHandler(f_stream)
            self.logger.addHandler(f_file)

    @property
    def get_logger(self):
        return self.logger


def logger(log_name):
    if not os.path.exists(conf.LOG_FOLDER):
        os.mkdir(conf.LOG_FOLDER)
    return LoggerHandler(log_name, conf.LOG_FILE_NAME).get_logger

