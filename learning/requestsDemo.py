import requests


def zentaoLogin():
    """登录请求"""
    data = {
        'account':'admin',
        'password':'123456',
        'referer':'http://192.168.1.106:8011/zentao/www/doc-browse-product-0-59-0.html'
    }

    return data


def login():
    """获取登录后返回Cookie"""
    r = requests.post(
            url='http://192.168.1.106:8011/zentao/www/user-login.html',
            data=zentaoLogin(),
            headers={'Content-Type':'application/x-www-form-urlencoded'}
    )
    return r.cookies


def uploadData():
    """接口参数"""
    data = {
        'product':'59',
        'module':'0',
        'type':'file',
        'title':'looking1',
        'url':'',
        'content':'',
        'keywords':'',
        'gigest':'',
        'labels[]':'',
        'lib':'product'
    }
    return data


def uploadFile():
    """上传文件接口"""
    r = requests.post(
        url = 'http://192.168.1.106:8011/zentao/www/doc-create-product-0-0-0-doc.html',
        data=uploadData(),
        headers={'Content-Type':'multipart/form-data'},
        files = {"file":("1.jpg",open(r"C:/1.jpg","rb"),"image/jpeg",{})},
        cookies=login()
    )
    print(r.status_code)
    print(r.text)


uploadFile()


"""
    整个文件上传的流程是先登录系统，再带上登录系统返回的Cookie信息，然后进行文件上传操作。在login()方法中，r.cookies方法表示获取登录后返回的Cookie信息，
    uploadFile()方法表示上传文件接口，这里需要用对应入参(接口地址url、请求参数data、请求头headers、文件类型files及cookies)

"""