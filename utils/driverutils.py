from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time


class DriverUtils(object):
    def __init__(self, driver):
        self.driver = driver

    def focus_frame(self, explicit_wait_time, element):
        # 프레임이 생성되기 전 까지 기다렸다가 생성이 완료 되면 프레임을 옮김
        WebDriverWait(self.driver, explicit_wait_time).until(EC.frame_to_be_available_and_switch_to_it(element))

    def clipboard_input(self, user_xpath, user_input):
        temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장

        pyperclip.copy(user_input)
        self.driver.find_element_by_xpath(user_xpath).click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
        time.sleep(1)
