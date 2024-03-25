
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# ChromeOptions 객체 생성
options = Options()
#user_data = r"C:\Users\B201812058\AppData\Local\Google\Chrome\User Data"
options.add_experimental_option("detach", True)
#options.add_argument(f"user-data-dir={user_data}")

# 웹 드라이버 시작
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)
wait = WebDriverWait(driver, 50)
# 로그인 페이지로 이동
driver.get('https://ceo-portal.yogiyo.co.kr/login/')

wait = WebDriverWait(driver, 50)

# 로그인 정보 입력
username = driver.find_element(By.NAME, 'username')  # 예시: 로그인 페이지의 사용자 이름 입력란 ID
password = driver.find_element(By.NAME, 'password')  # 예시: 로그인 페이지의 비밀번호 입력란 ID
login_button = driver.find_element(By.CLASS_NAME, 'Button__StyleButton-sc-2z9iin-0')  # 예시: 로그인 페이지의 로그인 버튼 ID

username.send_keys('jiwon.chaA')  # 여기에 사용자 이름 입력
password.send_keys('terminal2!')  # 여기에 비밀번호 입력
login_button.click()

driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/ul/li[4]').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/ul/li[4]/ul').click()
#driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[1]/form/div[1]/div[2]/div[1]/select').click()
select_element = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[1]/form/div[1]/div[2]/div[1]/select')
select = Select(select_element)
select.select_by_value("onboarding_yogiyo")
select_element = driver.find_element(By.NAME,'type_depth2')
select = Select(select_element)
select.select_by_value("고윈(PC주문접수) 설치 요청")
driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[1]/form/div[2]/button[2]').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/ul/li[4]/ul').click()
wait = WebDriverWait(driver, 50)
for _ in range(1):
    driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[1]/a').click()
    wait = WebDriverWait(driver, 50)
    select_element = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div/div[1]/div[16]/div/select')
    select = Select(select_element)
    select.select_by_value("ready")
    driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div/div[2]/button').click()
    driver.back()
    wait = WebDriverWait(driver, 50)