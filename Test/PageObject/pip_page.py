'''
登录页
'''
# 页面元素对象层
from selenium.webdriver import ActionChains
from Base.base import Base
import time
from Test.PageObject import sikuli
from Test.PageObject import common_page

UrbanLife_btn = "xpath,//*[@id='box']/div[2]"  # 城市生命线元素
Pip_btn = "xpath,//*[@id='app']/div/div[3]/div[4]/div[1]"  # 城市生命线元素
Warning_btn = "css,.alarm-total.el-popover__reference"  # 城市生命线元素
Warning_more = "css,.handle-btn.btn"
# Warning_total = "css,.alarm-total.selected>span:nth-child(2)"
Warning_total = "xpath,//*[@id='app']/div/div[2]/div/div[7]/div[3]/div/span[1]/div/span[2]"
Warning_num = "css,div.cursor:nth-child(2) > span:nth-child(3)"
Warning1_num = "css,[aria-hidden='false']>div.popover-content.warning>div.warning>div.warning-item.level1>span.value.level1"
Warning2_num = "css,[aria-hidden='false']>div.popover-content.warning>div.warning>div.warning-item.level2>span.value.level2"
Warning3_num = "css,[aria-hidden='false']>div.popover-content.warning>div.warning>div.warning-item.level3>span.value.level3"
Warning4_num = "css,[aria-hidden='false']>div.popover-content.warning>div.warning>div.warning-item.level4>span.value.level4"
Warning1_btn = "css,.warning-item.level1"
Warning2_btn = "css,.warning-item.level2"
Warning3_btn = "css,.warning-item.level3"
Warning4_btn = "css,.warning-item.level4"
device_total = "xpath,//*[@id='app']/div/div[2]/div/div[7]/div[3]/div/span[2]/div/span[2]"
device_online_total= "css,#app > div > div.frontend > div > div.bridge-monitor-container > div.alarm-list > div > span:nth-child(3) > div.device-total.online.el-popover__reference > span:nth-child(2)"
device_offline_total = "css,#app > div > div.frontend > div > div.bridge-monitor-container > div.alarm-list > div > span:nth-child(4) > div > span:nth-child(2)"
device_num = "css,[aria-hidden='false']>div.popover-content.warning>div.total.cursor>span.value"
device_onlinenum = "css,[aria-hidden='false'] > div.popover-content.warning > div.total.online.cursor > span.value"
device_offlinenum = "css,[aria-hidden='false'] > div.popover-content.warning > div.total.offline.curosr > span.value"
device_xyl = "css,[aria-hidden='false']>div.popover-content.warning>div.device>div:nth-child(5)"
device_view = "css,button.el-button.el-button--text.el-button--small:nth-child(1)"
device_name = "css,.list-item:nth-child(1)>span:nth-child(2)"
device_type = "css,.list-item:nth-child(2)>span:nth-child(2)"
device_install = "css,.list-item:nth-child(3)>span:nth-child(2)"
device_coor = "css,.list-item:nth-child(4)>span:nth-child(2)"
Pip_len = "css,.monitoring-object-box-list>div:nth-child(1)>div.content>div.count-unit>span:nth-child(1)"
road = "css,.monitoring-object-box-list>div:nth-child(2)>div.content>div.count-unit>span:nth-child(1)"
qingdao_onine = "css,[aria-hidden='false'] > div.popover-content.warning > div.total.online.cursor > span.value"
gongbeilu_online = "css,[aria-hidden='false'] > div.popover-content.warning > div.online-device > div:nth-child(1) > span.value"
jiaodongjichang_online = "css,[aria-hidden='false'] > div.popover-content.warning > div.online-device > div:nth-child(2) > span.value"
jiangshanlu_online = "css,[aria-hidden='false'] > div.popover-content.warning > div.online-device > div:nth-child(3) > span.value"
langu_online = "css,[aria-hidden='false'] > div.popover-content.warning > div.online-device > div:nth-child(4) > span.value"
anshunlu_online = "css,[aria-hidden='false'] > div.popover-content.warning > div.online-device > div:nth-child(5) > span.value"
haikoulu_online = "css,[aria-hidden='false'] > div.popover-content.warning > div.online-device > div:nth-child(6) > span.value"
zhongdeshengtaiyuan_online = "css,[aria-hidden='false'] > div.popover-content.warning > div.online-device > div:nth-child(7) > span.value"
zhilidaolu_online = "css,[aria-hidden='false'] > div.popover-content.warning > div.online-device > div:nth-child(8) > span.value"
xiyilu_online = "css,[aria-hidden='false'] > div.popover-content.warning > div.online-device > div:nth-child(9) > span.value"
gongbeilu_offline = "css,[aria-hidden='false'] > div.popover-content.warning > div.offline-device > div:nth-child(1) > span.value"
jiaodongjichang_offline = "css,[aria-hidden='false'] > div.popover-content.warning > div.offline-device > div:nth-child(2) > span.value"
jiangshanlu_offline = "css,[aria-hidden='false'] > div.popover-content.warning > div.offline-device > div:nth-child(3) > span.value"
langu_offline = "css,[aria-hidden='false'] > div.popover-content.warning > div.offline-device > div:nth-child(4) > span.value"
anshunlu_offline = "css,[aria-hidden='false'] > div.popover-content.warning > div.offline-device > div:nth-child(5) > span.value"
haikoulu_offline = "css,[aria-hidden='false'] > div.popover-content.warning > div.offline-device > div:nth-child(6) > span.value"
zhongdeshengtaiyuan_offline = "css,[aria-hidden='false'] > div.popover-content.warning > div.offline-device > div:nth-child(7) > span.value"
zhilidaolu_offline = "css,[aria-hidden='false'] > div.popover-content.warning > div.offline-device > div:nth-child(8) > span.value"
xiyilu_offline = "css,[aria-hidden='false'] > div.popover-content.warning > div.offline-device > div:nth-child(9) > span.value"
monitoring_env = "css,div.item-monitoring-equipment:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)"
monitoring_onenv = "css,div.item-monitoring-equipment:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"
monitoring_offenv = "css,div.item-monitoring-equipment:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)"
monitoring_str = "css,div.item-monitoring-equipment:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)"
monitoring_onstr = "css,div.item-monitoring-equipment:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"
monitoring_offstr = "css,div.item-monitoring-equipment:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)"
monitoring_pipe = "css,div.item-monitoring-equipment:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)"
monitoring_onpipe = "css,div.item-monitoring-equipment:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"
monitoring_offpipe = "css,div.item-monitoring-equipment:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)"
monitoring_fire = "css,div.item-monitoring-equipment:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)"
monitoring_onfire = "css,div.item-monitoring-equipment:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"
monitoring_offfire = "css,div.item-monitoring-equipment:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)"
iframe1 = "css,.em-map-div>iframe:nth-child(1)"
warn_title = "css,.map-title"
warn_level4 = "css,.level4 > span:nth-child(1)"
warn_level3 = "css,.level3 > span:nth-child(1)"
warn_level2 = "css,.level2 > span:nth-child(1)"
warn_level1 = "css,.level1 > span:nth-child(1)"
warn_location = "css,div.kv-li:nth-child(2) > div:nth-child(2) > span:nth-child(1)"
warn_text = "css,div.kv-li:nth-child(3) > div:nth-child(2) > span:nth-child(1)"
close_btn = "class,close-btn"
#   图片
devicepointImage = r"D:\wf\EmergUItest\Common\image\pip\PipDevice.png"
deviceviewImage = r"D:\wf\EmergUItest\Common\image\pip\view.png"
devicelocationImage = r"D:\wf\EmergUItest\Common\image\pip\deviceLocation.png"
piplenImage = r"D:\wf\EmergUItest\Common\image\pip\piplen.png"
piproadImage = r"D:\wf\EmergUItest\Common\image\pip\road.png"
piplen1Image = r"D:\wf\EmergUItest\Common\image\pip\qqq.png"
piproad1Image = r"D:\wf\EmergUItest\Common\image\pip\piprrr.png"
firezoneImage = r"D:\wf\EmergUItest\Common\image\pip\fhfq.png"
firezone1Image = r"D:\wf\EmergUItest\Common\image\pip\firezone1.png"
PerceptionImage = r"D:\wf\EmergUItest\Common\image\pip\gzsb.png"
Perception1Image = r"D:\wf\EmergUItest\Common\image\pip\gzsb1.png"
cabinImage = r"D:\wf\EmergUItest\Common\image\pip\cabin.png"
cabin1Image = r"D:\wf\EmergUItest\Common\image\pip\cabin1.png"
linetypeImage = r"D:\wf\EmergUItest\Common\image\pip\linetype.png"
linetype1Image = r"D:\wf\EmergUItest\Common\image\pip\linetype1.png"

class PipPage(object):
    def __init__(self, browser):
        # 私有方法
        self.driver = browser

    def find_UrbanLife(self):
        # 查找城市生命线
        # ele = self.driver.find_element_by_id('username')
        # ele = self.driver.find_element_by_name('username')
        ele = Base(self.driver).get_element(UrbanLife_btn)
        return ele

    def find_Pip(self):
        # 查找管理专项
        # ele = self.driver.find_element_by_id('password')
        ele = Base(self.driver).get_element(Pip_btn)
        return ele

    def find_Warn_btn(self):
        # 查找预警总数按钮
        # ele = self.driver.find_element_by_id('login-submit')
        ele = Base(self.driver).get_element(Warning_btn)
        return ele

    def find_Pip_warn_tol(self):
        # 查找预警总数值
        # ele = self.driver.find_element_by_id('loggedas')
        ele = Base(self.driver).get_element(Warning_total)
        return ele

    def find_Pip_warn_num(self):
        # 查找预警框总数
        # ele = self.driver.find_element_by_id('flash_error')
        ele = Base(self.driver).get_element(Warning_num)
        return ele

    def find_Pip_warn1_num(self):
        # 查找预警框总数
        # ele = self.driver.find_element_by_id('flash_error')
        ele = Base(self.driver).get_element(Warning1_num)
        return ele

    def find_Pip_warn2_num(self):
        # 查找预警框总数
        # ele = self.driver.find_element_by_id('flash_error')
        ele = Base(self.driver).get_element(Warning2_num)
        return ele

    def find_Pip_warn3_num(self):
        # 查找预警框总数
        # ele = self.driver.find_element_by_id('flash_error')
        ele = Base(self.driver).get_element(Warning3_num)
        return ele

    def find_Pip_warn4_num(self):
        # 查找预警框总数
        # ele = self.driver.find_element_by_id('flash_error')
        ele = Base(self.driver).get_element(Warning4_num)
        return ele

    def find_Pip_warn1_btn(self):
        # 查找一级预警按钮
        ele = Base(self.driver).get_element(Warning1_btn)
        return ele

    def find_Pip_warn2_btn(self):
        # 查找预警按钮
        ele = Base(self.driver).get_element(Warning2_btn)
        return ele

    def find_Pip_warn3_btn(self):
        # 查找预警按钮
        ele = Base(self.driver).get_element(Warning3_btn)
        return ele

    def find_Pip_warn4_btn(self):
        # 查找预警按钮
        ele = Base(self.driver).get_element(Warning4_btn)
        return ele

    def find_Pip_device_tol(self):
        # 查找设备总数
        # ele = self.driver.find_element_by_id('flash_error')
        ele = Base(self.driver).get_element(device_total)
        return ele

    def find_Pip_device_onlinetol(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(device_online_total)
        return ele
    def find_Pip_device_offlinetol(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(device_offline_total)
        return ele

    def find_Pip_device_onlinenum(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(device_onlinenum)
        return ele
    def find_Pip_device_offlinenum(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(device_offlinenum)
        return ele

    def find_Pip_onlinedevice_gongbei(self):
        ele = Base(self.driver).get_element(gongbeilu_online)
        return ele
    def find_Pip_onlinedevice_jiaodong(self):
        ele = Base(self.driver).get_element(jiaodongjichang_online)
        return ele
    def find_Pip_onlinedevice_jiangshan(self):
        ele = Base(self.driver).get_element(jiangshanlu_online)
        return ele
    def find_Pip_onlinedevice_langu(self):
        ele = Base(self.driver).get_element(langu_online)
        return ele
    def find_Pip_onlinedevice_anshun(self):
        ele = Base(self.driver).get_element(anshunlu_online)
        return ele
    def find_Pip_onlinedevice_haikou(self):
        ele = Base(self.driver).get_element(haikoulu_online)
        return ele
    def find_Pip_onlinedevice_zhongde(self):
        ele = Base(self.driver).get_element(zhongdeshengtaiyuan_online)
        return ele
    def find_Pip_onlinedevice_zhilidao(self):
        ele = Base(self.driver).get_element(zhilidaolu_online)
        return ele
    def find_Pip_onlinedevice_xiyilu(self):
        ele = Base(self.driver).get_element(xiyilu_online)
        return ele

    def find_Pip_offlinedevice_gongbei(self):
        ele = Base(self.driver).get_element(gongbeilu_offline)
        return ele
    def find_Pip_offlinedevice_jiaodong(self):
        ele = Base(self.driver).get_element(jiaodongjichang_offline)
        return ele
    def find_Pip_offlinedevice_jiangshan(self):
        ele = Base(self.driver).get_element(jiangshanlu_offline)
        return ele
    def find_Pip_offlinedevice_langu(self):
        ele = Base(self.driver).get_element(langu_offline)
        return ele
    def find_Pip_offlinedevice_anshun(self):
        ele = Base(self.driver).get_element(anshunlu_offline)
        return ele
    def find_Pip_offlinedevice_haikou(self):
        ele = Base(self.driver).get_element(haikoulu_offline)
        return ele
    def find_Pip_offlinedevice_zhongde(self):
        ele = Base(self.driver).get_element(zhongdeshengtaiyuan_offline)
        return ele
    def find_Pip_offlinedevice_zhilidao(self):
        ele = Base(self.driver).get_element(zhilidaolu_offline)
        return ele
    def find_Pip_offlinedevice_xiyilu(self):
        ele = Base(self.driver).get_element(xiyilu_offline)
        return ele

    def find_Pip_device_offlinetol(self):
        # 查找设备总数
        # ele = self.driver.find_element_by_id('flash_error')
        ele = Base(self.driver).get_element(device_offline_total)
        return ele

    def find_Pip_device_num(self):
        # 查找设备框总数
        # ele = self.driver.find_element_by_id('flash_error')
        ele = Base(self.driver).get_element(device_num)
        return ele

    def find_Pip_device_point(self):
        # 查找预警框总数
        # ele = self.driver.find_element_by_id('flash_error')
        ele = Base(self.driver).get_element(device_xyl)
        return ele

    def find_Pip_device_view(self):
        ele = Base(self.driver).get_element(device_view)
        return ele

    def find_Pip_device_name(self):
        ele = Base(self.driver).get_element(device_name)
        return ele

    def find_Pip_device_type(self):
        ele = Base(self.driver).get_element(device_type)
        return ele

    def find_Pip_device_install(self):
        ele = Base(self.driver).get_element(device_install)
        return ele

    def find_Pip_device_coor(self):
        ele = Base(self.driver).get_element(device_coor)
        return ele

    def find_Pip_len(self):
        ele = Base(self.driver).get_element(Pip_len)
        return ele

    def find_Pip_monitoring_envtol(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(monitoring_env)
        return ele
    def find_Pip_monitoring_onenvtol(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(monitoring_onenv)
        return ele
    def find_Pip_monitoring_offenvtol(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(monitoring_offenv)
        return ele
    def find_Pip_monitoring_strtol(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(monitoring_str)
        return ele
    def find_Pip_monitoring_onstrtol(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(monitoring_onstr)
        return ele
    def find_Pip_monitoring_offstrtol(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(monitoring_offstr)
        return ele
    def find_Pip_monitoring_pipetol(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(monitoring_pipe)
        return ele
    def find_Pip_monitoring_onpipetol(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(monitoring_onpipe)
        return ele
    def find_Pip_monitoring_offpipetol(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(monitoring_offpipe)
        return ele
    def find_Pip_monitoring_firetol(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(monitoring_fire)
        return ele
    def find_Pip_monitoring_onfiretol(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(monitoring_onfire)
        return ele
    def find_Pip_monitoring_offfiretol(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(monitoring_offfire)
        return ele

    def find_warn_title(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(warn_title)
        return ele
    def find_warn_level4(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(warn_level4)
        return ele
    def find_warn_level3(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(warn_level3)
        return ele
    def find_warn_level2(self):
        ele = Base(self.driver).get_element(warn_level2)
        return ele
    def find_warn_level1(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(warn_level1)
        return ele
    def find_warn_location(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(warn_location)
        return ele
    def find_warn_text(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(warn_text)
        return ele

    def find_close_btn(self):
        # 查找设备总数
        ele = Base(self.driver).get_element(close_btn)
        return ele
    # def find_verification_code(self):
    #     ele = self.driver.find_element_by_id('aaa')
    #     return ele


# 页面元素操作层
class PipOper(object):
    def __init__(self, browser):
        # 私有方法，调用元素定位的类
        self.Pip_page = PipPage(browser)
        self.driver = browser

    def click_UrbanLife_btn(self):
        ele = self.Pip_page.find_UrbanLife()
        ActionChains(self.driver).click(ele).perform()

    def click_Pip_btn(self):
        ele = self.Pip_page.find_Pip()
        ActionChains(self.driver).click(ele).perform()

    def click_Warn_btn(self):
        ele = self.Pip_page.find_Warn_btn()
        ActionChains(self.driver).click(ele).perform()

    def click_Warn1_btn(self):
        ele = self.Pip_page.find_Pip_warn1_btn()
        ActionChains(self.driver).click(ele).perform()

    def click_Warn2_btn(self):
        ele = self.Pip_page.find_Pip_warn2_btn()
        ActionChains(self.driver).click(ele).perform()

    def click_Warn3_btn(self):
        ele = self.Pip_page.find_Pip_warn3_btn()
        ActionChains(self.driver).click(ele).perform()

    def click_Warn4_btn(self):
        ele = self.Pip_page.find_Pip_warn4_btn()
        ActionChains(self.driver).click(ele).perform()

    def click_Warnpoint_btn(self):
        ele = self.Pip_page.find_Pip_warn_tol()
        ActionChains(self.driver).click(ele).perform()

    def get_Pip_warn_tol(self):
        # time.sleep(1)
        # self.driver.implicitly_wait(3)
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_warn_tol().text

    def get_Pip_warn_num(self):
        # time.sleep(1)
        # self.driver.implicitly_wait(3)
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_warn_num().text

    def get_Pip_warn1_num(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_warn1_num().text

    def get_Pip_warn2_num(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_warn2_num().text

    def get_Pip_warn3_num(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_warn3_num().text

    def get_Pip_warn4_num(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_warn4_num().text

    def click_device_btn(self):
        ele = self.Pip_page.find_Pip_device_tol()
        ActionChains(self.driver).click(ele).perform()

    def click_device_onlinebtn(self):
        ele = self.Pip_page.find_Pip_device_onlinetol()
        ActionChains(self.driver).click(ele).perform()

    def click_device_offlinebtn(self):
        ele = self.Pip_page.find_Pip_device_offlinetol()
        ActionChains(self.driver).click(ele).perform()

    def get_Pip_device_tol(self):
        # 返回总设备数
        return self.Pip_page.find_Pip_device_tol().text

    def get_onlinedevice_gongbei(self):
        return self.Pip_page.find_Pip_onlinedevice_gongbei().text
    def get_onlinedevice_jiaodong(self):
        return self.Pip_page.find_Pip_onlinedevice_jiaodong().text
    def get_onlinedevice_jiangshan(self):
        return self.Pip_page.find_Pip_onlinedevice_jiangshan().text
    def get_onlinedevice_langu(self):
        return self.Pip_page.find_Pip_onlinedevice_langu().text
    def get_onlinedevice_anshun(self):
        return self.Pip_page.find_Pip_onlinedevice_anshun().text
    def get_onlinedevice_haikou(self):
        return self.Pip_page.find_Pip_onlinedevice_haikou().text
    def get_onlinedevice_zhongde(self):
        return self.Pip_page.find_Pip_onlinedevice_zhongde().text
    def get_onlinedevice_zhilidao(self):
        return self.Pip_page.find_Pip_onlinedevice_zhilidao().text
    def get_onlinedevice_xiyilu(self):
        return self.Pip_page.find_Pip_onlinedevice_xiyilu().text

    def get_offlinedevice_gongbei(self):
        return self.Pip_page.find_Pip_offlinedevice_gongbei().text
    def get_offlinedevice_jiaodong(self):
        return self.Pip_page.find_Pip_offlinedevice_jiaodong().text
    def get_offlinedevice_jiangshan(self):
        return self.Pip_page.find_Pip_offlinedevice_jiangshan().text
    def get_offlinedevice_langu(self):
        return self.Pip_page.find_Pip_offlinedevice_langu().text
    def get_offlinedevice_anshun(self):
        return self.Pip_page.find_Pip_offlinedevice_anshun().text
    def get_offlinedevice_haikou(self):
        return self.Pip_page.find_Pip_offlinedevice_haikou().text
    def get_offlinedevice_zhongde(self):
        return self.Pip_page.find_Pip_offlinedevice_zhongde().text
    def get_offlinedevice_zhilidao(self):
        return self.Pip_page.find_Pip_offlinedevice_zhilidao().text
    def get_offlinedevice_xiyilu(self):
        return self.Pip_page.find_Pip_offlinedevice_xiyilu().text

    def get_Pip_device_onlinetol(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_device_onlinetol().text

    def get_Pip_device_onlinenum(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_device_onlinenum().text

    def get_Pip_device_offlinenum(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_device_offlinenum().text

    def get_Pip_device_offlinetol(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_device_offlinetol().text

    def get_Pip_device_num(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_device_num().text

    def click_devicepoint_btn(self):
        ele = self.Pip_page.find_Pip_device_point()
        ActionChains(self.driver).click(ele).perform()

    def click_deviceview_btn(self):
        ele = self.Pip_page.find_Pip_device_view()
        ActionChains(self.driver).click(ele).perform()

    def get_Pip_device_name(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_device_name().text

    def get_Pip_device_type(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_device_type().text

    def get_Pip_device_install(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_device_install().text

    def get_Pip_device_coor(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_device_coor().text

    def hover_piplen(self):
        ele = self.Pip_page.find_Pip_len()
        ActionChains(self.driver).move_to_element(ele).perform()

    def get_Pip_monitoring_envtol(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_monitoring_envtol().text
    def get_Pip_monitoring_onenvtol(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_monitoring_onenvtol().text
    def get_Pip_monitoring_offenvtol(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_monitoring_offenvtol().text
    def get_Pip_monitoring_strtol(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_monitoring_strtol().text
    def get_Pip_monitoring_onstrtol(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_monitoring_onstrtol().text
    def get_Pip_monitoring_offstrtol(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_monitoring_offstrtol().text
    def get_Pip_monitoring_pipetol(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_monitoring_pipetol().text
    def get_Pip_monitoring_onpipetol(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_monitoring_onpipetol().text
    def get_Pip_monitoring_offpipetol(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_monitoring_offpipetol().text
    def get_Pip_monitoring_firetol(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_monitoring_firetol().text
    def get_Pip_monitoring_onfiretol(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_monitoring_onfiretol().text
    def get_Pip_monitoring_offfiretol(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Pip_monitoring_offfiretol().text

    def get_warn_title(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_warn_title().text
    def get_warn_level4(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_warn_level4().text
    def get_warn_level3(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_warn_level3().text
    def get_warn_level2(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_warn_level2().text
    def get_warn_level1(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_warn_level1().text
    def get_warn_location(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_warn_location().text
    def get_warn_text(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_warn_text().text

    def click_close_btn(self):
        ele = self.Pip_page.find_close_btn()
        ActionChains(self.driver).click(ele).perform()

    # def input_verfication_code(self, fixed_value=123456): # 万能验证码
    #     self.login_page.find_verification_code().send_keys(fixed_value)


# 页面业务场景层
class PipScenario(object):
    def __init__(self, browser):
        # 私有方法：调用页面元素操作
        self.Pip_oper = PipOper(browser)
        self.driver = browser

    def Pip(self):
        # 定义一个登录场景，用到了3个操作
        time.sleep(1)
        self.Pip_oper.click_UrbanLife_btn()
        time.sleep(1)
        self.Pip_oper.click_Pip_btn()

    def Pip_warn(self):
        time.sleep(1)
        self.Pip_oper.click_Warn_btn()

    def Pip_warn1(self):
        time.sleep(1)
        self.Pip_oper.click_Warn1_btn()

    def Pip_warn2(self):
        time.sleep(1)
        self.Pip_oper.click_Warn2_btn()

    def Pip_warn3(self):
        time.sleep(1)
        self.Pip_oper.click_Warn3_btn()

    def Pip_warn4(self):
        time.sleep(1)
        self.Pip_oper.click_Warn4_btn()

    # 预警打点
    def Pip_warnpoint(self):
        time.sleep(1)
        self.Pip_oper.click_Warnpoint_btn()

    # 设备下拉
    def Pip_device(self):
        # time.sleep(1)
        self.Pip_oper.click_device_btn()

    # 在线设备下拉
    def Pip_onlinedevice(self):
        # time.sleep(1)
        self.Pip_oper.click_device_onlinebtn()
    def online_sum(self):
        num1_text = self.Pip_oper.get_onlinedevice_gongbei()
        num2_text = self.Pip_oper.get_onlinedevice_jiaodong()
        num3_text = self.Pip_oper.get_onlinedevice_jiangshan()
        num4_text = self.Pip_oper.get_onlinedevice_langu()
        num5_text = self.Pip_oper.get_onlinedevice_anshun()
        num6_text = self.Pip_oper.get_onlinedevice_haikou()
        num7_text = self.Pip_oper.get_onlinedevice_zhongde()
        num8_text = self.Pip_oper.get_onlinedevice_zhilidao()
        num9_text = self.Pip_oper.get_onlinedevice_xiyilu()
        num1_text = int(common_page.ComScenario.retain_numbers(self,num1_text))
        num2_text = int(common_page.ComScenario.retain_numbers(self,num2_text))
        num3_text = int(common_page.ComScenario.retain_numbers(self,num3_text))
        num4_text = int(common_page.ComScenario.retain_numbers(self,num4_text))
        num5_text = int(common_page.ComScenario.retain_numbers(self,num5_text))
        num6_text = int(common_page.ComScenario.retain_numbers(self,num6_text))
        num7_text = int(common_page.ComScenario.retain_numbers(self,num7_text))
        num8_text = int(common_page.ComScenario.retain_numbers(self,num8_text))
        num9_text = int(common_page.ComScenario.retain_numbers(self,num9_text))
        return sum([num9_text, num8_text, num7_text, num6_text, num5_text, num4_text, num3_text, num2_text,
                    num1_text])


    # 离线设备下拉
    def Pip_offlinedevice(self):
        # time.sleep(1)
        self.Pip_oper.click_device_offlinebtn()
    def offline_sum(self):
        num1_text = self.Pip_oper.get_offlinedevice_gongbei()
        num2_text = self.Pip_oper.get_offlinedevice_jiaodong()
        num3_text = self.Pip_oper.get_offlinedevice_jiangshan()
        num4_text = self.Pip_oper.get_offlinedevice_langu()
        num5_text = self.Pip_oper.get_offlinedevice_anshun()
        num6_text = self.Pip_oper.get_offlinedevice_haikou()
        num7_text = self.Pip_oper.get_offlinedevice_zhongde()
        num8_text = self.Pip_oper.get_offlinedevice_zhilidao()
        num9_text = self.Pip_oper.get_offlinedevice_xiyilu()
        num1_text = int(common_page.ComScenario.retain_numbers(self,num1_text))
        num2_text = int(common_page.ComScenario.retain_numbers(self,num2_text))
        num3_text = int(common_page.ComScenario.retain_numbers(self,num3_text))
        num4_text = int(common_page.ComScenario.retain_numbers(self,num4_text))
        num5_text = int(common_page.ComScenario.retain_numbers(self,num5_text))
        num6_text = int(common_page.ComScenario.retain_numbers(self,num6_text))
        num7_text = int(common_page.ComScenario.retain_numbers(self,num7_text))
        num8_text = int(common_page.ComScenario.retain_numbers(self,num8_text))
        num9_text = int(common_page.ComScenario.retain_numbers(self,num9_text))
        return sum([num9_text, num8_text, num7_text, num6_text, num5_text, num4_text, num3_text, num2_text,
                    num1_text])

    def Pip_len(self):
        # time.sleep(1)
        self.Pip_oper.hover_piplen()

    # 设备打点
    def Pip_devicepoint(self):
        # time.sleep(1)
        self.Pip_oper.click_devicepoint_btn()

    #   点击设备打点
    def sikuli_Pip_devicepoint(self):
        return sikuli.click(3, devicepointImage)

    def sikuli_Pip_devicelocation(self):
        return sikuli.Find(3, devicelocationImage)

    def sikuli_Pip_deviceview(self):
        return sikuli.click(3, deviceviewImage)

    def sikuli_Pip_len(self):
        return sikuli.hover(3, piplenImage)

    def sikuli_Pip_road(self):
        return sikuli.hover(3, piproadImage)

    def sikuli_Pip_len1(self):
        return sikuli.exists(3, piplen1Image)

    def sikuli_Pip_road1(self):
        return sikuli.exists(3, piproad1Image)

    def sikuli_Pip_firezone(self):
        return sikuli.click(3, firezoneImage)

    def sikuli_Pip_firezeon1(self):
        return sikuli.Find(3, firezone1Image)

    def sikuli_Pip_Perception(self):
        return sikuli.click(3, PerceptionImage)

    def sikuli_Pip_Perception1(self):
        return sikuli.Find(3, Perception1Image)

    def sikuli_Pip_cabin(self):
        return sikuli.hover(3, cabinImage)

    def sikuli_Pip_cabin1(self):
        return sikuli.exists(3, cabin1Image)

    def sikuli_Pip_linetype(self):
        return sikuli.hover(3, linetypeImage)

    def sikuli_Pip_linetype1(self):
        return sikuli.exists(3, linetype1Image)

    def Pip_deviceview(self):
        self.Pip_oper.click_deviceview_btn()

    def Pip_monitoring_envnum(self):
        mon_tol = self.Pip_oper.get_Pip_monitoring_envtol()
        onmon_tol = self.Pip_oper.get_Pip_monitoring_onenvtol()
        offmon_tol = self.Pip_oper.get_Pip_monitoring_offenvtol()
        mon_sum = int(onmon_tol)+int(offmon_tol)
        return (mon_sum,int(mon_tol))
    def Pip_monitoring_strnum(self):
        mon_tol = self.Pip_oper.get_Pip_monitoring_strtol()
        onmon_tol = self.Pip_oper.get_Pip_monitoring_onstrtol()
        offmon_tol = self.Pip_oper.get_Pip_monitoring_offstrtol()
        mon_sum = int(onmon_tol) + int(offmon_tol)
        return (mon_sum, int(mon_tol))
    def Pip_monitoring_pipenum(self):
        mon_tol = self.Pip_oper.get_Pip_monitoring_pipetol()
        onmon_tol = self.Pip_oper.get_Pip_monitoring_onpipetol()
        offmon_tol = self.Pip_oper.get_Pip_monitoring_offpipetol()
        mon_sum = int(onmon_tol)+int(offmon_tol)
        return (mon_sum,int(mon_tol))
    def Pip_monitoring_firenum(self):
        mon_tol = self.Pip_oper.get_Pip_monitoring_firetol()
        onmon_tol = self.Pip_oper.get_Pip_monitoring_onfiretol()
        offmon_tol = self.Pip_oper.get_Pip_monitoring_offfiretol()
        mon_sum = int(onmon_tol) + int(offmon_tol)
        return (mon_sum, int(mon_tol))

    def Pip_device_tol(self):
        device_tol = self.Pip_oper.get_Pip_device_tol()
        return int(device_tol)

    def warn4_window(self):
        iframe = Base(self.driver).get_element(iframe1)
        self.driver.switch_to.frame(iframe)
        t = self.Pip_oper.get_warn_title()
        n = self.Pip_oper.get_warn_level4()
        v = self.Pip_oper.get_warn_location()
        s = self.Pip_oper.get_warn_text()
        self.Pip_oper.click_close_btn()
        self.driver.switch_to.default_content()  # 切换到最外层
        return all([t,n,v,s])
    def warn3_window(self):
        iframe = Base(self.driver).get_element(iframe1)
        self.driver.switch_to.frame(iframe)
        t = self.Pip_oper.get_warn_title()
        n = self.Pip_oper.get_warn_level3()
        v = self.Pip_oper.get_warn_location()
        s = self.Pip_oper.get_warn_text()
        self.Pip_oper.click_close_btn()
        self.driver.switch_to.default_content()  # 切换到最外层
        return all([t,n,v,s])
    def warn2_window(self):
        iframe = Base(self.driver).get_element(iframe1)
        self.driver.switch_to.frame(iframe)
        t = self.Pip_oper.get_warn_title()
        n = self.Pip_oper.get_warn_level2()
        v = self.Pip_oper.get_warn_location()
        s = self.Pip_oper.get_warn_text()
        self.Pip_oper.click_close_btn()
        self.driver.switch_to.default_content()  # 切换到最外层
        return all([t,n,v,s])
    def warn1_window(self):
        iframe = Base(self.driver).get_element(iframe1)
        self.driver.switch_to.frame(iframe)
        t = self.Pip_oper.get_warn_title()
        n = self.Pip_oper.get_warn_level1()
        v = self.Pip_oper.get_warn_location()
        s = self.Pip_oper.get_warn_text()
        self.Pip_oper.click_close_btn()
        self.driver.switch_to.default_content()  # 切换到最外层
        return all([t,n,v,s])

