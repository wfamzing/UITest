'''
登录页
'''
# 页面元素对象层
from selenium.webdriver import ActionChains
from Base.base import Base
import time
from Test.PageObject import sikuli

UrbanLife_btn = "xpath,//*[@id='box']/div[2]"  # 城市生命线元素
Water_btn = "xpath,//*[@id='app']/div/div[3]/div[4]/div[2]"  # 城市生命线元素
Warning_btn = "css,.alarm-total.el-popover__reference"  # 城市生命线元素
Warning_more = "css,.handle-btn.btn"
# Warning_total = "css,.alarm-total.selected>span:nth-child(2)"
alarm_total = "css,.supply-water-monitor-container>div.alarm-list>div>span:nth-child(1)>div>span.cyan"
alarm_sub_count = "css,.value-total"
alarm_sub = "css,.total2 > span:nth-child(2)"
alarm_device_untotal = "css,div.card-body > div > div:nth-child(3) > div.right-info-item.device > div.right-fortop > p.real-time-items.tr > span"
alarm_sub_disposed = "css,.total3 > span:nth-child(2)"
shinan = "css,[aria-hidden='false']>div.popover-content>div.area>div:nth-child(1)>span.value"
shibei = "css,[aria-hidden='false']>div.popover-content>div.area>div:nth-child(2)>span.value"
licang = "css,[aria-hidden='false']>div.popover-content>div.area>div:nth-child(3)>span.value"
laoshan = "css,[aria-hidden='false']>div.popover-content>div.area>div:nth-child(4)>span.value"
chengyang = "css,[aria-hidden='false']>div.popover-content>div.area>div:nth-child(5)>span.value"
huangdao = "css,[aria-hidden='false']>div.popover-content>div.area>div:nth-child(6)>span.value"
jimo = "css,[aria-hidden='false']>div.popover-content>div.area>div:nth-child(7)>span.value"
jiaozhou = "css,[aria-hidden='false']>div.popover-content>div.area>div:nth-child(8)>span.value"
pingdu = "css,[aria-hidden='false']>div.popover-content>div.area>div:nth-child(9)>span.value"
laixi = "css,[aria-hidden='false']>div.popover-content>div.area>div:nth-child(10)>span.value"
alarm_title = "css,#app > div > div.risk-dialog > div > div > div.map-title"
alarm_name = "css,.kv-list>div:nth-child(1)>div.kv-value>span:nth-child(1)"
alarm_value = "css,#app>div>div.risk-dialog>div>div>div.kv-list>div:nth-child(2)>div.kv-value>span:nth-child(1)"
alarm_state = "css,#app>div>div.risk-dialog>div>div>div.kv-list>div:nth-child(3)>div.kv-value>span:nth-child(1)"
alarm_location = "css,#app>div>div.risk-dialog>div>div>div.kv-list>div:nth-child(4)>div.kv-value>span:nth-child(1)"
alarm_time = "css,#app>div>div.risk-dialog>div>div>div.kv-list>div:nth-child(5)>div.kv-value>span:nth-child(1)"
iframe1 = "css,.em-map-div>iframe:nth-child(1)"
alarm_list_time = "css,tr.el-table__row:nth-child(1) > td:nth-child(2) > div:nth-child(1)"
alarm_list_code = "css,tr.el-table__row:nth-child(1) > td:nth-child(3) > div:nth-child(1)"
alarm_list_type = "css,tr.el-table__row:nth-child(1) > td:nth-child(4) > div:nth-child(1)"
alarm_list_indicator = "css,tr.el-table__row:nth-child(1) > td:nth-child(5) > div:nth-child(1)"
alarm_list_value = "css,tr.el-table__row:nth-child(1) > td:nth-child(6) > div:nth-child(1)"
alarm_list_from = "css,tr.el-table__row:nth-child(1) > td:nth-child(7) > div:nth-child(1)"
alarm_list_state = "css,tr.el-table__row:nth-child(1) > td:nth-child(8) > div:nth-child(1)"
alarm_list_do = "css,tr.el-table__row:nth-child(1) > td:nth-child(9) > div:nth-child(1) > button:nth-child(1) > span:nth-child(2)"
warn_total = "css,div.alarm-total.el-popover__reference > span:nth-child(2)"
warn_totalbtn = "css,#app > div > div.frontend > div > div.supply-water-monitor-container > div.alarm-list > div > span:nth-child(2) > div"
warn_num = "css,[aria-hidden='false'] > div.popover-content.warning > div.total.cursor > span.value"
warn1_num = "css,[aria-hidden='false'] > div.popover-content.warning > div.warning > div.warning-item.level1 > span.value.level1"
warn2_num = "css,[aria-hidden='false'] > div.popover-content.warning > div.warning > div.warning-item.level2 > span.value.level2"
warn3_num = "css,[aria-hidden='false'] > div.popover-content.warning > div.warning > div.warning-item.level3 > span.value.level3"
warn4_num = "css,[aria-hidden='false'] > div.popover-content.warning > div.warning > div.warning-item.level4 > span.value.level4"
close_btn = "class,close-btn"

alarmsImage = r"D:\wf\EmergUItest\Common\image\water\alarmlist.png"

class PipPage(object):
    def __init__(self, browser):
        # 私有方法
        self.driver = browser
        # self.iframe = Base(self.driver).get_element(iframe_1)# 根据需要填入index，这里定位HTML里的第一个

    def find_UrbanLife(self):
        # 查找城市生命线
        ele = Base(self.driver).get_element(UrbanLife_btn)
        return ele

    def find_Pip(self):
        # 查找供水专项
        ele = Base(self.driver).get_element(Water_btn)
        return ele

    def find_Alarm_btn(self):
        # 查找预警总数按钮
        # ele = self.driver.find_element_by_id('login-submit')
        ele = Base(self.driver).get_element(alarm_total)
        return ele

    def find_Alarm_undevice(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(alarm_device_untotal)
        return ele

    def find_Alarm_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(alarm_sub)
        return ele
    def find_Alarm_subcount(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(alarm_sub_count)
        return ele
    def find_Alarm_subdisposed(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(alarm_sub_disposed)
        return ele

    def find_shinan_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(shinan)
        return ele
    def find_shibei_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(shibei)
        return ele
    def find_licang_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(licang)
        return ele
    def find_laoshan_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(laoshan)
        return ele
    def find_chengyang_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(chengyang)
        return ele
    def find_huangdao_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(huangdao)
        return ele
    def find_jimo_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(jimo)
        return ele
    def find_jiaozhou_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(jiaozhou)
        return ele
    def find_pingdu_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(pingdu)
        return ele
    def find_laixi_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(laixi)
        return ele

    def find_Alarm_title(self):
        ele = Base(self.driver).get_element(alarm_title)
        return ele
    def find_Alarm_name(self):
        ele = Base(self.driver).get_element(alarm_name)
        return ele
    def find_Alarm_value(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(alarm_value)
        # self.driver.switch_to.default_content()  # 切换到最外层
        return ele
    def find_Alarm_state(self):
        ele = Base(self.driver).get_element(alarm_state)
        # self.driver.switch_to.default_content()  # 切换到最外层
        return ele
    def find_Alarm_location(self):
        ele = Base(self.driver).get_element(alarm_location)
        # self.driver.switch_to.default_content()  # 切换到最外层
        return ele
    def find_Alarm_time(self):
        ele = Base(self.driver).get_element(alarm_time)
        return ele

    def find_Alarmlist_time(self):
        ele = Base(self.driver).get_element(alarm_list_time)
        return ele
    def find_Alarmlist_code(self):
        ele = Base(self.driver).get_element(alarm_list_code)
        return ele
    def find_Alarmlist_type(self):
        ele = Base(self.driver).get_element(alarm_list_type)
        return ele
    def find_Alarmlist_indicator(self):
        ele = Base(self.driver).get_element(alarm_list_indicator)
        return ele
    def find_Alarmlist_value(self):
        ele = Base(self.driver).get_element(alarm_list_value)
        return ele
    def find_Alarmlist_from(self):
        ele = Base(self.driver).get_element(alarm_list_from)
        return ele
    def find_Alarmlist_state(self):
        ele = Base(self.driver).get_element(alarm_list_indicator)
        return ele
    def find_Alarmlist_do(self):
        ele = Base(self.driver).get_element(alarm_list_do)
        return ele

    def find_Warn_total(self):
        ele = Base(self.driver).get_element(warn_total)
        return ele
    def find_Warn_num(self):
        ele = Base(self.driver).get_element(warn_num)
        return ele
    def find_Warn1_num(self):
        ele = Base(self.driver).get_element(warn1_num)
        return ele
    def find_Warn2_num(self):
        ele = Base(self.driver).get_element(warn2_num)
        return ele
    def find_Warn3_num(self):
        ele = Base(self.driver).get_element(warn3_num)
        return ele
    def find_Warn4_num(self):
        ele = Base(self.driver).get_element(warn4_num)
        return ele

    def find_close_btn(self):
        ele = Base(self.driver).get_element(close_btn)
        return ele

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

    def click_Alarm_btn(self):
        ele = self.Pip_page.find_Alarm_btn()
        ActionChains(self.driver).click(ele).perform()

    def click_Alarm_sub(self):
        ele = self.Pip_page.find_Alarm_sub()
        ActionChains(self.driver).click(ele).perform()

    def click_Warn1_btn(self):
        ele = self.Pip_page.find_Pip_warn1_btn()
        ActionChains(self.driver).click(ele).perform()

    def get_Alarm_tol(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Alarm_btn().text

    def get_Alarm_undevice(self):
        # 返回报警设备统计未处置报警设备
        return self.Pip_page.find_Alarm_undevice().text

    def get_Alarm_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Alarm_sub().text
    def get_Alarm_subcount(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Alarm_subcount().text
    def get_Alarm_subdisposed(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Alarm_subdisposed().text
    def get_shinan_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_shinan_sub().text
    def get_shibei_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_shibei_sub().text
    def get_laoshan_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_laoshan_sub().text
    def get_licang_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_licang_sub().text
    def get_chengyang_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_chengyang_sub().text
    def get_huangdao_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_huangdao_sub().text
    def get_jimo_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_jimo_sub().text
    def get_jiaozhou_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_jiaozhou_sub().text
    def get_pingdu_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_pingdu_sub().text
    def get_laixi_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_laixi_sub().text

    def get_Alarm_title(self):
        return self.Pip_page.find_Alarm_title().text
    def get_Alarm_name(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Alarm_name().text
    def get_Alarm_value(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Alarm_value().text
    def get_Alarm_state(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Alarm_state().text
    def get_Alarm_location(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Alarm_location().text
    def get_Alarm_time(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Alarm_time().text

    def get_Alarmlist_time(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Alarmlist_time().text
    def get_Alarmlist_code(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Alarmlist_code().text
    def get_Alarmlist_type(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Alarmlist_type().text
    def get_Alarmlist_indicator(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Alarmlist_indicator().text
    def get_Alarmlist_value(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Alarmlist_value().text
    def get_Alarmlist_from(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Alarmlist_from().text
    def get_Alarmlist_state(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Alarmlist_state().text
    def click_Alarmlist_do(self):
        ele = self.Pip_page.find_Alarmlist_do()
        ActionChains(self.driver).click(ele).perform()

    def click_Warn_total(self):
        ele = self.Pip_page.find_Warn_total()
        ActionChains(self.driver).click(ele).perform()
    def get_Warn_total(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Warn_total().text
    def click_Warn_num(self):
        # 返回登录后的用户名元素的文字
        ele = self.Pip_page.find_Warn_num()
        ActionChains(self.driver).click(ele).perform()
    def get_Warn_num(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Warn_num().text
    def get_Warn1_num(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Warn1_num().text
    def get_Warn2_num(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Warn2_num().text
    def get_Warn3_num(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Warn3_num().text
    def get_Warn4_num(self):
        # 返回登录后的用户名元素的文字
        return self.Pip_page.find_Warn4_num().text
    def click_Warn1_num(self):
        # 返回登录后的用户名元素的文字
        ele = self.Pip_page.find_Warn1_num()
        ActionChains(self.driver).click(ele).perform()
    def click_Warn2_num(self):
        # 返回登录后的用户名元素的文字
        ele = self.Pip_page.find_Warn2_num()
        ActionChains(self.driver).click(ele).perform()
    def click_Warn3_num(self):
        # 返回登录后的用户名元素的文字
        ele = self.Pip_page.find_Warn3_num()
        ActionChains(self.driver).click(ele).perform()
    def click_Warn4_num(self):
        # 返回登录后的用户名元素的文字
        ele = self.Pip_page.find_Warn4_num()
        ActionChains(self.driver).click(ele).perform()

    def click_close_btn(self):
        # 返回登录后的用户名元素的文字
        ele = self.Pip_page.find_close_btn()
        ActionChains(self.driver).click(ele).perform()


# 页面业务场景层
class PipScenario(object):
    def __init__(self, browser):
        # 私有方法：调用页面元素操作
        self.Pip_oper = PipOper(browser)
        self.driver = browser

    def water(self):
        # 定义一个登录场景，用到了3个操作
        time.sleep(1)
        self.Pip_oper.click_UrbanLife_btn()
        time.sleep(1)
        self.Pip_oper.click_Pip_btn()

    def water_alarm(self):
        time.sleep(1)
        self.Pip_oper.click_Alarm_btn()

    def water_alarm_sub(self):
        # time.sleep(1)
        self.Pip_oper.click_Alarm_sub()

    def alarm_sum(self):
        num1_text = int(self.Pip_oper.get_shinan_sub())
        num2_text = int(self.Pip_oper.get_shibei_sub())
        num3_text = int(self.Pip_oper.get_licang_sub())
        num4_text = int(self.Pip_oper.get_laoshan_sub())
        num5_text = int(self.Pip_oper.get_chengyang_sub())
        num6_text = int(self.Pip_oper.get_huangdao_sub())
        num7_text = int(self.Pip_oper.get_jimo_sub())
        num8_text = int(self.Pip_oper.get_jiaozhou_sub())
        num9_text = int(self.Pip_oper.get_pingdu_sub())
        num10_text = int(self.Pip_oper.get_laixi_sub())
        return sum([num10_text,num9_text,num8_text,num7_text,num6_text,num5_text,num4_text,num3_text,num2_text,num1_text])

    def sikuli_alarm_list(self):
        return sikuli.Find(3,alarmsImage)

    def alarm_window(self):
        iframe = Base(self.driver).get_element(iframe1)
        self.driver.switch_to.frame(iframe)
        t = self.Pip_oper.get_Alarm_title()
        n = self.Pip_oper.get_Alarm_name()
        v = self.Pip_oper.get_Alarm_value()
        s = self.Pip_oper.get_Alarm_state()
        l = self.Pip_oper.get_Alarm_location()
        tt = self.Pip_oper.get_Alarm_time()
        self.Pip_oper.click_close_btn()
        self.driver.switch_to.default_content()  # 切换到最外层
        return all([t,n,v,s,l,tt])

    def alarm_list_value(self):
        t = self.Pip_oper.get_Alarmlist_time()
        c = self.Pip_oper.get_Alarmlist_code()
        ty = self.Pip_oper.get_Alarmlist_type()
        i = self.Pip_oper.get_Alarmlist_indicator()
        v = self.Pip_oper.get_Alarmlist_value()
        f = self.Pip_oper.get_Alarmlist_from()
        s = self.Pip_oper.get_Alarmlist_state()
        return all([t,c,ty,i,v,f,s])

    def alarm_list_do(self):
        self.Pip_oper.click_Alarmlist_do()

    def warn_total(self):
        return self.Pip_oper.get_Warn_total()
    def click_warn_total(self):
        self.Pip_oper.click_Warn_total()

    def warn_num(self):
        return self.Pip_oper.get_Warn_num()
    def click_warn_num(self):
        self.Pip_oper.click_Warn_num()
    def click_warn1_num(self):
        self.Pip_oper.click_Warn1_num()
    def click_warn2_num(self):
        self.Pip_oper.click_Warn2_num()
    def click_warn3_num(self):
        self.Pip_oper.click_Warn3_num()
    def click_warn4_num(self):
        self.Pip_oper.click_Warn4_num()

    def warn_sum(self):
        num1_text = int(self.Pip_oper.get_Warn1_num())
        num2_text = int(self.Pip_oper.get_Warn2_num())
        num3_text = int(self.Pip_oper.get_Warn3_num())
        num4_text = int(self.Pip_oper.get_Warn4_num())
        return sum([num4_text,num3_text,num2_text,num1_text])
