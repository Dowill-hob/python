from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# 옵션객체
options = Options()
# 옵션객체
options.add_argument("--start-maximized")  # 시작과 동시에 최대화
options.add_argument("--incognito")
# options.add_argument("--headless")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
#  driver.maximize_window() # 시작후 실행

driver.get("https://www.google.com/")
# print(driver.title)
# print(driver.current_url)
# driver.implicitly_wait(5)
# # 무한스크롤페이지 스크롤내리기
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 검색창
search_input = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
print(search_input)

# 검색어
# 속성값 가져오기
# search_input.send_keys("파이썬 코딩연습")
# search_input.send_keys(Keys.ENTER)

# # 검색어 삭제
time.sleep(2)
# search_input.clear()
email_text = driver.find_element(
    By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[1]/a')
href = email_text.get_attribute("href")
print(href)

driver.save_screenshot("./1204/save.png")

input("종료입력: ")
