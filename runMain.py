import smtplib
from email.mime.text import MIMEText
import unittest
from Config.HTMLTestRunner import HTMLTestRunner
import time, os
from email.mime.multipart import MIMEMultipart
from email.header import Header
import configparser
from Utils.page import *


# 发送带邮件的函数动作
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    # 基本信息
    smtpserver = Helper().readConfig()[0]
    pwd = Helper().readConfig()[1]

    # 定义邮件主题
    msg = MIMEMultipart()
    msg['subject'] = Header(Helper().readConfig()[-1], 'utf-8')
    msg['from'] = Helper().readConfig()[2]  # 发送者的邮箱
    msg['to'] = Helper().readConfig()[3]  # 接收者的邮箱

    body = MIMEText(mail_body, "html", "utf-8")  # HTML邮件正文，直接发送附件的代码片段
    msg.attach(body)

    att = MIMEText(mail_body, "base64", "utf-8")
    att['Content-Type'] = "application/octet-stream"
    att['Content-Disposition'] = 'attachment;filename="Interface_report.html'
    msg.attach(att)

    # 链接邮箱服务器发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(msg['from'], pwd)
    smtp.sendmail(msg['from'], msg['to'], msg.as_string())

    print('邮件发送成功')


# 查找最新邮件
def new_file(test_dir):
    result_dir = test_dir
    lists = os.listdir(result_dir)  # print(lists) # 列出测试报告目录下所有的文件
    lists.sort()
    file = [x for x in lists if x.endswith('.html')]
    file_path = os.path.join(result_dir, file[-1])
    return file_path


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.realpath(__file__))    # 获取文件当前路径
    test_dir = os.path.join(base_dir,'TestCases')             # 测试用例所在路径
    test_report = os.path.join(base_dir,'Reports')            # 测试报告所在路径

    testlist = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + "\\" + now + 'result.html'

    fp = open(filename,'wb')

    runner = HTMLTestRunner(stream=fp,title=u'接口自动化测试框架设计报告',description=u'系统环境：Win10用例执行情况：')

    #runner.run(testlist)   # 课程本来是这一部分的内容，发现运行不起来，所以就拷贝了之前虫师的代码了
    runner.run(testlist, rerun=0, save_last_run=False)
    fp.close()

    new_report = new_file(test_report)    # 获取最新报告文件
    send_mail(new_report)                 # 发送最新的测试报告


