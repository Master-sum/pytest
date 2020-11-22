"""
作者   ：bjx
创建时间   ：2020/11/22  10:56 下午 
文件名称   ：test_case.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
import pytest,yaml
from ddt import ddt,file_data


@pytest.mark.parametrize('a', yaml.load(open('data.yaml', 'rb'),Loader=yaml.FullLoader))
def test01(a):
    print(a)
    f = a
    assert f == 1

if __name__ == "__main__":
    pytest.main()