from service.base.login.preposition_fixture import *
import allure
import pytest
from common.asserts import ResAssert
from common.requeststart import RequestStart
from confs.conf import get_server_formal
from data.get_data import read
from data.get_filepath import GetFilePath


# @pytest.mark.skip()  # 跳过执行
@pytest.mark.run(order=1)
@allure.epic('双创项目')  # 大标题 一级目录
@allure.feature('登录')  # feature：allure报告的标题（二级目录）
@allure.link('https://www.baidu.com')
@allure.issue('https://www.baidu.com')
# @pytest.mark.repeat(2) # 重复跑两次
class TestLogin:
    # allure.attach.file((GetFilePath().get_all_file_path(r'image/img.png')), attachment_type=allure.attachment_type.PNG)
    @allure.story('登录模块一')  # story：allure报告的三级目录
    # 缺陷等级 blocker：中断缺陷 critical:临界缺陷 normal：普通缺陷 minor：次要缺陷 trivial：轻微的缺陷
    @allure.severity(allure.severity_level.BLOCKER)
    # @pytest.mark.usefixtures('connect_db')  # 另一种调用方式 级别为class
    @pytest.mark.parametrize("case_info",
                             read.read_special_list_excel(GetFilePath().get_all_file_path(r'data/双创wa项目接口文档.xlsx'),
                                                          'wa登录', [2, 5, 6, 7, 9, 11, 12, 13, 14],
                                                          '登录login'))
    #  用例描述2, 接口路径5, 请求方法6, 请求类型7, 参数9,步骤11， 预期结果code12,预期结果msg13,预期结果message14,
    def test_login(self, connect_db, get_usernm_passwd, get_token, test_login_clear,
                   case_info):
        desc, url, method, request_type, args, step, expect_code, expect_result, expect_mes = case_info
        allure.dynamic.title(desc)  # 用例的标题
        allure.dynamic.description(desc)  # 用例的内容
        url = get_server_formal() + url  # 组合url
        print(get_token)
        with allure.step(step):
            datas = {
                "url": url,
                "method": method,
                'data': eval(args)
            }
            res_actual = RequestStart().send_request(datas)
            ResAssert.assert_code(expect_code, res_actual['Status'])
            ResAssert.assert_message(expect_result, res_actual['Result'])
            ResAssert.assert_message(expect_mes, res_actual['Message'])
