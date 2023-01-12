'''
@allure.epic()	epic描述	敏捷里面的概念，对用例或用例集进行描述分类
@allure.feature()	模块名称	与epic类似，只是比epic级别低
@allure.story()	用户故事	与epic类似，只是比feature级别低
@allure.title(用例的标题)	用例的标题	重命名html报告的用例名称
@allure.testcase()	测试用例的链接地址	与link类似
@allure.issue()	缺陷	与link类似
@allure.description()	用例描述	进行测试用例的描述
@allure.step()	操作步骤	进行测试用例的步骤
@allure.severity()	用例等级	blocker，critical，normal，minor，trivial
@allure.link()	链接	定义一个链接，在测试报告展现（推荐使用）
@allure.attachment()	附件	报告添加附件
@pytest.mark.repeat()
'''
import os
import time
import pytest
import text_unidecode

from emails.email_manage import EmailManage

if __name__ == '__main__':
    #pytest.main(['-sv', '--alluredir', '../temp_allurefile', '--clean-alluredir','../testcase/erxing_Love_Letter/test_get_bullet_screen_content.py'])
    pytest.main(['-v', '--alluredir', '../temp_allurefile', '--clean-alluredir', '../testcase'])
    '''
    pytest.main()：main中传入不同的指令用以执行指定测试用例a
    -s: 显示程序中的print/logging输出
    -v: 丰富信息模式, 输出更详细的用例执行信息
    -q: 安静模式, 不输出环境信息
    -k：关键字匹配，用and区分：匹配范围（文件名、类名、函数名）
    -s,py文件路径：指定py执行
    --alluredir ../temp_allurefile  创建allure原json文件目录的位置
    ../testcase：指定用例文件
    --reruns 2 --reruns-delay 2：失败重试2次，在每次重试前会等到2秒。
    --count=3：意思是重复执行3次
    --count=3 --repeat-scope=session：–repeat-scope也可以设置参数:session,module,class或者function（默认值）
    '''
    time.sleep(3)
    os.system('allure generate ../temp_allurefile -o ../reports/Perfectresult ../reports --clean ')
    '''
    allure generate：生成命令
    ../temp：原Json文件
    -o：输出
    ../reports/Perfectresult  本地可以出趋势图：如果要部署到jenkins可以删除掉
    ../reports：新生产报告的位置
    --clean：每次生成前都会清楚之前的报告
    '''
    # mailbody = '''
    #    经理你好：<p>
    #    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;接口项目测试已经完成，测试日志及用例请参阅附件。<p>
    #    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbspallure测试报告地址：http://192.168.125.1:1234/<p>
    #    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;麻烦阅读！
    #    '''
    # EmailManage().send_mail('jingkangyang@163.com', 'LWNOFKLJUSYPSRIS', '接口测试报告',
    #                         ['1097904758@qq.com', '441191551@qq.com'],
    #                         ['1097904758@qq.com', '441191551@qq.com'], mailbody,
    #                         ['../data/双创wa项目接口文档.xlsx', '../data/双创wa项目接口文档.xlsx'])
