from selenium import webdriver  #selenium의 webdriver를 사용
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#PageLoading시 기다리는데에 사용할 모듈
import time

# //*[@id="thumbnail-container"]



def seleniumTest1(req):
    #내부망 이슈로 크롬드라이버 못 받아옴..집에서 해볼것.
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(("https://youtube.com"))

    time.sleep(5)

    search = driver.find_element_by_xpath('//*[@id="search')

    search.send_keys('고양이')
    search.send_keys(Keys.ENTER)
    time.sleep(5)