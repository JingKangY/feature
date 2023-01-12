# -*- coding: utf-8 -*-
'''
@File    :   get_filepath.py
@Time    :   2022/8/29 15:34
@Author  :   YangJingKang(靖康阳)
@Gitee   :   https://gitee.com/jingkangyang/
@Jianshu :   靖康阳
@Contact :   1097904758@qq.com
@License :   (C)Copyright 2022-2025, Micro-Circle
@Desc    :   文件内容描述
os.path.commonprefix(list) 返回list(多个路径)中，所有path共有的最长的路径
os.path.dirname(path) 返回文件路径
os.path.exists(path) 如果路径 path 存在，返回 True；如果路径 path 不存在，返回 False。
os.path.lexists 路径存在则返回True,路径损坏也返回True
os.path.expanduser(path) 把path中包含的""和"user"转换成用户目录
os.path.expandvars(path) 根据环境变量的值替换path中包含的"n a m e " 和 " name"和"name"和"{name}"
os.path.getatime(path) 返回最近访问时间（浮点型秒数）
os.path.getmtime(path) 返回最近文件修改时间
os.path.getctime(path) 返回文件 path 创建时间
os.path.getsize(path) 返回文件大小，如果文件不存在就返回错误
os.path.isabs(path) 判断是否为绝对路径
os.path.isfile(path) 判断路径是否为文件
os.path.isdir(path) 判断路径是否为目录
os.path.islink(path) 判断路径是否为链接
os.path.ismount(path) 判断路径是否为挂载点
os.path.join(path1[, path2[, …]]) 把目录和文件名合成一个路径
os.path.normcase(path) 转换path的大小写和斜杠
os.path.normpath(path) 规范path字符串形式
os.path.realpath(path) 返回path的真实路径
os.path.relpath(path[, start]) 从start开始计算相对路径
os.path.samefile(path1, path2) 判断目录或文件是否相同
os.path.sameopenfile(fp1, fp2) 判断fp1和fp2是否指向同一文件
os.path.samestat(stat1, stat2) 判断stat tuple stat1和stat2是否指向同一个文件
os.path.split(path) 把路径分割成 dirname 和 basename，返回一个元组
os.path.splitdrive(path) 一般用在 windows 下，返回驱动器名和路径组成的元组
os.path.splitext(path) 分割路径，返回路径名和文件扩展名的元组
os.path.splitunc(path) 把路径分割为加载点与文件
os.path.walk(path, visit, arg) 遍历path，进入每个目录都调用visit函数，visit函数必须有3个参数(arg, dirname, names)，dirname表示当前目录的目录名，names代表当前目录下的所有文件名，args则为walk的第三个参数
os.path.supports_unicode_filenames 设置是否支持unicode路径名

'''
import os


class GetFilePath(object):
    """
    静态方法 非必须传参
    """
    @staticmethod
    def get_all_file_path(file=""):
        '''
        :param file: 文件的相对文件路径
        :return:文件绝对路径
        '''
        curr_file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # print(type(curr_file_path))
        file_path = os.path.join(curr_file_path, file)
        return file_path


if __name__ == '__main__':
    GetFilePath().get_all_file_path(r'data/双创wa项目接口文档.xlsx')
    # GetFilePath().get_all_file_path()
