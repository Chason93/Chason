
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # 웹 드라이버 시작
# driver = webdriver.Chrome() 
# # 크롬 드라이버에 url 주소 넣고 실행
# driver.get('https://ceo-portal.yogiyo.co.kr/assign/ticket/detail/4142764')

# # SelectBox__Select-sc-weu0am-1 클래스를 가진 select 요소를 찾습니다.
# status_select = Select(driver.find_element(By.CLASS_NAME, 'SelectBox__Select-sc-weu0am-1'))

# # "처리 중" 옵션을 선택합니다.
# status_select.select_by_value('in_progress')

# # 변경된 상태를 확인합니다.
# # 예를 들어, 버튼을 클릭하여 저장할 수 있습니다.
# save_button = driver.find_element(By.ID, 'save_button_id')
# save_button.click() 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# ChromeOptions 객체 생성
options = Options()
user_data = r"C:\Users\B201812058\AppData\Local\Google\Chrome\User Data"
options.add_experimental_option("detach", True)
options.add_argument(f"user-data-dir={user_data}")

# 웹 드라이버 시작
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)
wait = WebDriverWait(driver, 50)
# 로그인 페이지로 이동
driver.get('https://ceo-portal.yogiyo.co.kr/assign/ticket/detail/4148901')

wait = WebDriverWait(driver, 50)

# 로그인 정보 입력
username = driver.find_element(By.NAME, 'username')  # 예시: 로그인 페이지의 사용자 이름 입력란 ID
password = driver.find_element(By.NAME, 'password')  # 예시: 로그인 페이지의 비밀번호 입력란 ID
login_button = driver.find_element(By.CLASS_NAME, 'Button__StyleButton-sc-2z9iin-0')  # 예시: 로그인 페이지의 로그인 버튼 ID

username.send_keys('jiwon.chaA')  # 여기에 사용자 이름 입력
password.send_keys('terminal1@')  # 여기에 비밀번호 입력
login_button.click()

wait = WebDriverWait(driver, 3)

 # 로그인 완료 후 다음 페이지로 이동
#next_page_url = 'https://ceo-portal.yogiyo.co.kr/assign/ticket/detail/4148901'  # 다음 페이지의 URL
#driver.get(next_page_url)

# # 페이지가 완전히 로드될 때까지 기다립니다.
# wait = WebDriverWait(driver, 3)
# status_select = wait.until(EC.presence_of_element_located((By.NAME, 'status')))

# # "처리 중" 옵션을 선택합니다.
# status_select = Select(status_select)
# status_select.select_by_value('in_progress')

# # 변경된 상태를 저장합니다.
# save_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Button__StyleButton-sc-2z9iin-0')))
# save_button.click()
