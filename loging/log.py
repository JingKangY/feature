# coding=utf-8
'''
@File    :   log.py
@Time    :   2022/7/19 8:30
@Author  :   YangJingKang(靖康阳)
@Gitee   :   https://gitee.com/jingkangyang/
@Jianshu :   靖康阳
@Contact :   1097904758@qq.com
@License :   (C)Copyright 2022-2025, Micro-Circle
@Desc    :   日志封装
'''

import logging
import os
from logging.handlers import RotatingFileHandler
import colorlog

log_colors_config = {
    "DEBUG": "bold_blue",
    "INFO": "bold_green",
    "WARNING": "bold_yellow",
    "ERROR": "bold_red",
    "CRITICAL": "bold_purple",
}


class Log(object):
    """
    日志封装，带颜色的
    """

    def __init__(self, logname='LogFile.log'):
        self.logname = os.path.join('%s' % logname)
        self.logger = logging.getLogger()  # 创建日志对象
        self.logger.setLevel(logging.DEBUG)  # 设置日志输出登记
        # 设置日志输出格式
        self.formatter1 = logging.Formatter(
            '%(levelname)1.1s %(asctime)s| %(levelname)-8s | [%(filename)s:%(module)s:%(funcName)s:%(lineno)d] - %(message)s')
        self.formatter = colorlog.ColoredFormatter(
            "%(log_color)s%(levelname)1.1s %(log_color)s%(asctime)s%(reset)s| %(message_log_color)s%(levelname)-8s %(reset)s| %("
            "log_color)s[%(filename)s%(reset)s:%(log_color)s%(module)s%(reset)s:%(log_color)s%(funcName)s%("
            "reset)s:%(log_color)s%(""lineno)d] %(reset)s- %(log_color)s%(message)s", reset=True,
            log_colors=log_colors_config,
            secondary_log_colors={
                "message": {
                    "DEBUG": "bold_blue",
                    "INFO": "bold_green",
                    "WARNING": "bold_yellow",
                    "ERROR": "bold_red",
                    "CRITICAL": "bold_purple"
                }
            },
            style="%"
        )  # 日志输出格式
        # 创建TimedRotatingFileHandler切割，用于输出到文件
        fh = logging.handlers.TimedRotatingFileHandler(self.logname, when='MIDNIGHT', interval=1, encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter1)  # 输出到本地日志，去掉颜色
        self.logger.addHandler(fh)
        # 创建一个StreamHandler，用于输出到控制台
        ch = logging.StreamHandler()  # 创建日志流处理器
        ch.setLevel(logging.DEBUG)  # 设置日志输出登记
        ch.setFormatter(self.formatter)  # 设置日志处理器输出格式
        self.logger.addHandler(ch)  # 日志处理器增加到日志对象

    def get_logger(self):
        """
        获取logger日志对象（栈）
        :return:日志对象
        """
        return self.logger


log = Log().get_logger()

if __name__ == '__main__':
    log.info('晚上好')
    log.debug('晚上好')
    log.error('晚上好')
    log.warning('晚上好')
    log.critical('晚上好')
