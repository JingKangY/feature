# -*-coding = utf-8 -*-
'''
@File    :  test_login2.py
@Time    :  2022-11-22 20:43
@Author  :  yangjingkang(靖康阳)
@Gitee   :  https://gitee.com/jingkangyang
@Jianshu :  靖康阳
@Contact :  1097904758@qq.com
@License :  (C)Copyright 2022--2025, Micro-Circle
@Software:  PyCharm
@Desc    :  文件内容描述
'''
from common.asserts import *
from confs.conf import *
from data.get_data import *
from common.mysql import *
from common.requeststart import *
import allure
import pytest
from service.base.shuanghcuang.preposition_fixture import *


@pytest.mark.skip()  # 跳过执行
@pytest.mark.run(order=1)
@allure.epic('双创项目')  # 大标题 一级目录
@allure.feature('登录')  # feature：allure报告的标题（二级目录）
@allure.link('https://www.baidu.com')
@allure.issue('https://www.baidu.com')
# @pytest.mark.repeat(2) # 重复跑两次
class TestLogin:
    # allure.attach.file((GetFilePath().get_all_file_path(r'image/img.png')), attachment_type=allure.attachment_type.PNG)
    @allure.story('登录模块三')  # allure报告的三级目录
    # 缺陷等级 blocker：中断缺陷 critical:临界缺陷 normal：普通缺陷 minor：次要缺陷 trivial：轻微的缺陷
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("case_info",
                             read.read_special_rows_list_excel(GetFilePath().get_all_file_path(r'data/双创wa项目接口文档.xlsx'),
                                                               '双创登录', 1, 4, [4, 7, 8, 9, 11, 13, 14, 15, 18]))
    # 用例编号1, 用例描述4, 接口路径7, 请求方法8, 请求类型9, 参数11,步骤13， 预期结果code14,预期结构message15,断言标记18
    def test_login(self, case_info):  # 登录接口测试函数(自动化测试用例)，login.xlsx叫手工测试用例或者测试数据
        desc, url, method, request_type, args, step, expect_code, expect_mes, assert_sign = case_info
        allure.dynamic.title(desc)  # 用例的标题
        allure.dynamic.description(desc)  # 用例的内容
        url = get_server_other() + url  # 组合url
        with allure.step(step):
            datas = {
                "url": url,
                "method": method,
                "json": eval(args)
            }
            res_actual = RequestStart().send_request(datas)
            ResAssert.assert_code(expect_code, res_actual['code'])
            ResAssert.assert_message(expect_mes, res_actual['msg'])
