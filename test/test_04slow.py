"""
作者   ：bjx
创建时间   ：2020/11/11  1:20 上午 
文件名称   ：test_04slow.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
import pytest
@pytest.fixture
def error_fixture():
    assert 0

@pytest.mark.slow
def test_ok():
    print("ok")


def test_fail():
    assert 0


def test_error(error_fixture):
    pass


def test_skip():
    pytest.skip("skipping this test")


def test_xfail():
    pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass