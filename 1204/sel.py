from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--start-maximized")  # 시작과 동시에 최대화
options.add_argument("--incognito")  # 시크릿 모드에서 동작작

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/")
search_input = driver.find_element(By.ID, "APjFqb")  # 요소 선택

search_input.send_keys("강아지")  # 검색어 입력
search_input.send_keys(Keys.ENTER)

input("닫기 입력: ")
