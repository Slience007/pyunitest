#coding:utf-8
import  unittest
#导入HTMLTestRunner
from HTMLTestRunner import  HTMLTestRunner
#从testCase包里面导入测试类
from testCases.userLoginTest import loginTest
from testCases.userRegTest import regTest

from utils.emailUtil import sendEmail
#构造测试套
def suite():
    suite = unittest.TestSuite()
    suite.addTest(loginTest("test_loginsucess_L0"))
    suite.addTest(loginTest("test_pwdwrong_L0"))
    suite.addTest(loginTest("test_statuserr_L1"))
    suite.addTest(regTest("test_pwdlenerr_L1"))
    suite.addTest(regTest("test_regsucess_L0"))
    suite.addTest(regTest("test_regagain_L1"))
    return suite

#运行测试用例
if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # #调用test runner的run方法执行用例
    # runner.run(suite())
    #以二进制格式打开TestReport.html用于写入数据
    with open("./TestReport.html","wb") as f:
        runner = HTMLTestRunner(stream=f,title="Reg And Login Test Report")
        result = runner.run(suite())
        totalNums = suite().countTestCases()
        passedNums = result.success_count
        failedNums = result.failure_count
        skippedNums = len(result.skipped)
        #通过率，保留两位小数
        passRate = round(passedNums * 100/  totalNums)
        emailBody = "Hi,all:\n \t本次构建一共运行：{totalNums}个用例，通过{passedNums}个，失败{failedNums}个，跳过{skippedNums}个。通过率：{passRate}%.\n \t详细信息请查看附件。"
        content = emailBody.format(totalNums=totalNums,passedNums=passedNums,failedNums=failedNums,skippedNums=skippedNums,passRate=passRate)
        #收件人列表
        receiver = ['1280353877@qq.com',"wang_suqiang@126.com"]
        #测试报告的路径
        path1 = "/home/stephen/PycharmProjects/unitTestDemo/TestReport.html"
        subject = "登录注册功能每日构建"
        e = sendEmail(subject,content,receiver,attachPath=path1)
        #发送邮件
        e.sendEmail()


    # startPath = './testCases'
    # discover = unittest.defaultTestLoader.discover(start_dir=startPath,pattern='*Test.py')
    # print(discover)
