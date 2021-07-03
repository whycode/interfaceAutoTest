import unittest
from Utils.page import *
import requests


class Totasks(unittest.TestCase, Helper):

    @classmethod
    def setUp(cls):
        pass

    @classmethod
    def tearDown(cls):
        pass

    def test_register(self):
        """注册接口"""
        url = 'http://211.156.133.120:3000/register'
        data = {'username': 'jackLu', 'password': 'jackLu', 'password_confirmation': 'jackLu'}
        r = self.post(url, data)
        self.assertEqual(r.json()['username', 'jackLu'])
        self.assertEqual(r.status_code, 200)

    def test_login(self):
        """登录接口"""
        url = 'http://211.156.133.120:3000/login'
        data = {'username': 'jackLu', 'password': 'jackLu'}
        r = self.post(url, data)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['username'], 'jackLu')

    def writeToken(self):
        """将Token写入Token.md文件中"""
        url = 'http://211.156.133.120:3000/login'
        data = {'username':'jackLu','password':'jackLu'}
        r = requests.post(url,data)
        with open(self.dirname('Token.md'),'w') as f:
            f.write(r.json()['token'])

    def readToken(self):
        """读取Token.md文件中的Token值"""
        with open(self.dirname('Token.md','r')) as f:
            return f.read()



if __name__ == '__main__':
    unittest.main(verbosity=2)
