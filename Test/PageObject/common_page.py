'''
登录页
'''
# 页面元素对象层
from selenium.webdriver import ActionChains
from Base.base import Base
import time
from Test.PageObject import sikuli

map = "css,#app>div>div.frontend>div>div.header-nav>div.map-tool.expanded>div>div.expanded>div:nth-child(1)>img"
map_btn = "css,#app>div>div.frontend>div>div.header-nav>div.map-tool.expanded>div>div.expanded>div:nth-child(1)"
tool_btn = "css,#app>div>div.frontend>div>div.header-nav>div.map-tool.expanded>div>div.map-switch-btn.active>div"
sub_title = "css,#app>div>div.frontend>div>div.sub-title"
loginpwd_input = "xpath,//input[@type='password']" #登陆密码元素
login_btn = "css,.el-button.el-button--primary" #登录按钮
login_alert = "class,el-message__content" #弹窗提示
alarm_more = "css,div.bottom-total:nth-child(3) > div:nth-child(3)"
alarm_list_title = "css,div.el-dialog__wrapper:nth-child(13) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)"
alarm_list_total = "css,.el-pagination__total"
alarm_list_close = "css,[aria-label='报警列表'] > div.el-dialog__header > button"
warn_list_close = "css,[aria-label='平台预警列表'] > div.el-dialog__header > button"
list_close = "class,close-btn"
warn_more = "css,div.total:nth-child(4) > div:nth-child(3)"
warn_list_title = "css,[aria-label='平台预警列表'] > div.el-dialog__header > span"
iframe1 = "css,.em-map-div>iframe:nth-child(1)"
device_total = "css,.alarm-box > span:nth-child(3) > div:nth-child(2) > span:nth-child(2)"
device_online_total= "css,div.online:nth-child(2) > span:nth-child(2)"
device_offline_total = "css,.alarm-box > span:nth-child(5) > div:nth-child(2) > span:nth-child(2)"
device_num = "css,[aria-hidden='false']>div.popover-content.warning>div.total.cursor>span.value"
device_onlinenum = "css,[aria-hidden='false'] > div.popover-content.warning > div.total.online.cursor > span.value"
device_offlinenum = "css,[aria-hidden='false'] > div.popover-content.warning > div.total.offline.cursor > span.value"
shinan_device = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)"
shibei_device = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)"
licang_device = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > span:nth-child(2)"
laoshan_device = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > span:nth-child(2)"
chengyang_device = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(5) > div:nth-child(1) > span:nth-child(2)"
huangdao_device = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(6) > div:nth-child(1) > span:nth-child(2)"
jimo_device = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(7) > div:nth-child(1) > span:nth-child(2)"
jiaozhou_device = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(8) > div:nth-child(1) > span:nth-child(2)"
pingdu_device = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(9) > div:nth-child(1) > span:nth-child(2)"
laixi_device = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(10) > div:nth-child(1) > span:nth-child(2)"
shinan_device1 = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)"
shibei_device1 = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(2) > span:nth-child(2)"
licang_device1 = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(3) > span:nth-child(2)"
laoshan_device1 = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(4) > span:nth-child(2)"
chengyang_device1 = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(5) > span:nth-child(2)"
huangdao_device1 = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(6) > span:nth-child(2)"
jimo_device1 = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(7) > span:nth-child(2)"
jiaozhou_device1 = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(8) > span:nth-child(2)"
pingdu_device1 = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(9) > span:nth-child(2)"
laixi_device1 = "css,[aria-hidden='false'] > div.popover-content.warning > div:nth-child(2) > div:nth-child(10) > span:nth-child(2)"

alarmpointImage = r"D:\wf\EmergUItest\Common\image\alarm.png"
alarmviewImage = r"D:\wf\EmergUItest\Common\image\alarmview.png"
warnpointImage = r"D:\wf\EmergUItest\Common\image\Warning.png"
warnpointImage_4 = r"D:\wf\EmergUItest\Common\image\Warning_4.png"
warnpointImage_3 = r"D:\wf\EmergUItest\Common\image\Warning_3.png"
warnpointImage_2 = r"D:\wf\EmergUItest\Common\image\Warning_2.png"
warnpointImage_1 = r"D:\wf\EmergUItest\Common\image\Warning_1.png"
titleImage = r"D:\wf\EmergUItest\Common\image\EmergTitle.png"
closeImage = r"D:\wf\EmergUItest\Common\image\Close.png"
closeImage_1 = r"D:\wf\EmergUItest\Common\image\Close1.png"

class comPage(object):
    def __init__(self, browser):
        # 私有方法
        self.driver = browser

    def find_map(self):
        # 查找并返回用户名输入框元素
        ele = Base(self.driver).get_element(map).get_attribute('alt')
        return ele

    def find_map_btn(self):
        ele = Base(self.driver).get_element(map_btn)
        return ele

    def find_sub_title(self):
        ele = Base(self.driver).get_element(sub_title)
        return ele

    def find_alarm_more(self):
        ele = Base(self.driver).get_element(alarm_more)
        return ele

    def find_alarmlist_title(self):
        ele = Base(self.driver).get_element(alarm_list_title)
        return ele

    def find_alarmlist_total(self):
        ele = Base(self.driver).get_element(alarm_list_total)
        return ele

    def find_list_close(self):
        ele = Base(self.driver).get_element(list_close)
        return ele

    def find_alarmlist_close(self):
        ele = Base(self.driver).get_element(alarm_list_close)
        return ele
    def find_warnlist_close(self):
        ele = Base(self.driver).get_element(warn_list_close)
        return ele

    def find_warn_more(self):
        ele = Base(self.driver).get_element(warn_more)
        return ele
    def find_warnlist_title(self):
        ele = Base(self.driver).get_element(warn_list_title)
        return ele

    def find_device_total(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(device_total)
        return ele
    def find_device_num(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(device_num)
        return ele
    def find_device_ontotal(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(device_online_total)
        return ele
    def find_device_onnum(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(device_onlinenum)
        return ele
    def find_device_offtotal(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(device_offline_total)
        return ele
    def find_device_offnum(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(device_offlinenum)
        return ele
    def find_shinan_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(shinan_device)
        return ele
    def find_shibei_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(shibei_device)
        return ele
    def find_licang_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(licang_device)
        return ele
    def find_laoshan_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(laoshan_device)
        return ele
    def find_chengyang_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(chengyang_device)
        return ele
    def find_huangdao_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(huangdao_device)
        return ele
    def find_jimo_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(jimo_device)
        return ele
    def find_jiaozhou_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(jiaozhou_device)
        return ele
    def find_pingdu_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(pingdu_device)
        return ele
    def find_laixi_sub(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(laixi_device)
        return ele

    def find_shinan_sub1(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(shinan_device1)
        return ele
    def find_shibei_sub1(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(shibei_device1)
        return ele
    def find_licang_sub1(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(licang_device1)
        return ele
    def find_laoshan_sub1(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(laoshan_device1)
        return ele
    def find_chengyang_sub1(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(chengyang_device1)
        return ele
    def find_huangdao_sub1(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(huangdao_device1)
        return ele
    def find_jimo_sub1(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(jimo_device1)
        return ele
    def find_jiaozhou_sub1(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(jiaozhou_device1)
        return ele
    def find_pingdu_sub1(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(pingdu_device1)
        return ele
    def find_laixi_sub1(self):
        # 查找预警总数按钮
        ele = Base(self.driver).get_element(laixi_device1)
        return ele

    # def find_verification_code(self):
    #     ele = self.driver.find_element_by_id('aaa')
    #     return ele

# 页面元素操作层
class ComOper(object):
    def __init__(self, browser):
        # 私有方法，调用元素定位的类
        self.Com_page = comPage(browser)
        self.driver = browser


    def get_map_text(self):
        time.sleep(1)
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_map()

    def click_map_btn(self):
        ele = self.Com_page.find_map_btn()
        ActionChains(self.driver).click(ele).perform()

    def click_sub_title(self):
        ele = self.Com_page.find_sub_title()
        ActionChains(self.driver).click(ele).perform()

    def move_sub_title(self):
        ele = self.Com_page.find_sub_title()
        ActionChains(self.driver).move_by_offset(10,10).perform()

    def click_alarm_more(self):
        ele = self.Com_page.find_alarm_more()
        ActionChains(self.driver).click(ele).perform()

    def get_alarmlist_title(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_alarmlist_title().text
    def get_alarmlist_total(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_alarmlist_total().text

    def click_list_close(self):
        ele = self.Com_page.find_list_close()
        ActionChains(self.driver).click(ele).perform()

    def click_alarmlist_close(self):
        ele = self.Com_page.find_alarmlist_close()
        ActionChains(self.driver).click(ele).perform()
    def click_warnlist_close(self):
        ele = self.Com_page.find_warnlist_close()
        ActionChains(self.driver).click(ele).perform()

    def click_warn_more(self):
        ele = self.Com_page.find_warn_more()
        ActionChains(self.driver).click(ele).perform()

    def get_warnlist_title(self):
        return self.Com_page.find_warnlist_title().text

    def click_device_total(self):
        ele = self.Com_page.find_device_total()
        ActionChains(self.driver).click(ele).perform()
    def click_device_ontotal(self):
        ele = self.Com_page.find_device_ontotal()
        ActionChains(self.driver).click(ele).perform()
    def click_device_offtotal(self):
        ele = self.Com_page.find_device_offtotal()
        ActionChains(self.driver).click(ele).perform()
    def get_device_total(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_device_total().text
    def get_device_num(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_device_num().text
    def get_device_ontotal(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_device_ontotal().text
    def get_device_onnum(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_device_onnum().text
    def get_device_offtotal(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_device_offtotal().text
    def get_device_offnum(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_device_offnum().text
    def get_shinan_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_shinan_sub().text
    def get_shibei_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_shibei_sub().text
    def get_laoshan_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_laoshan_sub().text
    def get_licang_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_licang_sub().text
    def get_chengyang_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_chengyang_sub().text
    def get_huangdao_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_huangdao_sub().text
    def get_jimo_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_jimo_sub().text
    def get_jiaozhou_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_jiaozhou_sub().text
    def get_pingdu_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_pingdu_sub().text
    def get_laixi_sub(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_laixi_sub().text

    def get_shinan_sub1(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_shinan_sub1().text
    def get_shibei_sub1(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_shibei_sub1().text
    def get_laoshan_sub1(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_laoshan_sub1().text
    def get_licang_sub1(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_licang_sub1().text
    def get_chengyang_sub1(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_chengyang_sub1().text
    def get_huangdao_sub1(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_huangdao_sub1().text
    def get_jimo_sub1(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_jimo_sub1().text
    def get_jiaozhou_sub1(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_jiaozhou_sub1().text
    def get_pingdu_sub1(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_pingdu_sub1().text
    def get_laixi_sub1(self):
        # 返回登录后的用户名元素的文字
        return self.Com_page.find_laixi_sub1().text


# 页面业务场景层
class ComScenario(object):
    def __init__(self, browser):
        # 私有方法：调用页面元素操作
        self.Com_oper = ComOper(browser)
        self.driver = browser

    def map_switch(self):
        # 定义一个登录场景，用到了3个操作
        self.Com_oper.click_map_btn()

    def sub_title_click(self):
        # 点击专项标题
        self.Com_oper.click_sub_title()

    def sub_more_click(self):
        # 点击专项标题
        self.Com_oper.click_alarm_more()

    def list_close_click(self):
        iframe = Base(self.driver).get_element(iframe1)
        self.driver.switch_to.frame(iframe)
        self.Com_oper.click_list_close()
        self.driver.switch_to.default_content()  # 切换到最外层

    def alarmlist_close_click(self):
        self.Com_oper.click_alarmlist_close()
    def warnlist_close_click(self):
        self.Com_oper.click_warnlist_close()

    def alarm_list_title(self):
        # 点击专项标题
        return self.Com_oper.get_alarmlist_title()

    def alarm_list_total(self):
        # 点击专项标题
        return self.Com_oper.get_alarmlist_total()

    def sikuli_title_hover(self):
        # 点击专项标题
        return sikuli.hover(5,titleImage)

    def sikuli_alarm_click(self):
        return sikuli.click(3, alarmpointImage)

    def sikuli_alarmview_find(self):
        return sikuli.exists(3, alarmviewImage)

    def sikuli_warn_click(self):
        return sikuli.click(5,warnpointImage)

    def sikuli_warn1_click(self):
        return sikuli.click(5,warnpointImage_1)

    def sikuli_warn2_click(self):
        return sikuli.click(5,warnpointImage_2)

    def sikuli_warn3_click(self):
        return sikuli.click(5,warnpointImage_3)

    def sikuli_warn4_click(self):
        return sikuli.click(5,warnpointImage_4)

    def sikuli_close(self):
        return sikuli.click(3,closeImage)

    def sikuli_close1(self):
        return sikuli.click(3,closeImage_1)

    def retain_numbers(self,string):
        result = ''  # 初始化结果字符串
        for char in string:  # 遍历字符串的每个字符
            if char.isdigit():  # 判断字符是否为数字
                result += char  # 如果是数字，则将其添加到结果字符串中
        return result  # 返回结果字符串

    def warn_more_click(self):
        # 点击专项标题
        self.Com_oper.click_warn_more()
    def warn_list_title(self):
        # 点击专项标题
        return self.Com_oper.get_warnlist_title()

    def device_total_click(self):
        # 点击专项标题
        self.Com_oper.click_device_total()
    def device_ontotal_click(self):
        # 点击专项标题
        self.Com_oper.click_device_ontotal()
    def device_offtotal_click(self):
        # 点击专项标题
        self.Com_oper.click_device_offtotal()

    def device_sum(self):
        num1_text = self.Com_oper.get_shinan_sub()
        num2_text = self.Com_oper.get_shibei_sub()
        num3_text = self.Com_oper.get_licang_sub()
        num4_text = self.Com_oper.get_laoshan_sub()
        num5_text = self.Com_oper.get_chengyang_sub()
        num6_text = self.Com_oper.get_huangdao_sub()
        num7_text = self.Com_oper.get_jimo_sub()
        num8_text = self.Com_oper.get_jiaozhou_sub()
        num9_text = self.Com_oper.get_pingdu_sub()
        num10_text = self.Com_oper.get_laixi_sub()
        num1_text = int(self.retain_numbers(num1_text))
        num2_text = int(self.retain_numbers(num2_text))
        num3_text = int(self.retain_numbers(num3_text))
        num4_text = int(self.retain_numbers(num4_text))
        num5_text = int(self.retain_numbers(num5_text))
        num6_text = int(self.retain_numbers(num6_text))
        num7_text = int(self.retain_numbers(num7_text))
        num8_text = int(self.retain_numbers(num8_text))
        num9_text = int(self.retain_numbers(num9_text))
        num10_text = int(self.retain_numbers(num10_text))
        return sum([num10_text, num9_text, num8_text, num7_text, num6_text, num5_text, num4_text, num3_text, num2_text,
                    num1_text])

    def device_sum1(self):
        num1_text = self.Com_oper.get_shinan_sub1()
        num2_text = self.Com_oper.get_shibei_sub1()
        num3_text = self.Com_oper.get_licang_sub1()
        num4_text = self.Com_oper.get_laoshan_sub1()
        num5_text = self.Com_oper.get_chengyang_sub1()
        num6_text = self.Com_oper.get_huangdao_sub1()
        num7_text = self.Com_oper.get_jimo_sub1()
        num8_text = self.Com_oper.get_jiaozhou_sub1()
        num9_text = self.Com_oper.get_pingdu_sub1()
        num10_text = self.Com_oper.get_laixi_sub1()
        num1_text = int(self.retain_numbers(num1_text))
        num2_text = int(self.retain_numbers(num2_text))
        num3_text = int(self.retain_numbers(num3_text))
        num4_text = int(self.retain_numbers(num4_text))
        num5_text = int(self.retain_numbers(num5_text))
        num6_text = int(self.retain_numbers(num6_text))
        num7_text = int(self.retain_numbers(num7_text))
        num8_text = int(self.retain_numbers(num8_text))
        num9_text = int(self.retain_numbers(num9_text))
        num10_text = int(self.retain_numbers(num10_text))
        return sum([num10_text, num9_text, num8_text, num7_text, num6_text, num5_text, num4_text, num3_text, num2_text,
                    num1_text])

