# -*-coding = utf-8 -*-
'''
@File    :  test_login1.py
@Time    :  2022-11-22 1:16
@Author  :  yangjingkang(靖康阳)
@Gitee   :  https://gitee.com/jingkangyang
@Jianshu :  靖康阳
@Contact :  1097904758@qq.com
@License :  (C)Copyright 2022--2025, Micro-Circle
@Software:  PyCharm
@Desc    :  文件内容描述
'''
from service.base.login.preposition_fixture import *
import allure
import pytest
from common.asserts import ResAssert
from common.requeststart import RequestStart
from confs.conf import get_server_formal
from data.get_data import read
from data.get_filepath import GetFilePath


@pytest.mark.skip()
@pytest.mark.run(order=2)
@allure.epic('双创项目')  # 大标题 一级目录
@allure.feature('登录')  # feature：allure报告的标题（二级目录）
@allure.link('https://www.baidu.com')
@allure.issue('https://www.baidu.com')
class TestLogin1:
    @allure.story('登录模块二')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("case_info",
                             read.read_special_rows_list_excel(GetFilePath().get_all_file_path(r'data/双创wa项目接口文档.xlsx'),
                                                               'wa登录', 12, 12, [2, 5, 6, 11, 12, 13, 14]))
    # [['1、正确输入接口地址 2、正确输入请求参数 3、查看响应body是否正确', "{'Status':1001,'Result':'Username is null','Message':'用户名不能为空'}"]]

    def test_login1(self, case_info, connect_db, get_token, get_usernm_passwd):  # 登录接口测试函数(自动化测试用例)，login.xlsx叫手工测试用例或者测试数据
        print(case_info)
        desc, url, method, step, expect_code, expect_result, expect_mes = case_info
        username, password = get_usernm_passwd
        allure.dynamic.title(desc)  # 用例的标题
        allure.dynamic.description(desc)  # 用例的内容
        url = get_server_formal() + url
        # print(get_token)
        with allure.step('step'):
            datas = {
                "url": url,
                "method": method,
                "data": {'username': username, 'password': password}
            }
            res_actual = RequestStart().send_request(datas)
            ResAssert.assert_code(expect_code, res_actual['Status'])
            ResAssert.assert_message(expect_result, res_actual['Result'])
            ResAssert.assert_message(expect_mes, res_actual['Message'])
