import allure
from loging.log import *


class ResponseAssert:
    '''
    断言封装
    '''

    @allure.step("step：响应结果断言")
    def asserts(self, expect, res_actual):  # 比对断言结果，参数：expect，actual 结果：断言是否通过
        '''
        :param expect: 预期结果
        :param res_actual: 实际结果
        :return: 用例是否通过
        '''
        try:
            log.debug(f'Response实际结果为：{res_actual}')
            log.debug(f'Response预期结果为：{expect}')
            assert str(res_actual) == str(expect)  # 成立返回TURE，失败返回FALSE
            log.info('断言用例通过！')
        except AssertionError as e:
            log.error(f'断言失败，Response实际结果为：{res_actual}，Response预期结果为：{expect}')
            log.error(f'断言用例不通过！')
            raise e

    @allure.step("step：响应状态码结果断言")
    def assert_code(self, expect_code, actual_code):
        try:
            log.debug(f'Response_Code实际结果为：{actual_code}')
            log.debug(f'Response_Code预期结果为：{expect_code}')
            assert str(actual_code) == str(expect_code)  # 成立返回TURE，失败返回FALSE
            log.info('断言Code用例通过！')
        except AssertionError as e:
            log.error(f'断言失败，Response_Code实际结果为：{actual_code}，Response预期结果为：{expect_code}')
            log.error('断言用例不通过！')
            raise e

    @allure.step("step：响应文本信息结果断言")
    def assert_message(self, expect_mes, actual_mes):
        try:
            log.debug(f'Response_Message实际结果为：{actual_mes}')
            log.debug(f'Response_Message预期结果为：{expect_mes}')
            assert str(actual_mes) == str(expect_mes)  # 成立返回TURE，失败返回FALSE
            log.info('断言Message用例通过！')
        except AssertionError as e:
            log.error(f'断言失败，Response_Message实际结果为：{actual_mes}，Response预期结果为：{expect_mes}')
            log.error('断言用例不通过！')
            raise e


ResAssert = ResponseAssert()
