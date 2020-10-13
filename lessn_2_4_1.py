from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import os

wd = os.path.dirname(os.path.realpath(__file__))

try:
    browser = webdriver.Chrome(executable_path = os.path.join(wd, 'webdriver', 'chromedriver.exe'))

    browser.get("http://suninjuly.github.io/wait2.html")

    # ������� Selenium ��������� � ������� 5 ������, ���� ������ �� ������ ������������
    button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "verify"))
        )
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    # �������� ����������� ��� �� 30 ������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()

# �� �������� �������� ������ ������ � ����� �����