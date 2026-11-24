import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pymysql
import psycopg2  

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

@pytest.fixture
def db_connection_postgres():
    connection = psycopg2.connect(
        host='localhost',
        port=5432,
        user='app',
        password='pass',
        dbname='app'
    )
    yield connection
    connection.close()