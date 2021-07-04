import unittest
from Utils.page import *  # 导入Helper工具类
from Utils.excels import *  # 导入Excels工具灰
import requests


class Totasks(unittest.TestCase, Helper, Excels):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_register(self):
        """注册接口"""
        # url = 'http://211.156.133.120:3000/register'
        # data = {'username': 'jackLu', 'password': 'jackLu', 'password_confirmation': 'jackLu'}
        # r = self.post(url, data)
        r = self.post(self.readUrl(1), self.readData(1))
        self.assertEqual(r.json()['username'], 'jackLu')
        self.Makelog('接口断言：注册接口响应数据检验jackLu')
        self.assertEqual(r.status_code, 200)
        self.Makelog('接口断言：注册接口响应状态码检验200')

    def test_login(self):
        """登录接口"""
        # url = 'http://211.156.133.120:3000/login'
        # data = {'username': 'jackLu', 'password': 'jackLu'}
        # r = self.post(url, data)
        r = self.post(self.readUrl(2), self.readData(2))
        self.assertEqual(r.status_code, 200)
        self.Makelog('接口断言：登录接口响应状态码检验200')
        self.assertEqual(r.json()['username'], 'jackLu')
        self.Makelog('接口断言：登录接口响应数据检验jackLu')

    def write_Token(self):
        """将Token写入Token.md文件中"""
        # url = 'http://211.156.133.120:3000/login'
        # data = {'username': 'jackLu', 'password': 'jackLu'}
        # r = requests.post(url, data)
        r = requests.post(self.readUrl(2), self.readData(2))
        with open(self.dirname('Token.md'), 'w') as f:
            self.Makelog('日志跟踪：将Token写入Token.md文件中')
            f.write(r.json()['token'])

    def read_Token(self):
        """读取Token.md文件中的Token值"""
        with open(self.dirname('Token.md'), 'r') as f:
            self.Makelog('日志跟踪：读取Token.md文件中的Token')
            return f.read()

    def setToken(self, rx):
        """对动态参数Token赋值"""
        dinfo = self.readToken(rx)
        self.Makelog('动态参数处理：读取Excel表中的Token值')
        dinfo['token'] = self.read_Token()
        self.Makelog('动态参数处理：对Token重新赋值为最新服务器生成的Token值')
        return {"Authorization": "Bearer " + dinfo['token']}

    def test_getApiTask(self):
        """获取所有文章"""
        # r = self.get(self.readUrl(3),self.readToken())
        r = self.get(self.readUrl(3), self.setToken(3))
        self.assertEqual(r.status_code, 200)
        self.Makelog('接口断言：获取所有文章响应状态码检验200')

    def test_postApiTasks(self):
        """创建文章接口"""
        # url = 'http://211.156.133.120:3000/api/tasks'
        # data = {'title':'https://www.cnblogs.com/fighter006','desc':'接口描述'}
        # r = self.post(url,data,self.readToken())
        r = self.post(self.readUrl(4), self.readData(4), self.readToken(4))
        self.assertEqual(r.json()['desc'], '接口描述')
        self.Makelog('接口断言：创建文章响应数据断言【接口描述】')
        self.assertEqual(r.status_code, 200)
        self.Makelog('接口断言：创建文章响应状态码检验200')

    def writeTaskId(self):
        """写入Token到taskID文件中"""
        # url = 'http://211.156.133.120:3000/api/tasks'
        # data = {'title':'https://www.cnblogs.com/fighter006','desc':'接口描述'}
        # r = requests.post(url,data,self.readToken())
        r = requests.post(self.readUrl(4), self.readData(4), self.readToken(5))
        with open(self.dirname('taskID'), 'w') as f:
            f.write(str(r.json()['id']))
            self.Makelog('接口业务：将创建后的文章ID写入到taskID文件中')

    def getTaskID(self):
        """读取taskID"""
        with open(self.dirname('taskID'), 'r') as f:
            self.Makelog('接口业务：读取创建文章后的文章ID')
            return f.read()

    def test_deleteApiTask(self):
        """删除文章接口"""
        # url = 'http://211.156.133.120:3000/api/tasks/:'
        # r = self.delete(url+self.getTaskID(),self.readToken())
        r = self.delete(self.readUrl(5) + self.getTaskID(), self.readToken())
        self.assertEqual(r.status_code, 200)
        self.Makelog('接口断言：删除文章响应状态码检验200')


if __name__ == '__main__':
    unittest.main(verbosity=2)
