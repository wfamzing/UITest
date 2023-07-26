import time
from time import sleep
import pytest
import allure
import os
# 导入本用例用到的页面对象文件
from Test.PageObject import login_page
from Common.parse_csv import parse_csv
from Common.parse_yml import parse_yml
from Test.PageObject import common_page

# main文件下执行路径
host = parse_yml("./Config/emerg.yml", "websites", "host")
# 当前文件下执行路径文件下执行路径
# host = parse_yml("../../Config/emerg.yml", "websites", "host")
url = host+'#/login'
# main文件下执行路径
data = parse_csv("./Data/test_data.csv")
# 当前文件下执行路径文件下执行路径
# data = parse_csv("../../Data/test_data.csv")

@allure.suite('驾驶舱测试')
@allure.epic('登录')
@allure.story('登录驾驶舱')
@pytest.mark.Pipe
@pytest.mark.Supply
@pytest.mark.Supplytt
@pytest.mark.parametrize(("username", "password", "status"), data)
class TestLogin():

    def setup_methon(self):
        print("----startPip-----")

    def teardown_methon(self):
        print('----Pipend----')

    # @allure.story('登录成功')
    @allure.severity("critical")
    @pytest.mark.flaky(reruns=3, reruns_delay=1)
    def test_001_login(self, browser, username, password, status):
        allure.dynamic.title('登录驾驶舱测试')
        browser.get(url)
        # 登录的3个操作用业务场景方法一条语句代替
        login_page.LoginScenario(browser).login(username, password)
        text = login_page.LoginOper(browser).get_login_alert()
        assert '登录成功' in text

