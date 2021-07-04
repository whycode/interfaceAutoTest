import configparser
import os, requests,logging


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

    def Makelog(self,log_content):
        """定义日志级别"""
        #定义日志文件
        logFile = logging.FileHandler(self.dirname('log.tx','Log'),'a',encoding='utf-8')

        # 设置log格式
        fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levealname)s-%(module)s:%(message)s')

        logFile.setFormatter(fmt)
        logger1 = logging.Logger('logTest',level=logging.DEBUG)    # 定义日志
        logger1.addHandler(logFile)
        logger1.info(log_content)
        logFile.close()

    def readConfig(self):
        """读取配置文件中的内容"""
        savedata = []
        config = configparser.ConfigParser()
        config.read(self.dirname('config.ini','Config'),encoding='utf-8')

        email_host = config.get("EMAIL","mail_host")
        email_password = config.get("EMAIL","mail_pass")
        email_sender = config.get("EMAIL", "sender")
        email_user = config.get("EMAIL", "mail_user")
        email_receiver = config.get("EMAIL", "receiver")
        email_subject = config.get("EMAIL", "subject")

        savedata.append(email_host)
        savedata.append(email_password)
        savedata.append(email_sender)
        savedata.append(email_user)
        savedata.append(email_receiver)
        savedata.append(email_subject)

        return savedata
