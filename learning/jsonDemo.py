import json

dict1 = {
    'name':'fighter',
    'age':28,
    'address':'shenzhen'
}

print('未序列化前的数据类型为：',type(dict1))
print('未序列化前的数据为：',dict1)

print('begin对Python对象进行序列化操作--------->')
str1 = json.dumps(dict1)
print('序列化后的数据类型为：',type(str1))
print('序列化后的数据为：',str1)

print('begin对str1对象进行反序列化操作--------->')
dict2 = json.loads(str1)
print('反序列化后的数据类型为：',type(dict2))
print('反序列化后的数据为：',dict2)