import time
from time import sleep
import pytest
import allure
import os
# 导入本用例用到的页面对象文件
from Test.PageObject import login_page
from Test.PageObject import supply_page
from Common.parse_csv import parse_csv
from Common.parse_yml import parse_yml
from Test.PageObject import common_page
# from conftest import browser

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
@allure.epic('供水专项')
@allure.story("供水报警模块")
@pytest.mark.Supply
@pytest.mark.parametrize(("username", "password", "status"), data)
class TestSupply_alarm():
    @allure.severity("critical")
    @pytest.mark.Supplytt
    def test_001_supplyAlarm(self, browser, username, password, status):
        allure.dynamic.title('供水报警数一致性测试')
        supply_page.PipScenario(browser).water()
        map_text = common_page.ComOper(browser).get_map_text()
        if map_text == '2d':
            with allure.step("step:切换2d地图，比对总数"):
                common_page.ComScenario(browser).map_switch()
                sleep(3)
                tol_text = supply_page.PipOper(browser).get_Alarm_tol()
                supply_page.PipScenario(browser).water_alarm()
                num_text = supply_page.PipOper(browser).get_Alarm_undevice()
        else:
            with allure.step("step:比对总数"):
                tol_text = supply_page.PipOper(browser).get_Alarm_tol()
                supply_page.PipScenario(browser).water_alarm()
                num_text = supply_page.PipOper(browser).get_Alarm_undevice()
        assert tol_text == num_text

    @allure.severity("critical")
    def test_002_supplyAlarmSub(self, browser, username, password, status):
        allure.dynamic.title('供水报警下拉处置+未处置=总数测试')
        num_text = supply_page.PipOper(browser).get_Alarm_sub()
        count = supply_page.PipOper(browser).get_Alarm_subcount()
        disposed_sub = supply_page.PipOper(browser).get_Alarm_subdisposed()
        assert int(count) == int(num_text)+int(disposed_sub)

    @allure.severity("critical")
    def test_003_supplyAlarmpoint(self, browser, username, password, status):
        allure.dynamic.title('供水报警打点测试')
        # browser.get(url)
        # # 登录的3个操作用业务场景方法一条语句代替
        # login_page.LoginScenario(browser).login(username, password)
        num_text = supply_page.PipOper(browser).get_Alarm_sub()
        sleep(1)
        tol_text = supply_page.PipScenario(browser).alarm_sum()
        with allure.step("step:比对各区数量相加是否一致"):
         assert tol_text == int(num_text)
        if num_text != '0':
            with allure.step("step:供水报警点击打点"):
                supply_page.PipScenario(browser).water_alarm_sub()
                common_page.ComScenario(browser).sub_title_click()
                common_page.ComScenario(browser).sikuli_alarm_click()
                if common_page.ComScenario(browser).sikuli_alarmview_find():
                    assert supply_page.PipScenario(browser).alarm_window()
                    # common_page.ComScenario(browser).sikuli_close1()
                else:
                    assert supply_page.PipScenario(browser).sikuli_alarm_list()

    @allure.severity("critical")
    def test_004_supplyAlarmList(self, browser, username, password, status):
        allure.dynamic.title('供水报警列表跳转测试')
        common_page.ComScenario(browser).list_close_click()
        supply_page.PipScenario(browser).water_alarm()
        common_page.ComScenario(browser).sub_more_click()
        sleep(0.5)
        list_title = common_page.ComScenario(browser).alarm_list_title()
        assert list_title == '报警列表'

    @allure.severity("critical")
    def test_005_supplyAlarmListpoint(self, browser, username, password, status):
        allure.dynamic.title('供水报警列表打点测试')
        list_toatal = common_page.ComScenario(browser).alarm_list_total()
        if list_toatal != '共 0 条':
            with allure.step("step:判断字段不为空"):
                assert supply_page.PipScenario(browser).alarm_list_value()
            with allure.step("step:查看定位"):
                supply_page.PipScenario(browser).alarm_list_do()
                common_page.ComScenario(browser).alarmlist_close_click()
                common_page.ComScenario(browser).sikuli_alarm_click()
                assert supply_page.PipScenario(browser).alarm_window()
        else:
            pass

@allure.suite('驾驶舱测试')
@allure.epic('供水专项')
@allure.story("供水预警模块")
@pytest.mark.Supply
@pytest.mark.parametrize(("username", "password", "status"), data)
class TestSupply_warn():
    @allure.severity("critical")
    def test_001_supplyWarn(self, browser, username, password, status):
        allure.dynamic.title('供水预警数量准确测试')
        warn_total = supply_page.PipScenario(browser).warn_total()
        supply_page.PipScenario(browser).click_warn_total()
        warn_num = supply_page.PipScenario(browser).warn_num()
        warn_sum = supply_page.PipScenario(browser).warn_sum()
        with allure.step("step:比对预警数量"):
            assert warn_total == warn_num
            assert warn_sum == int(warn_num)
        if warn_sum != 0:
            with allure.step("step:供水预警点击打点"):
                num1_text = supply_page.PipOper(browser).get_Warn1_num()
                num2_text = supply_page.PipOper(browser).get_Warn2_num()
                num3_text = supply_page.PipOper(browser).get_Warn3_num()
                num4_text = supply_page.PipOper(browser).get_Warn4_num()
                if num4_text != '0':
                    supply_page.PipScenario(browser).click_warn4_num()
                    sleep(1)
                    common_page.ComScenario(browser).sub_title_click()
                    assert common_page.ComScenario(browser).sikuli_warn4_click()
                elif num3_text != '0':
                    supply_page.PipScenario(browser).click_warn3_num()
                    sleep(1)
                    common_page.ComScenario(browser).sub_title_click()
                    assert common_page.ComScenario(browser).sikuli_warn4_click()
                elif num2_text != '0':
                    supply_page.PipScenario(browser).click_warn2_num()
                    sleep(1)
                    common_page.ComScenario(browser).sub_title_click()
                    assert common_page.ComScenario(browser).sikuli_warn4_click()
                elif num1_text != '0':
                    supply_page.PipScenario(browser).click_warn1_num()
                    sleep(1)
                    common_page.ComScenario(browser).sub_title_click()
                    assert common_page.ComScenario(browser).sikuli_warn4_click()
                else:
                    assert False
        else:
            with allure.step("step:预警数为0"):
                pass

    @allure.severity("critical")
    def test_002_supplyWarnList(self, browser, username, password, status):
        allure.dynamic.title('供水平台预警列表跳转测试')
        # supply_page.PipScenario(browser).click_warn_total()
        common_page.ComScenario(browser).warn_more_click()
        sleep(0.5)
        list_title = common_page.ComScenario(browser).warn_list_title()
        common_page.ComScenario(browser).warnlist_close_click()
        # common_page.ComScenario(browser).sikuli_close()
        assert list_title == '平台预警列表'

@allure.suite('驾驶舱测试')
@allure.epic('供水专项')
@allure.story("供水设备模块")
@pytest.mark.Supply
@pytest.mark.parametrize(("username", "password", "status"), data)
class TestSupply_device():
    @allure.severity("critical")
    def test_001_supplydevice(self, browser, username, password, status):
        allure.dynamic.title('供水监测设备顶部在线+离线=总数测试')
        tol_text = common_page.ComOper(browser).get_device_total()
        online_tol = int(common_page.ComOper(browser).get_device_ontotal())
        offline_tol = int(common_page.ComOper(browser).get_device_offtotal())
        assert int(tol_text) == sum([online_tol, offline_tol])

    # @pytest.mark.Supplytt
    @allure.severity("critical")
    def test_002_supplydevice(self, browser, username, password, status):
        allure.dynamic.title('供水监测设备数量准确性测试')
        tol = common_page.ComOper(browser).get_device_total()
        common_page.ComScenario(browser).device_total_click()  # 点击顶部监测设备按钮
        num = common_page.ComOper(browser).get_device_num()
        sum = common_page.ComScenario(browser).device_sum()
        num_1 = int(common_page.ComScenario.retain_numbers(self,num))
        tol_1 = int(tol)
        assert tol_1 == num_1
        assert sum == tol_1

    @allure.severity("critical")
    def test_003_supplyonlinedevice(self, browser, username, password, status):
        allure.dynamic.title('供水监测设备在线数量准确性测试')
        online_tol = common_page.ComOper(browser).get_device_ontotal()
        common_page.ComScenario(browser).device_ontotal_click()  # 点击顶部监测设备按钮
        online_num = common_page.ComOper(browser).get_device_onnum()
        online_sum = common_page.ComScenario(browser).device_sum1()
        assert int(online_tol) == int(common_page.ComScenario.retain_numbers(self,online_num))
        assert online_sum == int(online_tol)

    @allure.severity("critical")
    def test_004_supplyofflinedevice(self, browser, username, password, status):
        allure.dynamic.title('供水监测设备离线数量准确性测试')
        # common_page.ComScenario(browser).sub_title_click()
        offline_tol = common_page.ComOper(browser).get_device_offtotal()
        common_page.ComScenario(browser).device_offtotal_click()  # 点击离线监测设备按钮
        offline_num = common_page.ComOper(browser).get_device_offnum()
        offline_sum = common_page.ComScenario(browser).device_sum1()
        assert int(offline_tol) == int(common_page.ComScenario.retain_numbers(self,offline_num))
        assert offline_sum == int(offline_tol)
        