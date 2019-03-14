from sites.naver import Naver
import time

if __name__ == "__main__":
    naver = Naver('', '')
    try:
        naver.clipboard_login(naver.ID, naver.PW)
    finally:
        time.sleep(5)
        naver.driver.quit()
