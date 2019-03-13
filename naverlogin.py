from sites.naver import Naver
import time

if __name__ == "__main__":
    naver = Naver('your_id', 'your_pw')
    try:
        naver.security_login(naver.ID, naver.PW)
    finally:
        time.sleep(5)
        naver.driver.quit()
