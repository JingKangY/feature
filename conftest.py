import pytest
from common.mysql import *
# from service.base.login.public_method import get_username_password


# '''
# 方法：fixture(scope="function", params=None, autouse=False, ids=None, name=None)
# 常用参数:
# scope：被标记方法的作用域  session>module>class>function
# function" (default)：作用于每个测试方法，每个test都运行一次
# "class"：作用于整个类，每个class的所有test只运行一次 一个类中可以有多个方法
# "module"：作用于整个模块，每个module的所有test只运行一次；每一个.py文件调用一次，该文件内又有多个function和class
# "session：作用于整个session(慎用)，每个session只运行一次；是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
# params：(list类型)提供参数数据，供调用标记方法的函数使用；一个可选的参数列表，它将导致多个参数调用fixture功能和所有测试使用它。
# autouse：是否自动运行,默认为False不运行，设置为True自动运行；如果True，则为所有测试激活fixture func可以看到它
# '''
#
#
# 执行前打开数据库--执行后关闭数据库
# @pytest.fixture(scope='class')
# def connect_db():
#     connect_mysql.connect()
#     connect_db = connect_mysql
#     yield connect_db
#     connect_db.close_db()
# 连接数据库 关闭数据库
# @pytest.fixture(scope='module')
# def connect_db():
#     connect_mysql.connect()
#     connect_db = connect_mysql
#     yield connect_db
#     connect_db.close_db()



# # 初始化登录接口数据库数据
# @pytest.fixture(scope='class')
# def test_login_clear():
#     connect_mysql.delete_one("DELETE FROM info WHERE id=4")
#     connect_mysql.delete_one("DELETE FROM users WHERE id=4")
#     connect_mysql.insert_one("INSERT INTO users(id, username, password) VALUES(4, 'test01', md5('123456'))")
#     connect_mysql.delete_one("DELETE FROM info WHERE id=5")
#     connect_mysql.delete_one("DELETE FROM users WHERE id=5")
#     connect_mysql.insert_one("INSERT INTO users(id, username, password) VALUES(5, 'test02', md5('123456'))")
#     connect_mysql.delete_one("INSERT INTO info(id, name) VALUES(5, '登录密码为空用户')")
#     connect_mysql.delete_one("DELETE FROM info WHERE name='登录用户名错误用户'")
#     connect_mysql.delete_one("DELETE FROM users WHERE username='test03'")
#     connect_mysql.delete_one("DELETE FROM info WHERE id=6")
#     connect_mysql.delete_one("DELETE FROM users WHERE id=6")
#     connect_mysql.insert_one("INSERT INTO users(id, username, password) VALUES(6, 'test04', md5('123456'))")
#     connect_mysql.delete_one("INSERT INTO info(id, name) VALUES(6, '登录密码错误用户')")
#     connect_mysql.delete_one("DELETE FROM info WHERE name='登录用户名与密码均错误用户'")
#     connect_mysql.delete_one("DELETE FROM users WHERE username='test05'")
#     connect_mysql.delete_one("DELETE FROM info WHERE id=8")
#     connect_mysql.delete_one("DELETE FROM users WHERE id=8")
#     connect_mysql.insert_one("INSERT INTO users(id, username, password) VALUES(8, 'test15', md5('123456'))")
#     connect_mysql.delete_one("INSERT INTO info(id, name) VALUES(8, '密码超过限制长度')")
#
#

