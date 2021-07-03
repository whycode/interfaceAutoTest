import os, requests


class Helper(object):

    def get(self, url, headers=''):
        """重构GET请求"""
        if url:
            r = requests.get(url=url, headers=headers)
            return r
        else:
            try:
                print('接口地址有误！')
            except Exception as e:
                print('错误原因：%s' % e)

    def post(self, url, data, headers=''):
        """重构POST请求"""
        if url:
            r = requests.post(url=url, json=data, headers=headers)
            return r
        else:
            try:
                print('接口地址有误！')
            except Exception as e:
                print('错误原因：%s' % e)

    def delete(self, url, headers=''):
        """重构DELETE请求"""
        if url:
            r = requests.delete(url=url,headers=headers)
            return r
        else:
            try:
                print('接口地址有误！')
            except Exception as e:
                print('错误原因：%s' % e)

    def dirname(self,fileName='',filePath='Data'):
        """
        作用：将接口测试用例中服务器返回的动态数据写入到指定目录下。调用dirname()方法时只需要传入文件名即可
        :param fileName: 文件名
        :param filePath: 写入指定目录
        :return:
        """
        return os.path.join(os.path.dirname(os.path.dirname(__file__)),filePath,fileName)