import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pymysql

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def db_connection():
    connection = pymysql.connect(
        host='localhost',
        port=3307,
        user='app',
        password='pass',
        database='app',
        cursorclass=pymysql.cursors.DictCursor
    )
    yield connection
    connection.close()