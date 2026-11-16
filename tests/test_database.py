import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Проверка записи в БД после успешной оплаты")
def test_db_after_successful_payment(driver, db_connection):
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
    
    result = None
    for _ in range(10):
        time.sleep(1)
        with db_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM payment_entity ORDER BY created DESC LIMIT 1")
            result = cursor.fetchone()
            if result is not None:
                break
    
    assert result is not None, "В базе данных нет записей о платежах"
    assert result['status'] == 'APPROVED', f"Неверный статус в БД: {result['status']}"