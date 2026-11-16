import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Успешная покупка тура по дебетовой карте")
def test_successful_payment(driver):
    driver.get("http://localhost:8080")
    wait = WebDriverWait(driver, 10)
    
    buy_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Купить']]")))
    buy_button.click()
    
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(), 'Оплата по карте')]")))
    
    inputs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.input__control")))
    inputs[0].send_keys("4444 4444 4444 4441")
    inputs[1].send_keys("12")
    inputs[2].send_keys("26")
    inputs[3].send_keys("IVAN IVANOV")
    inputs[4].send_keys("123")
    
    driver.find_element(By.XPATH, "//button[.//span[text()='Продолжить']]").click()
    time.sleep(2)
    
    assert "Успешно" in driver.page_source, "Сообщение об успехе не появилось"