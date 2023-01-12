from common.asserts import *
from common.requeststart import *
from conftest import *
import allure
from confs.conf import *
from data.get_data import read
from data.get_filepath import GetFilePath
from service.base.signup.preposition_fixture import *


@pytest.mark.run(order=2)
# @pytest.mark.skip('仅用于测试过程，暂时不跑')  # 跳过执行
@allure.epic('双创项目')  # 一级目录
@allure.feature('注册')  # feature：allure报告的标题（二级目录）
@allure.link('www.baidu.com')
@allure.issue('缺陷标题测试')
class TestSignup:
    @allure.story('注册模块一')  # story：allure报告的三级目录
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize('case_info',
                             read.read_special_list_excel(GetFilePath().get_all_file_path(r'data/双创wa项目接口文档.xlsx'),
                                                          'wa注册',
                                                          [1, 2, 3, 4, 5, 10, 12, 16, 17, 18, 19],
                                                          '注册signup'))
    # 用例编号1, 用例描述2, 接口路径3, 请求方法4,请求类型5, 参数10,步骤12, 预期结果16,验库表名17, 验库sql18, 数据库预期行数19
    def test_signup(self, case_info, connect_db, test_signup_clear):  # 注册接口测试函数(自动化测试用例)
        '''
        :param case_info:  参数化用例
        :param connect_db: 前后置数据库操作
        :param sign_clear: 初始化数据库
        :return: 结果
        '''
        number, desc, url, method, res_type, args, step, expect, tables, check_sql, db_expect = case_info
        allure.dynamic.title(number + desc)  # 用例的标题
        allure.dynamic.description(desc)  # 用例的内容
        url = str(get_server_formal()) + url
        # db = connect_db
        # clear = test_signup_clear
        with allure.step(step):
            datas = {
                "url": url,
                "method": method,
                'json': eval(args)
            }
            res_actual = RequestStart().send_request(datas)
            ResAssert.asserts(eval(expect), res_actual)
            connect_mysql.asserts_db(eval(db_expect), connect_mysql.select(check_sql))
