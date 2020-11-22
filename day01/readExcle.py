"""
作者   ：bjx
创建时间   ：2020/11/22  11:46 下午 
文件名称   ：readExcle.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
import xlrd
data_file = r'data路径'
def get_body(sheetName):
    value_rows = []
