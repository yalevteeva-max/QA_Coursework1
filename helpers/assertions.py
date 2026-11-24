def assert_success(driver):
    assert "Успешно" in driver.page_source, "Сообщение об успехе не появилось"

def assert_declined(driver):
    page_source = driver.page_source
    assert "Операция отклонена" in page_source or "Отказ" in page_source, "БАГ: Приложение одобрило операцию по карте DECLINED!"