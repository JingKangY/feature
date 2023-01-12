# -*-coding = utf-8 -*-
'''
@File    :  preposition_fixture.py
@Time    :  2022-11-21 16:47
@Author  :  yangjingkang(靖康阳)
@Gitee   :  https://gitee.com/jingkangyang
@Jianshu :  靖康阳
@Contact :  1097904758@qq.com
@License :  (C)Copyright 2022--2025, Micro-Circle
@Software:  PyCharm
@Desc    :  文件内容描述
'''
# 初始化登录接口数据库数据
import pytest

from common.mysql import connect_mysql
from confs.conf import get_dbinfo_formal
from loging.log import *

# 连接数据库 关闭数据库
from testcase.public_method import *


# 获取数据库中存储的token
@pytest.fixture(scope='class')
def get_token():
    db_token = get_mysql_token("SELECT token_value FROM wa_test.token")
    yield db_token


# 连接数据库 关闭数据库
@pytest.fixture(scope='module')
def connect_db():
    connect_mysql.connect(get_dbinfo_formal())
    connect_db = connect_mysql
    try:
        log.info('*********************开始数据库连接*********************')
        yield connect_db
        log.info('*********************开始关闭数据库连接*********************')
        connect_db.close_db()
    except Exception as e:
        log.error('*********************连接数据库并关闭数据库失败*********************')
        log.error(f'数据库错误信息{e}')
        connect_db.close_db()
        raise e
