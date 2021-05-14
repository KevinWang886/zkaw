#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import datetime
import sys
import os
sys.path.append('.')


# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 页面元素目录
ELEMENT_PATH = os.path.join(BASE_DIR, 'element')

# 测试数据
TEST_DATA_PATH = os.path.join(BASE_DIR, 'test_data')


# ---------------- 日志相关 --------------------
# 日志级别
LOG_LEVEL = 'debug'
LOG_STREAM_LEVEL = 'debug'  # 屏幕输出流
LOG_FILE_LEVEL = 'info'   # 文件输出流
# 日志命名
LOG_FOLDER = os.path.join(BASE_DIR, 'logs')
LOG_FILE_NAME = os.path.join(LOG_FOLDER, '{}.log'.format(datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')))
