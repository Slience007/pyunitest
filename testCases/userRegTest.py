#coding:utf-8
#导入unittest模块
import unittest
#从模块userRegLogin中导入类user_manage
from userManage.userRegLogin import user_manage

#定义测试类，继承于unittest.TestCase
class regTest(unittest.TestCase):
    #测试方法或者叫测试用例必须以test开头
    #测试场景：密码长度小于6
    def setUp(self):
        print("setUp run before test case")
        self.user1 = user_manage("TestUser1","1234")
        self.user2 = user_manage("TestUser2","TestUser2")
        self.user3 = user_manage("TestUser3","TestUser3")

        #注册TestUser3
        self.user3.userReg()
    #@unittest.skip("skip test case of user reg")
    def test_pwdlenerr_L1(self):
        print("test case:test_pwdlenerr_L1")
        res = self.user1.userReg()
        self.assertEqual(res,"passwordLenError")

    #测试场景：正常注册
    #@unittest.skipIf(2>1,"skip if condiction")
    def test_regsucess_L0(self):
        print("test case:test_regsucess_L0")
        res = self.user2.userReg()
        self.assertEqual(res,"regSucess")

    #测试场景：用户名重名
    #@unittest.skipUnless(1<0,"skip unless.")
    def test_regagain_L1(self):
        print("test case:test_regagain_L1")
        res = self.user3.userReg()
        self.assertEqual(res,"SameNameError")

    def tearDown(self):
        print("tearDown run after test case")
        sql = '''delete from  user_info  where name = %s'''
        self.user2.execUpdateSql(sql,[self.user2.name])
        self.user3.execUpdateSql(sql,[self.user3.name])


#定义测试类，继承于unittest.TestCase
# class regTest(unittest.TestCase):
#     #测试方法或者叫测试用例必须以test开头
#     #测试场景：密码长度小于6
#     @classmethod
#     def setUpClass(cls):
#         print("setUpClass run before test case")
#
#     def test_pwdlen(self):
#         print("test case:test_pwdlen")
#         self.user1 = user_manage("TestUser8","1234")
#         res = self.user1.userReg()
#         self.assertEqual(res,"passwordLenError")
#
#     #测试场景：正常注册
#     def test_normalreg(self):
#         print("test case:test_normalreg")
#         self.user2 = user_manage("TestUser10","123456")
#         res = self.user2.userReg()
#         self.assertEqual(res,"regSucess")
#
#     @classmethod
#     def tearDownClass(cls):
#         # sql = '''delete from  user_info  where name = %s'''
#         # sef.user2.execUpdateSql(sql,[self.user2.name])
#         print("tearDownClass run after test case")
#执行test开头的方法
if __name__ == '__main__':
    unittest.main()
