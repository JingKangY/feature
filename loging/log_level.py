# coding=utf-8

import logging

LOG_FILE = 'Debug.log'

# file_handler = logging.FileHandler(LOG_FILE.encode('utf-8'))  # 输出到文件
file_handler = logging.FileHandler(filename=LOG_FILE, encoding='UTF-8')  # 输出到文件
console_handler = logging.StreamHandler()  # 输出到控制台
file_handler.setLevel('INFO')  # info以上才输出到文件
console_handler.setLevel('INFO')  # info以上才输出到控制台

fmt = '日志日期：%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
fmt1 = "日志日期：%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d:%(message)s"
formatter = logging.Formatter(fmt)

file_handler.setFormatter(formatter)  # 设置输出内容的格式
console_handler.setFormatter(formatter)

logger = logging.getLogger('updateSecurity')  # 创建日志收集器
logger.setLevel('DEBUG')  # 设置了这个才会把debug以上的输出到控制台

logger.addHandler(file_handler)  # 添加handler
logger.addHandler(console_handler)


def lg_debug(debug):
    logger.debug(debug)


def lg_info(info):
    logger.info(info)


def lg_warning(warning):
    logger.warning(warning)


def lg_error(error):
    logger.error(error)


def lg_critical(critical):
    logger.critical(critical)


if __name__ == '__main__':
    # lg_info('nihao')
    lg_debug('好啊啊')
    lg_error('error')
