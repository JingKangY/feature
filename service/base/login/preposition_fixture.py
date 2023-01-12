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

from data.get_data import read
from loging.log import *
from common.mysql import *
from confs.conf import *
from testcase.public_method import *


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


# 前置数据库获取账户信息
@pytest.fixture(scope="class")
def get_usernm_passwd():
    try:
        log.info(f'==========开始获取获取用户信息==========')
        username = get_username_password("SELECT username FROM `users` WHERE id = '1'")
        password = get_username_password("SELECT password FROM `users` WHERE id = '1'")
        log.info(f'==========成功获取用户信息：{username},{password} ==========')
        yield username, password
    except Exception as e:
        log.error(f'==========获取用户信息失败，错误原因：{e}==========')
        raise e


@pytest.fixture(scope='class')
def test_login_clear():
    connect_mysql.delete_one("DELETE FROM info WHERE id=4")
    connect_mysql.delete_one("DELETE FROM users WHERE id=4")
    connect_mysql.insert_one("INSERT INTO users(id, username, password) VALUES(4, 'test01', md5('123456'))")
    connect_mysql.delete_one("DELETE FROM info WHERE id=5")
    connect_mysql.delete_one("DELETE FROM users WHERE id=5")
    connect_mysql.insert_one("INSERT INTO users(id, username, password) VALUES(5, 'test02', md5('123456'))")
    connect_mysql.delete_one("INSERT INTO info(id, name) VALUES(5, '登录密码为空用户')")
    connect_mysql.delete_one("DELETE FROM info WHERE name='登录用户名错误用户'")
    connect_mysql.delete_one("DELETE FROM users WHERE username='test03'")
    connect_mysql.delete_one("DELETE FROM info WHERE id=6")
    connect_mysql.delete_one("DELETE FROM users WHERE id=6")
    connect_mysql.insert_one("INSERT INTO users(id, username, password) VALUES(6, 'test04', md5('123456'))")
    connect_mysql.delete_one("INSERT INTO info(id, name) VALUES(6, '登录密码错误用户')")
    connect_mysql.delete_one("DELETE FROM info WHERE name='登录用户名与密码均错误用户'")
    connect_mysql.delete_one("DELETE FROM users WHERE username='test05'")
    connect_mysql.delete_one("DELETE FROM info WHERE id=8")
    connect_mysql.delete_one("DELETE FROM users WHERE id=8")
    connect_mysql.insert_one("INSERT INTO users(id, username, password) VALUES(8, 'test15', md5('123456'))")
    connect_mysql.delete_one("INSERT INTO info(id, name) VALUES(8, '密码超过限制长度')")


# 获取token，然后写入数据库 有的时候网址会失效 所以说获取token前置有的时候需要干掉
@pytest.fixture(scope='module')
def insert_token_first():
    cookie = get_cookie('http://124.223.214.171:8080/integration/login', 'post', {
        "data": {
            "password": "12345678",
            "userName": "root"
        }})
    args = read.read_all_excel(GetFilePath().get_all_file_path(r'data/双创wa项目接口文档.xlsx'), '获取token')
    token = get_login_token(url=get_server_other() + args[0][0], method=args[0][1], cookie=cookie)
    insert_token(token)


# 获取数据库中存储的token
@pytest.fixture(scope='class')
def get_token():
    db_token = get_mysql_token("SELECT token_value FROM wa_test.token")
    yield db_token
