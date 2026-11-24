import allure
from pages.main_page import MainPage
from pages.payment_page import PaymentPage
from data.test_data import VALID_CARD, MONTH, YEAR, HOLDER, CVC
from helpers.assertions import assert_success

@allure.title("Успешная покупка тура по дебетовой карте")
def test_successful_payment(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)
    
    main_page.open()
    main_page.click_buy()
    payment_page.fill_form(VALID_CARD, MONTH, YEAR, HOLDER, CVC)
    payment_page.click_continue()
    payment_page.wait_for_success()
    
    assert_success(driver)