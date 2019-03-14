from selenium import webdriver
from utils.driverutils import DriverUtils
from utils.winkeyboard import WinKeyboard
import time


class Naver(object):
    def __init__(self, user_id, user_pw):
        self.ID = user_id
        self.PW = user_pw

        # Web Driver 옵션 추가
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument("--app=https://google.com") # win32api_login 사용 시 반드시 활성화
        options.add_argument("disable-gpu")
        options.add_argument('window-size=1920x1080')
        options.add_argument("lang=ko_KR")
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36')
        options.add_argument("user-data-dir=\\user-data\\naver\\")
        self.driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
        self.driver.get('https://naver.com')

        self.explicit_wait_time = 1
        self.driver_utils = DriverUtils(self.driver)

        self.keyboard = WinKeyboard()

    def clipboard_login(self, user_id, user_pw):
        self.driver.find_element_by_xpath('//*[@id="account"]/div/a/i').click()
        time.sleep(2)

        self.driver_utils.clipboard_input('//*[@id="id"]', user_id)
        self.driver_utils.clipboard_input('//*[@id="pw"]', user_pw)

        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

    def win32api_login(self, user_id, user_pw):
        self.driver.find_element_by_xpath('//*[@id="account"]/div/a/i').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="id"]').click()
        self.keyboard.press(list(user_id))
        self.driver.find_element_by_xpath('//*[@id="pw"]').click()
        self.keyboard.press(list(user_pw))
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

    def send_keys_login(self, user_id, user_pw):
        self.driver.find_element_by_xpath('//*[@id="account"]/div/a/i').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="id"]').send_keys(user_id)
        self.driver.find_element_by_xpath('//*[@id="pw"]').send_keys(user_pw)
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
