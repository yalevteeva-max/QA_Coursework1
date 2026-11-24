import allure
from pages.main_page import MainPage
from pages.payment_page import PaymentPage
from data.test_data import VALID_CARD, DECLINED_CARD, MONTH, YEAR, HOLDER, CVC
from helpers.assertions import assert_success, assert_declined

@allure.title("Успешная выдача кредита по данным карты")
def test_successful_credit(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)
    
    main_page.open()
    main_page.click_credit()
    payment_page.fill_form(VALID_CARD, MONTH, YEAR, HOLDER, CVC)
    payment_page.click_continue()
    payment_page.wait_for_success()
    
    assert_success(driver)

@allure.title("Отказ в выдаче кредита по данным карты (DECLINED)")
def test_declined_credit(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)
    
    main_page.open()
    main_page.click_credit()
    payment_page.fill_form(DECLINED_CARD, MONTH, YEAR, HOLDER, CVC)
    payment_page.click_continue()
    
    # Здесь мы ожидаем ошибку, но из-за бага её нет, поэтому тест упадет (это правильно)
    payment_page.wait_for_error()
    assert_declined(driver)