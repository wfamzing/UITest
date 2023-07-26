from time import sleep

from selenium import webdriver
import pytest
import allure
# 导入本用例用到的页面对象文件
from Test.PageObject import login_page
from Common.parse_csv import parse_csv
from Common.parse_yml import parse_yml

# main文件下执行路径
host = parse_yml("./Config/emerg.yml", "websites", "host")
# 当前文件下执行路径文件下执行路径
# host = parse_yml("../../Config/emerg.yml", "websites", "host")
url = host+'#/login'
# main文件下执行路径
data = parse_csv("./Data/test_01_index.csv")
# 当前文件下执行路径文件下执行路径
# data = parse_csv("../../Data/test_01_index.csv")

@allure.feature("登录场景")
@pytest.mark.parametrize(("username", "password", "status"), data)
class TestLogin():
    def setup(self):
        print("----startlogin-----")


    @allure.severity("critical")
    def test_001_login(self,browser, username, password, status):
        browser.get(url)
        # 登录的3个操作用业务场景方法一条语句代替
        login_page.LoginScenario(browser).login(username,password)
        if status == '0':
            # 登录失败后的提示信息，通过封装的元素操作来代替
            text = login_page.LoginOper(browser).get_login_alert()
            assert text == '登录失败，用户名或密码错误'
            browser.refresh()   # 刷新页面清除弹窗防止影响下一个用例
        elif status == '1':
            # 登录后显示的用户名，通过封装的元素操作来代替
            text = login_page.LoginOper(browser).get_login_alert()
            assert '登录成功' in text
            # 增加一个断言
            # assert "登录成功" in self.driver.page_source
        else:
            print('参数化的状态只能传入0或1')


if __name__ == '__main__':
    pytest.main(['-sv', '--alluredir', './Report/report', '--clean-alluredir'])
    # allure generate --clean report