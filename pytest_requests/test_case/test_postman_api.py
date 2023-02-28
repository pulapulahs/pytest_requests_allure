# encoding: utf-8
import allure
import pytest
import requests
from utils.read_excel import *

'''
@author: double
@file: test_postman_api.py
@time: 2023/02/28 15:26
@desc: 测试postman API
'''

test_data = get_xls()

@allure.feature('postman')
@allure.story('postman-api')
@pytest.mark.parametrize('timestamp,target,expected,test_data')
def test_timestamp(timestamp, target, expected, env_config):
    """
    用例描述：用于测试不同的timestamp和target
    """

    # 从yml配置文件获取url
    url = env_config['host']['url']
    payload = {'timestamp': timestamp, 'target': target}
    r = requests.get(url, params=payload)
    print(r.url)
    result = r.json()
    assert str(result['before']) == expected




