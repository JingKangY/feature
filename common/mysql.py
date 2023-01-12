# coding = utf-8
'''
@File    :   requests_send_request.py
@Time    :   2021/04/22 11:54
@Author  :   FengQzhu
@Github :    https://FengQzhu.cn/
@Contact :   //
@License :   (C)Copyright 2021-2023, Micro-Circle
@Desc    :   数据库 封装
'''

# 导入模块
import allure
import pymysql
from confs.conf import *
from loging.log import *


class ConnectMysql(object):

    @allure.step('连接数据库')
    def connect(self, dbinfo):
        '''
        连接MySQL数据库
        '''
        try:
            self.connectmysql = pymysql.connect(**dbinfo)
            log.info(f'===============>成功连接数据库,参数为：{dbinfo}<===================')
        except Exception as e:
            log.error(f'数据库连接失败，连接参数为{dbinfo}')
            log.error(f'错误原因{e}')
            raise e
    @allure.step('写入数据库信息')
    def insert_one(self, sql):  # 新增单条数据
        """
        :param sql: 插入数据sql语句
        :return: 新增数据
        """
        rqmysql = self.connectmysql  # 调用函数
        cursor = rqmysql.cursor()  # 游标
        try:
            cursor.execute(sql)  # 操作
            rqmysql.commit()  # 进行提交保存
            log.debug(f'执行SQL语句=====>{sql}<=====成功')
        except Exception as e:
            log.error(f'执行SQL语句=====>{sql}<=====出错')
            raise e

    # 新增多条数据
    def insert_many(self, sqls: list):
        '''
        :param sqls: 传入批量SQL语句，格式为列表
        :return: 返回执行结果
        '''
        rqmysql = self.connectmysql  # 调用函数
        cursor = rqmysql.cursor()  # 游标
        log.debug(f'初始化开始，共查找SQL语句{len(sqls)}条，SQL执行开始')
        for sql in sqls:
            try:
                cursor.execute(sql)  # 操作
                rqmysql.commit()  # 进行提交保存
            except Exception as e:
                log.error(f'执行SQL语句=====>{sql}<=====出错')
                raise e
        log.info(f'初始化成功，共执行SQL语句{len(sqls)}条')

    # 更新数据
    def update(self, sql):
        '''
        :param sql:更新SQL语句
        :return:返回执行结果
        '''
        rqmysql = self.connectmysql  # 调用函数
        cursor = rqmysql.cursor()  # 游标
        try:
            cursor.execute(sql)  # 操作
            rqmysql.commit()  # 进行提交保存
            log.debug(f'执行SQL语句=====>{sql}<=====成功')
        except Exception as e:
            log.error(f'执行SQL语句=====>{sql}<=====出错')
            raise e

    @allure.step('初始化数据库信息')
    def delete_one(self, sql: str):  # 删除单个数据
        '''
        :param sql: 单独传入SQL语句，格式为字符串
        :return:返回执行结果
        '''
        rqmysql = self.connectmysql  # 调用函数
        cursor = rqmysql.cursor()  # 游标
        try:
            cursor.execute(sql)  # 操作
            rqmysql.commit()  # 进行提交保存
            log.debug(f'执行SQL语句=====>{sql}<=====成功')
        except Exception as e:
            log.error(f'执行SQL语句=====>{sql}<=====出错')
            raise e

    def delete_many(self, sqls: list):  # 删除多条数据
        '''
        :param sqls: 传入批量SQL语句，格式为列表
        :return:返回执行结果
        '''
        rqmysql = self.connectmysql  # 调用函数
        cursor = rqmysql.cursor()  # 游标
        log.debug(f'初始化开始，共查找SQL语句{len(sqls)}条，SQL执行开始')
        for sql in sqls:
            try:
                cursor.execute(sql)  # 操作
                rqmysql.commit()  # 进行提交保存
            except Exception as e:
                log.error(f'执行SQL语句=====>{sql}<=====出错')
                raise e
        log.info(f'初始化成功，共执行SQL语句{len(sqls)}条')

    # 查询数据
    def select(self, sql):
        """
        :param sql:查询select数据sql语句 -->   SELECT * FROM 表
        :return:查询数据
        """
        select_mysql = self.connectmysql  # 调用函数
        cursor = select_mysql.cursor()
        try:
            cursor.execute(sql)  # 操作
            select_mysql.commit()  # 进行提交保存
            db_actual = cursor.fetchone()  # 返回元组信息
            return db_actual
        except BaseException as e:
            log.error(f'执行SQL语句错误，错误信息为：{e}')
            raise e

    def selects(self, sql):
        """
        :param sql:查询select数据sql语句 -->   SELECT * FROM 表
        :return:查询数据,返回结果是元组嵌套
        """
        select_mysql = self.connectmysql  # 调用函数
        cursor = select_mysql.cursor()
        try:
            cursor.execute(sql)  # 操作
            select_mysql.commit()  # 进行提交保存
            db_actual = cursor.fetchall()  # 返回元组列表信息
            return db_actual
        except BaseException as e:
            log.error(f'执行SQL语句错误，错误信息为：{e}')
            raise e

    @allure.step("step：数据库断言")
    def asserts_db(self, db_expect, db_actual):
        try:
            log.debug(f'验库的预期结果：{db_expect}')
            log.debug(f'验库的实际结果：{db_actual}')
            assert db_actual == db_expect
            log.info('验证数据库用例通过！')
        except AssertionError as e:
            log.error(f'验库失败，预期结果为：{db_expect}，实际结果为：{db_actual}')
            log.error('验证数据库用例不通过！')
            raise e

    @allure.step('关闭数据库连接')
    def close_db(self):
        close_mysql = self.connectmysql  # 调用函数
        close_mysql.close()  # 关闭数据库
        log.debug('==============================关闭数据库成功===============================')


connect_mysql = ConnectMysql()

if __name__ == '__main__':
    connect_mysql.connect()
    # connect_mysql.conf_db()
    # # info = connect_mysql.selects("SELECT id,name FROM wa_test.info")
    # # if info != eval("()"):
    # #     for i in info:
    # #         if i[0] > 3:
    # #             connect_mysql.delete_one("DELETE FROM wa_test.info WHERE id = {}".format(i[0]))
    # #
    # # users_info = connect_mysql.selects("SELECT id,username FROM wa_test.users")
    # # if users_info != eval("()"):
    # #     for i in users_info:
    # #         if i[0] > 3:
    # #             connect_mysql.delete_one("DELETE FROM wa_test.users WHERE id = {}".format(i[0]))
    # # connect_mysql.delete_one("DELETE FROM info WHERE id=4")
    # # connect_mysql.delete_one("DELETE FROM users WHERE id=4")
    # # connect_mysql.delete_one("DELETE FROM info WHERE id=5")
    # # connect_mysql.delete_one("DELETE FROM users WHERE id=5")
    # # connect_mysql.insert_many(["INSERT INTO users(id, username, password) VALUES(4, 'test01', md5('123456'))",
    # #                            "INSERT INTO users(id, username, password) VALUES(5, 'test02', md5('123456'))"])
    # # connect_mysql.close_db()
    # connect_mysql.select('SELECT username,password FROM `users` WHERE id = "1"')
