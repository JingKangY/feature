# -*- coding: utf-8 -*-
'''
@File    :   email_manage.py
@Time    :   2022/7/13 20:21
@Author  :   YangJingKang(靖康阳)
@Gitee   :   https://gitee.com/jingkangyang/
@Jianshu :   靖康阳
@Contact :   1097904758@qq.com
@License :   (C)Copyright 2022-2025, Micro-Circle
@Desc    :   文件内容描述
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from loging.log import log


class EmailManage:

    def send_mail(self, account, password, subject, receivers=[], carbon_copy=[], mailbody='', attach_files=[]):
        '''
        :param account: 发件人邮箱
        :param password: SMTP密码
        :param subject: 邮件标题
        :param receivers: 收件人
        :param carbon_copy: 抄送人
        :param mailbody: 邮箱主题内容
        :param attach_files: 文件名
        :return:
        '''
        # 2、连接邮件服务器
        smtp = smtplib.SMTP('smtp.163.com', 25)
        # 3、登录邮箱
        smtp.login(account, password)
        # 4、指定邮件信息
        sender = account
        mailbody = MIMEText(mailbody, 'html', 'utf-8')
        mail = MIMEMultipart()
        mail.attach(mailbody)  # 邮箱主题内容
        mail['Subject'] = subject
        mail['from'] = sender
        mail['To'] = ','.join(receivers)
        mail['Cc'] = ','.join(carbon_copy)
        for file in attach_files:
            attach_file = open(file, 'rb').read()
            attach = MIMEText(attach_file, 'base64', 'utf-8')
            attach['Content-Type'] = 'application/octet-stream'
            attach.add_header('Content-Disposition', 'attachment', filename=file)
            mail.attach(attach)
        # 5、发送邮件
        smtp.sendmail(sender, receivers, mail.as_string())
        log.info("==============================发送报告成功==============================")
        # 6、断开连接
        smtp.quit()


if __name__ == '__main__':
    mailbody = '''
    经理你好：<p>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;接口项目测试已经完成，测试日志及用例请参阅附件。<p>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbspallure测试报告地址：http://169.254.53.71:9090/<p>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;麻烦阅读！
    '''
    EmailManage().send_mail('jingkangyang@163.com', 'LWNOFKLJUSYPSRIS', '接口测试报告',
                            ['1097904758@qq.com', '441191551@qq.com'],
                            ['1097904758@qq.com', '441191551@qq.com'], mailbody,
                            ['../testrun/LogFile.log', '../data/双创wa项目接口文档.xlsx'])
