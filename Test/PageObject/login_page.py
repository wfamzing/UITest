'''
登录页
'''
# 页面元素对象层
from selenium.webdriver import ActionChains
from Test.PageObject import ocr
from Base.base import Base
import time
from PIL import Image
from retrying import retry

loginname_input = "xpath,//input[@type='text']" #登录名元素
loginpwd_input = "xpath,//input[@type='password']" #登陆密码元素
login_btn = "css,.el-button.el-button--primary" #登录按钮
login_alert = "class,el-message__content" #弹窗提示
login_faild = "css,body>div.el-message.el-message--warning"
login_code = "xpath,//*[@id='app']/div/form/div[4]/div/div[1]/img"
logincode_input = "name,code"

class LoginPage(object):
    def __init__(self, browser):
        # 私有方法
        self.driver = browser

    def find_username(self):
        # 查找并返回用户名输入框元素
        # ele = self.driver.find_element_by_id('username')
        # ele = self.driver.find_element_by_name('username')
        ele = Base(self.driver).get_element(loginname_input)
        return ele

    def find_password(self):
        # 查找并返回密码输入框元素
        # ele = self.driver.find_element_by_id('password')
        ele = Base(self.driver).get_element(loginpwd_input)
        return ele

    def find_login_btn(self):
        # 查找并返回登录按钮元素
        # ele = self.driver.find_element_by_id('login-submit')
        ele = Base(self.driver).get_element(login_btn)
        return ele

    def find_login_alert(self):
        # 查找并返回登录后的弹窗提示元素
        # ele = self.driver.find_element_by_id('loggedas')
        ele = Base(self.driver).get_element(login_alert)
        return ele

    def find_login_failed_info(self):
        # 查找并返回登录失败后的提示信息元素
        # ele = self.driver.find_element_by_id('flash_error')
        ele = Base(self.driver).get_element(login_faild)
        return ele

    def find_login_code(self):
        # 查找并返回登录验证码元素
        ele = Base(self.driver).get_element(login_code)
        return ele

    def find_verification_code(self):
        # 查找并返回登录验证码输入框元素
        ele = Base(self.driver).get_element(logincode_input)
        return ele

# 页面元素操作层
class LoginOper(object):
    def __init__(self, browser):
        # 私有方法，调用元素定位的类
        self.login_page = LoginPage(browser)
        self.driver = browser

    def input_username(self, username):
        # 对用户名输入框做clear和send_keys操作
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(username)

    def input_password(self, password):
        # 对密码输入框做clear和send_keys操作
        self.login_page.find_password().clear()
        self.login_page.find_password().send_keys(password)

    # def click_login_btn(self):
    #     # 对登录按钮做点击操作
    #     self.login_page.find_login_btn().click()

    def click_login_btn(self):
        ele = self.login_page.find_login_btn()
        ActionChains(self.driver).click(ele).perform()

    def get_login_alert(self):
        time.sleep(1)
        # self.driver.implicitly_wait(3)
        # 返回登录后的用户名元素的文字
        return self.login_page.find_login_alert().text

    def get_login_failed_info(self):
        # 返回登录失败后提示信息的文字
        return self.login_page.find_login_failed_info().text

    def get_login_code(self):
        # 返回登录失败后提示信息的文字
        return self.login_page.find_login_code().get_attribute('src')

    def click_login_code(self):
        ele = self.login_page.find_login_code()
        ActionChains(self.driver).click(ele).perform()

    def input_logincode(self,code):
        # 对密码输入框做clear和send_keys操作
        self.login_page.find_verification_code().clear()
        # code = ocr.ocrCaptcha()
        # length = len(code)
        self.login_page.find_verification_code().send_keys(code)

    def get_verificationImage(self):
        self.driver.save_screenshot('login.png')

        # 选择验证码图片的元素
        yzm_btn = self.login_page.find_login_code()
        # 获取图片元素的位置
        loc = yzm_btn.location
        # 获取图片的宽高
        size = yzm_btn.size
        # 获取验证码上下左右的位置    缩放布局是100% 则对应*1.0
        left = loc['x'] * 1.0
        top = loc['y'] * 1.0
        right = (loc['x'] + size['width']) * 1.0
        botom = (loc['y'] + size['height']) * 1.0
        val = (left, top, right, botom)
        # 打开网页截图
        login_pic = Image.open('login.png')
        # 通过上下左右的值，去截取验证码
        yzm_pic = login_pic.crop(val)
        yzm_pic.save('code.png')

    # def input_verfication_code(self, fixed_value=123456): # 万能验证码
    #     self.login_page.find_verification_code().send_keys(fixed_value)

# 页面业务场景层
class LoginScenario(object):
    def __init__(self, browser):
        # 私有方法：调用页面元素操作
        self.login_oper = LoginOper(browser)

    @retry(stop_max_attempt_number=5)
    def login(self, username, password):
        # 定义一个登录场景，用到了3个操作
        self.login_oper.input_username(username)
        self.login_oper.input_password(password)
        self.login_oper.get_verificationImage()
        code = ocr.ocrCaptcha()
        length = len(code)
        self.login_oper.input_logincode(code)
        if length < 4:
            self.login_oper.click_login_code()
            time.sleep(1)
            raise
        self.login_oper.click_login_btn()
        text = self.login_oper.get_login_alert()
        if text != '登录成功':
            time.sleep(1)
            raise

    # def tryAgain(self):
    #     self.login_oper.click_login_code()
    #     self.login_oper.get_verificationImage()
    #     self.login_oper.input_logincode()
    #     self.login_oper.click_login_btn()

