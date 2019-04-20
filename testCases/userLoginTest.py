#coding:utf-8
import unittest
from userManage.userRegLogin import user_manage

class loginTest(unittest.TestCase):
    #准备工作
    def setUp(self):
        self.user4 = user_manage("TestUser4","TestUser4")
        self.user5 = user_manage("TestUser4","TestUser5")
        self.user6 = user_manage("TestUser6","TestUser6")

        #验证登录功能前需要先注册
        self.user4.userReg()
        #构造一个状态为inactive的用户
        self.user6.userReg()
        setStatus = '''update user_info set status="inactive" where name=%s;'''
        self.user6.execUpdateSql(setStatus,[self.user6.name])
    #登录成功测试
    def test_loginsucess_L0(self):
        res = self.user4.userLogin()
        self.assertEqual(res,"loginSucess")
    #密码错误测试
    def test_pwdwrong_L0(self):
        res = self.user5.userLogin()
        self.assertEqual(res,"passwordError")
    #用户状态异常测试
    def test_statuserr_L1(self):
        res = self.user6.userLogin()
        self.assertEqual(res,"UserStatusError")
    #清理工作
    def tearDown(self):
        print("tearDown run after test case")
        #删除用户TestUser4,TestUser6
        sql = '''delete from  user_info  where name = %s'''
        self.user4.execUpdateSql(sql,[self.user4.name])
        self.user6.execUpdateSql(sql,[self.user6.name])

if __name__ == '__main__':
    unittest.main()
