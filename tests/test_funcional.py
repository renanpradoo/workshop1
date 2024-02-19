from selenium import webdriver
from time import sleep
import pytest
import subprocess
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options = options)
    driver.set_page_load_timeout(5)
    yield driver

    driver.quit()
    process.kill()

def test_app_opens(driver):
    driver.get("http://localhost:8501")
    sleep(2)
    # page_title = driver.title