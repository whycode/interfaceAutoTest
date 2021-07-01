import requests
import unittest


class ApiTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = 'http://212.123.456.123:1122/login'

    @classmethod
    def tearDown(cls):
        pass

    def write_token(self):
        '''将Token信息写入到token.md文件中'''
        data = {'username': 'admin', 'password': 'admin'}
        response = requests.post(url=self.url, json=data, headers={'Content-Type': "application/json"})

        with open('token.md', 'w') as f:
            f.write(response.json()['token'])

    def read_token(self):
        '''读取token.md文件中的Token信息'''
        with open('token.md', 'r') as f:
            return f.read()

    def test_getApiTask(self):
        response = requests.get(url=self.url + '/api/tasks', headers=self.read_token())
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.mian(verbosity=2);
