from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.card_inputs = (By.CSS_SELECTOR, "input.input__control")
        self.continue_button = (By.XPATH, "//button[.//span[text()='Продолжить']]")
        self.success_message = (By.XPATH, "//*[contains(text(), 'Успешно')]")
        self.error_message = (By.XPATH, "//*[contains(text(), 'Операция отклонена') or contains(text(), 'Отказ')]")

    def fill_form(self, card_number, month, year, holder, cvc):
        inputs = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.card_inputs)
        )
        inputs[0].send_keys(card_number)
        inputs[1].send_keys(month)
        inputs[2].send_keys(year)
        inputs[3].send_keys(holder)
        inputs[4].send_keys(cvc)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def wait_for_success(self):
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.success_message)
        )

    def wait_for_error(self):
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message)
        )