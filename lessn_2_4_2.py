from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import os
from my import *
import time

wd = os.path.dirname(os.path.realpath(__file__))

try:
    browser = webdriver.Chrome(executable_path = os.path.join(wd, 'webdriver', 'chromedriver.exe'))
    
    #Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    #Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    #text_to_be_present_in_element
    WebDriverWait(browser, 15).until( EC.text_to_be_present_in_element((By.ID, "price"), "$100") )    
    #Нажать на кнопку "Book"
    browser.find_element_by_id("book").click()

	#Проскроллить страницу вниз.
    browser.execute_script("window.scrollBy(0, 300);")

    #Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    my_math(browser)

	#Нажать кнопку "Submit"
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла