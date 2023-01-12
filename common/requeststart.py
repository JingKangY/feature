import time

import requests

from loging.log import *


class RequestStart(object):
    def __init__(self):
        '''
        Session:通过session方法快速关联session
        '''
        self.session = requests.Session()

    def send_request(self, data: dict):
        '''
        :param data: 参数为data格式传递,来源于request源方法
        :return: 接口返回数据 所有接口都可用
        '''
        try:
            self.response = requests.request(**data)
            log.debug(f'发起请求的参数为：{data}')
            # self._printResponse(self.response)
            # res = self.response.json()

            return self.response.json()
        except Exception as e:
            log.error(f'发起请求失败，请求参数为；{data}')
            log.error(f'发生错误的原因为：{e}')
            raise e

    def get_session_cookie(self, data: dict):
        '''
        :param data: 参数为data格式传递,来源于request源方法
        :return: 接口返回数据 所有接口都可用
        '''
        try:
            self.response = self.session.request(**data)
            log.info(f'发起请求的参数为：{data}')
            cookie = "; ".join([str(x) + "=" + str(y) for x, y in self.session.cookies.get_dict().items()])
            return cookie
        except Exception as e:
            log.error(f'发起请求失败，请求参数为；{data}')
            log.error(f'发生错误的原因为：{e}')
            raise e

    def _printResponse(self, response):
        # time.sleep(0.5)
        print("---------------- HTTP Response * header ----------------")
        # print(response.status_code)
        print('URL:' + response.url)
        for self.i, self.v in response.headers.items():
            print("{}:{}".format(self.i, self.v))
        print("Code" + str(response.status_code))
        print("---------------- HTTP Response * information ----------------")
        print('响应结果body:' + response.content.decode("utf-8"))
        # logger.info("日志打印结果body:" + response.content.decode("utf-8"))
        print("---------------- HTTP Response * end ----------------/n")
        time.sleep(0.5)
        return response.json()

