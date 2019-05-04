# NaverCaptcha

## User Python Installation
  * **selenium**  
    ``` pip install selenium ```

  * **pyperclip**  
    ``` pip install pyperclip ```
  
  * **win32api**  
    ``` pip install pywin32 ```  
    
 외부 라이브러리 설치가 필요합니다.
 
   ## Principle
  ```
  pyperclip.copy(user_input)
  self.driver.find_element_by_xpath(user_xpath).click()
  ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
  ```
  클립보드로 아이디 및 비밀번호를 복사하여 Ctrl+V(Paste) 키 조합을 selenium의 element.sned_keys() 메서드로 전송하면 됩니다.
 
 ## Example
  ```
from sites.naver import Naver
import time

if __name__ == "__main__":
    naver = Naver('your_id', 'your_pw')
    try:
        naver.clipboard_login(naver.ID, naver.PW)
    finally:
        time.sleep(5)
        naver.driver.quit()
  ```
        
  ## How to use
  ```
  self.driver_utils = DriverUtils(self.driver)
  self.driver_utils.clipboard_input('//*[@id="id"]', user_id)
  ```
  DriverUtils 생성자에 Driver 객체를 넣어준 다음에 driver_utils를 이용하여 로그인에 시도할 수 있습니다.
  
  ## 악용 금지
  어뷰저로 사용하는 경우 처벌받을 수 있습니다.  
  본 오픈소스는 개인 사무용으로만 사용해주시기 바랍니다.
