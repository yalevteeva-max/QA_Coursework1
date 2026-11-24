import allure
from pages.main_page import MainPage
from pages.payment_page import PaymentPage
from data.test_data import VALID_CARD, MONTH, YEAR, HOLDER, CVC

@allure.title("Проверка записи в БД после успешной оплаты")
def test_db_after_successful_payment(driver, db_connection):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)
    
    main_page.open()
    main_page.click_buy()
    payment_page.fill_form(VALID_CARD, MONTH, YEAR, HOLDER, CVC)
    payment_page.click_continue()
    payment_page.wait_for_success()
    
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT * FROM payment_entity ORDER BY created DESC LIMIT 1")
        result = cursor.fetchone()
    
    assert result is not None, "В базе данных нет записей о платежах"
    assert result['status'] == 'APPROVED', f"Неверный статус в БД: {result['status']}"