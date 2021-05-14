import logging
from config import conf
import os


class LoggerHandler:
    """ 日志操作 """

    def __init__(self):
        log_path = self.log_path[:self.log_path.rfind('/')]
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        # 创建日志对象
        self.logger = logging.getLogger()
        # 设置日志级别o
        # self.logger.setLevel(self.logger_level)
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

            # 设置日志输出流
            f_file = logging.FileHandler(self.log_path, encoding='utf-8')
            f_file.setLevel(logging.INFO)

            # # 设置输出流级别
            f_stream = logging.StreamHandler()
            f_stream.setLevel(logging.INFO)

            # 设置日志输出格式
            formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
            f_stream.setFormatter(formatter)
            f_file.setFormatter(formatter)

            # 给logger添加handler
            self.logger.addHandler(f_stream)
            self.logger.addHandler(f_file)

    @property
    def log_path(self):
        return conf.LOG_FILE_NAME


logger = LoggerHandler().logger
# def logger():
#     if not os.path.exists(conf.LOG_FOLDER):
#         os.mkdir(conf.LOG_FOLDER)
#     return LoggerHandler().get_logger

