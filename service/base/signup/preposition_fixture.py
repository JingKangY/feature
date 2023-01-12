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


@pytest.fixture(scope='module')
def connect_db():
    dbinfo = get_dbinfo_formal()
    connect_mysql.connect(dbinfo)
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


# 初始化注册接口数据库数据
@pytest.fixture(scope='class')
def test_signup_clear():
    connect_mysql.delete_one("DELETE FROM info WHERE name='成功注册用户'")
    connect_mysql.delete_one("DELETE FROM users WHERE username='test06'")
    connect_mysql.delete_one("DELETE FROM info WHERE name='注册密码为空用户'")
    connect_mysql.delete_one("DELETE FROM info WHERE name='注册确认密码为空用户'")
    connect_mysql.delete_one("DELETE FROM users WHERE username='test08'")
    connect_mysql.delete_one("DELETE FROM users WHERE username='test09'")
    connect_mysql.delete_one("DELETE FROM info WHERE name='注册两个密码不一致用户'")
    connect_mysql.delete_one("DELETE FROM users WHERE username='test10'")
    connect_mysql.delete_one("DELETE FROM info WHERE id=7")
    connect_mysql.delete_one("DELETE FROM users WHERE id=7")
    connect_mysql.insert_one("INSERT INTO users(id, username, password) VALUES(7, 'test11', md5('123456'))")
    connect_mysql.insert_one("INSERT INTO info(id, name) VALUES(7, '重复注册用户')")
    connect_mysql.delete_one("DELETE FROM info WHERE name='中文注册用户'")
    connect_mysql.delete_one("DELETE FROM users WHERE username='阳靖康'")
    connect_mysql.delete_one("DELETE FROM info WHERE name='特殊字符用户'")
    connect_mysql.delete_one("DELETE FROM users WHERE username='%￥#@&*'")
    connect_mysql.delete_one("DELETE FROM info WHERE name='注册密码为中文'")
    connect_mysql.delete_one("DELETE FROM users WHERE username='test12'")
