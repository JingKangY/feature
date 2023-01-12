import configparser

from data.get_filepath import GetFilePath
from loging.log import *


class Conf:
    def __init__(self):
        '''
        初始化服务器配置文件，数据库配置文件
        '''
        self.conf = configparser.ConfigParser()  # 创建配置对象，申请内存，准备存储文件中的数据
        self.server_file = GetFilePath().get_all_file_path(r'confs/server.conf')
        self.db_file = GetFilePath().get_all_file_path(r'confs/db.conf')

    def conf_get_sever(self, arg1):
        self.conf.read(self.server_file, encoding='utf-8')
        ip = self.conf.get(arg1, 'ip')
        port = self.conf.get(arg1, 'port')
        host = f"http://{ip}:{port}"
        return host

    def conf_get_db(self, arg1):
        self.conf.read(self.db_file, encoding='utf-8')
        host = self.conf.get(arg1, 'host')
        db = self.conf.get(arg1, 'db')
        user = self.conf.get(arg1, 'user')
        passwd = self.conf.get(arg1, 'passwd')
        dbinfo = {'host': host, 'db': db, 'user': user, 'passwd': passwd}
        log.debug(f'读数据库服务器配置文件{self.db_file}成功，数据库信息是{dbinfo}')
        return dbinfo


conf = Conf()


def get_server_other():  # 获取formal服务器配置
    return conf.conf_get_sever('other')
def get_server_formal():  # 获取formal服务器配置
    return conf.conf_get_sever('formal')

def get_server_smoke():  # 获取smoke服务器配置
    return conf.conf_get_sever('smoke')


def get_server_debug():  # 获取debug服务器配置
    return conf.conf_get_sever('debug')


def get_server_regress():  # 获取regress服务器配置
    return conf.conf_get_sever('regress')


def get_dbinfo_formal():  # 获取regress数据库配置
    return conf.conf_get_db('formal')


def get_dbinfo_debug():  # 获取debug数据库配置
    return conf.conf_get_db('debug')


def get_dbinfo_smoke():  # 获取smoke数据库配置
    return conf.conf_get_db('smoke')


def get_dbinfo_regress():  # 获取regress数据库配置
    return conf.conf_get_db('regress')


if __name__ == '__main__':
    print(type(get_server_other()))

