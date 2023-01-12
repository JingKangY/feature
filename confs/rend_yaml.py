import os
import yaml
from loging.log_level import *


# 通过key读取extract.yaml文件
def read_yaml(key, ):
    with open('./confs/yamls.yaml', encoding='utf-8', mode='r') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        # lg_info(f'读取数据库地址成功:{value[key]}')

        return value[key]


if __name__ == '__main__':
    print(read_yaml('data_bases'))
