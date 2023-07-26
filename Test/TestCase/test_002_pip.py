import time
from time import sleep
import pytest
import allure
import os
# 导入本用例用到的页面对象文件
from Test.PageObject import login_page
from Test.PageObject import pip_page
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
@allure.epic('管廊专项')
@allure.story("管廊模块")
@pytest.mark.Pipe
@pytest.mark.parametrize(("username", "password", "status"), data)
class TestPip():
    def setup_methon(self):
        print("----startPip-----")

    def teardown_methon(self):
        print('----Pipend----')


    @allure.severity("critical")
    def test_001_PipWarn(self, browser, username, password, status):
        allure.dynamic.title('管廊预警数一致性测试')
        pip_page.PipScenario(browser).Pip()
        map_text = common_page.ComOper(browser).get_map_text()
        if map_text == '2d':
            with allure.step("step:切换2d地图，比对总数"):
                common_page.ComScenario(browser).map_switch()
                sleep(3)
                tol_text = pip_page.PipOper(browser).get_Pip_warn_tol()
                pip_page.PipScenario(browser).Pip_warn()
                num_text = pip_page.PipOper(browser).get_Pip_warn_num()
        else:
            with allure.step("step:比对总数"):
                tol_text = pip_page.PipOper(browser).get_Pip_warn_tol()
                pip_page.PipScenario(browser).Pip_warn()
                num_text = pip_page.PipOper(browser).get_Pip_warn_num()
        assert tol_text == num_text

    @allure.severity("critical")
    def test_002_PipWarnpoint(self, browser, username, password, status):
        allure.dynamic.title('管廊预警打点测试')
        num_text = pip_page.PipOper(browser).get_Pip_warn_num()
        if num_text != '0':
            with allure.step("step:管廊预警点击打点"):
                num1_text = pip_page.PipOper(browser).get_Pip_warn1_num()
                num2_text = pip_page.PipOper(browser).get_Pip_warn2_num()
                num3_text = pip_page.PipOper(browser).get_Pip_warn3_num()
                num4_text = pip_page.PipOper(browser).get_Pip_warn4_num()
                # pip_page.PipScenario(browser).Pip_warnpoint()
                if num4_text != '0':
                    pip_page.PipScenario(browser).Pip_warn4()
                    sleep(1)
                    common_page.ComScenario(browser).sub_title_click()
                    assert common_page.ComScenario(browser).sikuli_warn4_click()
                    assert pip_page.PipScenario(browser).warn4_window()
                elif num3_text != '0':
                    # pip_page.PipScenario(browser).Pip_warn()
                    pip_page.PipScenario(browser).Pip_warn3()
                    sleep(1)
                    common_page.ComScenario(browser).sub_title_click()
                    assert common_page.ComScenario(browser).sikuli_warn3_click()
                    assert pip_page.PipScenario(browser).warn3_window()
                elif num2_text != '0':
                    # pip_page.PipScenario(browser).Pip_warn()
                    pip_page.PipScenario(browser).Pip_warn2()
                    sleep(1)
                    common_page.ComScenario(browser).sub_title_click()
                    assert common_page.ComScenario(browser).sikuli_warn2_click()
                    assert pip_page.PipScenario(browser).warn3_window()
                elif num1_text != '0':
                    # pip_page.PipScenario(browser).Pip_warn()
                    pip_page.PipScenario(browser).Pip_warn1()
                    sleep(1)
                    common_page.ComScenario(browser).sub_title_click()
                    assert common_page.ComScenario(browser).sikuli_warn1_click()
                    assert pip_page.PipScenario(browser).warn2_window()
                else:
                    assert False
        else:
            with allure.step("step:预警数为0"):
                pass

    @allure.severity("critical")
    def test_003_PipDevicepoint(self, browser, username, password, status):
        allure.dynamic.title('管廊设备详情测试')
        pip_page.PipScenario(browser).Pip_device()  # 点击监测设备按钮
        tol_text = pip_page.PipOper(browser).get_Pip_device_tol() + ' 台'    # 获取监测设备总数
        if tol_text != '0':
            num_text = pip_page.PipOper(browser).get_Pip_device_num()   # 获取下拉框设备总数
            time.sleep(3)
            pip_page.PipScenario(browser).Pip_devicepoint() # 设备打点
            common_page.ComScenario(browser).sub_title_click()   # 点击专项标题，收起设备下拉框
            sleep(2)
            pip_page.PipScenario(browser).sikuli_Pip_devicepoint()  # 调用sikuli识别图像定位点击设备点位
            common_page.ComScenario(browser).sikuli_title_hover()
            # sleep(1)
            assert pip_page.PipScenario(browser).sikuli_Pip_devicelocation()
            pip_page.PipScenario(browser).sikuli_Pip_deviceview()  # 查看设备详情
            # pip_page.PipScenario(browser).sikuli_Pip_deviceview()
            pip_page.PipOper(browser).get_Pip_device_name()
            assert pip_page.PipOper(browser).get_Pip_device_name() is not None
            assert pip_page.PipOper(browser).get_Pip_device_type() is not None
            assert pip_page.PipOper(browser).get_Pip_device_install() is not None
            assert pip_page.PipOper(browser).get_Pip_device_coor() is not None
            common_page.ComScenario(browser).sikuli_close()
            common_page.ComScenario(browser).sikuli_close()
            # sleep(2)

        else:
            num_text = pip_page.PipOper(browser).get_Pip_device_num()
        assert tol_text == num_text

    @allure.severity("critical")
    def test_004_Pipdevice(self, browser, username, password, status):
        allure.dynamic.title('管廊监测设备顶部在线+离线=总数测试')
        tol_text = pip_page.PipOper(browser).get_Pip_device_tol()# 获取监测设备总数
        online_tol = int(pip_page.PipOper(browser).get_Pip_device_onlinetol())
        offline_tol = int(pip_page.PipOper(browser).get_Pip_device_offlinetol())
        assert int(tol_text) == sum([online_tol,offline_tol])

    @allure.severity("critical")
    def test_005_Piponlinedevice(self, browser, username, password, status):
        allure.dynamic.title('管廊监测设备在线数量准确性测试')
        online_tol = pip_page.PipOper(browser).get_Pip_device_onlinetol()
        pip_page.PipScenario(browser).Pip_onlinedevice()  # 点击在线监测设备按钮
        online_num = pip_page.PipOper(browser).get_Pip_device_onlinenum()
        online_sum = pip_page.PipScenario(browser).online_sum()
        assert  int(online_tol) == int(common_page.ComScenario.retain_numbers(self,online_num))
        assert online_sum == int(online_tol)

    @allure.severity("critical")
    def test_006_Pipofflinedevice(self, browser, username, password, status):
        allure.dynamic.title('管廊监测设备离线数量准确性测试')
        common_page.ComScenario(browser).sub_title_click()
        offline_tol = pip_page.PipOper(browser).get_Pip_device_offlinetol()
        pip_page.PipScenario(browser).Pip_offlinedevice()  # 点击离线监测设备按钮
        offline_num = pip_page.PipOper(browser).get_Pip_device_offlinenum()
        offline_sum = pip_page.PipScenario(browser).offline_sum()
        assert int(offline_tol) == int(common_page.ComScenario.retain_numbers(self,offline_num))
        assert offline_sum == int(offline_tol)

    @allure.severity("critical")
    def test_007_Pipobject(self, browser, username, password, status):
        allure.dynamic.title('管廊监测对象测试')
        common_page.ComScenario(browser).sub_title_click()
        pip_page.PipScenario(browser).sikuli_Pip_len()
        assert pip_page.PipScenario(browser).sikuli_Pip_len1()
        pip_page.PipScenario(browser).sikuli_Pip_road()
        assert pip_page.PipScenario(browser).sikuli_Pip_road1()
        pip_page.PipScenario(browser).sikuli_Pip_firezone()
        # assert pip_page.PipScenario(browser).sikuli_Pip_firezeon1()
        common_page.ComScenario(browser).sikuli_close()
        pip_page.PipScenario(browser).sikuli_Pip_Perception()
        # assert pip_page.PipScenario(browser).sikuli_Pip_Perception1()
        common_page.ComScenario(browser).sikuli_close()
        pip_page.PipScenario(browser).sikuli_Pip_cabin()
        assert pip_page.PipScenario(browser).sikuli_Pip_cabin1()
        pip_page.PipScenario(browser).sikuli_Pip_linetype()
        assert pip_page.PipScenario(browser).sikuli_Pip_linetype1()

    @allure.severity("critical")
    def test_008_Pipmonitoring(self, browser, username, password, status):
        allure.dynamic.title('管廊左侧监测设备数量准确性测试')
        common_page.ComScenario(browser).sub_title_click()
        with allure.step("比对环境监测设备数量"):
            env_sum, env_tol = pip_page.PipScenario(browser).Pip_monitoring_envnum()
            assert env_tol == env_sum
        with allure.step("比对结构监测设备数量"):
            str_sum, str_tol = pip_page.PipScenario(browser).Pip_monitoring_strnum()
            assert str_tol == str_sum
        with allure.step("比对管线监测设备数量"):
            pipe_sum, pipe_tol = pip_page.PipScenario(browser).Pip_monitoring_pipenum()
            assert pipe_tol == pipe_sum
        with allure.step("比对消防监测设备数量"):
            fire_sum, fire_tol = pip_page.PipScenario(browser).Pip_monitoring_firenum()
            assert fire_tol == fire_sum
        with allure.step("比对左侧监测设备和总数数量"):
            device_tol = pip_page.PipScenario(browser).Pip_device_tol()
            assert device_tol == sum([env_tol, str_tol, pipe_tol, fire_tol])
        # sleep(1)


# if __name__ == '__main__':
#     pytest.main(['-sv', '--alluredir', '../../Report/report', '--clean-alluredir'])
#     # allure generate --clean report