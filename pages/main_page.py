from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://localhost:8080"
        self.buy_button = (By.XPATH, "//button[.//span[text()='Купить']]")
        self.credit_button = (By.XPATH, "//button[.//span[text()='Купить в кредит']]")

    def open(self):
        self.driver.get(self.url)

    def click_buy(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.buy_button)).click()

    def click_credit(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.credit_button)).click()