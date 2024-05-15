import pytest  
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    # 取得瀏覽器的設定資料
    browser_options = Options() 
    # 不顯示瀏覽器
    # browser_options.add_argument('--headless') 
    # 启动浏览器
    browser = webdriver.Chrome(options=browser_options)
    # 等待瀏覽器開啟
    browser.implicitly_wait(20)
    # 送出瀏覽器物件
    yield browser
    # 关闭浏览器
    browser.quit()

scenarios('../features/login.feature')  

@given(parsers.parse('I visit login page'))
def set_account(driver):
    driver.get('http://127.0.0.1:5000/login')

@when(parsers.parse('I enter {account} in the account field'))
def set_password(driver, account):
    driver.find_element(By.NAME, 'name').send_keys(account)
 
@when(parsers.parse('I enter {password} in the password field'))
def set_password(driver, password):
    driver.find_element(By.NAME, 'password').send_keys(password)

@when(parsers.parse('I press the login button'))
def click_login_button(driver):
    driver.find_element(By.XPATH, '/html/body/form/button').click()

@then(parsers.parse('I should see the hello'))  
def login_success(driver):
    data = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, '/html/body/h1')))
    assert 'hello' == data.text