"""
作者   ：bjx
创建时间   ：2020/11/22  10:28 下午 
文件名称   ：test.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
import yaml
file = open('data_test.yaml','rb')
data = yaml.load(stream=file,Loader=yaml.FullLoader)
print(data)
file1 = open('dict_test.yaml','rb')
data1 = yaml.load(stream=file1,Loader=yaml.FullLoader)
print(data1['a'])

file2 = open('dict_list_test.yaml','rb')
data2 = yaml.load(stream=file2,Loader=yaml.FullLoader)
print(data2)
file3 = open('list_dict_test.yaml','rb')
data3 = yaml.load(stream=file3,Loader=yaml.FullLoader)
print(data3)
print(data3[0]['dict']['name'])