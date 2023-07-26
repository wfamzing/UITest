import os

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = None

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()  # rep可以拿到用例的执行结果详情

    # 以下为实现异常截图的代码：
    # rep.when可选参数有call、setup、teardown，
    # call表示为用例执行环节、setup、teardown为环境初始化和清理环节
    # 这里只针对用例执行且失败的用例进行异常截图
    if rep.when == "call" and rep.failed:
        # 检查driver对象是否包含get_screenshot_as_png方法
        mode = "a" if os.path.exists("./Report/report/failures") else "w"
        with open("./Report/report/failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # pic_info = adb_screen_shot()
        with allure.step('添加失败截图...'):
            allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)

@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        options = Options()
        options.add_argument("--kiosk") # 全屏效果，相当于F11
        # 禁止显示“Chrome正受到自动化软件的控制”
        options.add_experimental_option("prefs", {"credentials_enable_service": False,"profile.password_manager_enabled": False})
        options.add_experimental_option("excludeSwitches", ['enable-automation'])   #禁止显示“Chrome正受到自动化软件的控制”
        driver = webdriver.Chrome(options=options)
        # driver.maximize_window()
    yield driver
    # return driver
    # 所有用例执行完毕退出浏览器
    driver.quit()