# -*-coding = utf-8 -*-
'''
@File    :  public_method.py
@Time    :  2022-11-21 15:40
@Author  :  yangjingkang(靖康阳)
@Gitee   :  https://gitee.com/jingkangyang
@Jianshu :  靖康阳
@Contact :  1097904758@qq.com
@License :  (C)Copyright 2022--2025, Micro-Circle
@Software:  PyCharm
@Desc    :  文件内容描述
'''
import allure
import requests

from common.data_conversion import DataCoversion
from common.mysql import connect_mysql
from common.requeststart import RequestStart
from confs.conf import get_dbinfo_formal
from loging.log import *


@allure.step("获取用户账户、密码")
def get_username_password(sql):
    info_db = connect_mysql.select(sql)
    info_db = DataCoversion().tuple_to_str(info_db)
    # print(type(info_db))
    return info_db


def login_sc(url, method, args):
    data = {
        "url": url,
        "method": method,
        'json': args
    }
    res_actual = RequestStart().send_request(data)
    # cookies = requests.utils.dict_from_cookiejar(res_actual.cookies)
    # cookie = "; ".join([str(x) + "=" + str(y) for x, y in cookies.items()])
    print(res_actual.cookies)


# 1.获取请求头中的cookie
@allure.step('登录获取cookie')
def get_cookie(url, method, data):
    data = {
        "url": url,
        "method": method,
        'json': data
    }
    cookies = RequestStart().get_session_cookie(data)
    return cookies


@allure.step('获取登录后的token值')
def get_login_token(url, method, cookie):
    '''

    '''
    headers = {'cookie': cookie}
    data = {
        "url": url,
        "method": method,
        "headers": headers
    }
    res_actual = RequestStart().send_request(data)
    token = res_actual['token']['items']['OnClick_pButton_ctlSave_frmEditDivision_jssave']
    return token


@allure.step('初始化token、写入数据库存储的token值')
def insert_token(token):
    # 传入一个token进行写入
    # dbinfo = get_dbinfo_formal()
    # connect_mysql.connect(dbinfo)
    db_number = connect_mysql.selects("SELECT token_id,token_name,token_value FROM wa_test.token")
    print(db_number)
    if db_number != eval("()"):
        for i in db_number:
            connect_mysql.delete_one("DELETE FROM wa_test.token WHERE token_id = {}".format(i[0]))
        connect_mysql.insert_one(f"INSERT INTO wa_test.token VALUES (1,'token','{token}')")
    else:
        connect_mysql.insert_one(f"INSERT INTO wa_test.token VALUES (1,'token','{token}')")


@allure.step('获取数据库存储的token值')
def get_mysql_token(sql):
    # connect_mysql.connect(get_dbinfo_formal()) # 连接数据库已经连接 不用再次连接
    token = connect_mysql.select(sql)
    token = DataCoversion().tuple_to_str(token)
    return token


def add():
    args = {
        "data": {
            "id": "",
            "eq_name": "太垃1123131圾内",
            "Mode": "Add"
        },
        "hmac": ""
    }
    dbinfo = get_dbinfo_formal()
    connect_mysql.connect(dbinfo)
    headers = {"cookie": get_cookie(), 'token': get_login_token()}
    data = {
        "headers": headers,
        "method": 'post',
        "url": 'http://124.223.214.171:8080/integration/api/save',
        "json": args
    }
    res_actual = RequestStart().send_request(data)
    print(res_actual)


#
if __name__ == '__main__':
    # insert_token()
    # get_mysql_token()
    # # get_cookie()
    add()
