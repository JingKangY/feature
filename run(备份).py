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
reruns=5：意思是失败重运行5次
count=3：意思是重复执行3次
'''
import os
import sys
import time
import pytest
# 测试代码上传
# sys.path.append(os.path.dirname(__file__))
if __name__ == '__main__':
    pytest.main(['-sv', '--alluredir', './temp_allurefile', '--clean-alluredir'])
    # pytest.main(['-v', '--alluredir', '../temp_allurefile', '--clean-alluredir'])
    '''
    pytest.main()：main中传入不同的指令用以执行指定测试用例a
    -s: 显示程序中的print/logging输出
    -v: 丰富信息模式, 输出更详细的用例执行信息
    -q: 安静模式, 不输出环境信息
    -k：关键字匹配，用and区分：匹配范围（文件名、类名、函数名）
    -s,py文件路径：指定py执行
    --alluredir ../temp_allurefile  创建allure原json文件目录的位置
    '''
    time.sleep(3)
    os.system('allure generate ./temp_allurefile -o ./reports/Perfectresult ./reports --clean ./reports/Perfectresult')
    '''
    allure generate：生成命令
    ../temp：原Json文件
    -o：输出
    ../reports：新生产报告的位置
    --clean：每次生成前都会清楚之前的报告
    ../reports/Perfectresult  本地可以出趋势图：如果要部署到jenkins可以删除掉
    '''
