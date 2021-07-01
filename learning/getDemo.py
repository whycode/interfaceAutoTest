# import requests
# r = requests.get('http://www.baidu.com/s?',params={'wd':'python'})
# print(r.url)
# print(type(r))

import requests
r = requests.get('http://httpbin.org/get',timeout=10)
print('HTTP状态码：',r.status_code)
print('返回原始响应体：',r.raw)
print('请求的响应体：',type(r.content),r.content)   # 字节方式的响应体，会自动解码gzip和deflate压缩
print('获取headers：',r.headers)
print('响应内容1：',type(r.text),r.text)   # 字符串方式的响应体，会自动根据响应头部的字符编码进行解码
print('响应内容2：',type(r.json()),r.json())   # Requests中内置的JSON解码器，将响应结果转换为JSON字符串
print('失败请求(非200响应)抛出异常:',r.raise_for_status())   # 失败请求(非200响应)抛出异常
