from selenium import webdriver
import time 
import os
import math

link = "http://suninjuly.github.io/find_xpath_form"
wd = os.path.dirname(os.path.realpath(__file__))

try:
    browser = webdriver.Chrome(executable_path = os.path.join(wd, 'webdriver', 'chromedriver.exe'))
    browser.get(link)

    elements = browser.find_elements_by_xpath("//input[@type='text']")
    for element in elements:
       element.send_keys("Мой ответ")

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

    alert=browser.switch_to_alert() 
    print (alert.text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла