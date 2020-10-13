from selenium import webdriver
import time 
import os
import math

link = "http://suninjuly.github.io/registration2.html"
wd = os.path.dirname(os.path.realpath(__file__))

try:
#    browser = webdriver.Chrome(executable_path = os.path.join(wd, 'webdriver', 'chromedriver.exe'))
    browser = webdriver.Chrome()
    browser.get(link)

    el = browser.find_element_by_css_selector(".first_block .form-control.first")
    el.send_keys("Фамилия") 

    el = browser.find_element_by_css_selector(".first_block .form-control.second")
    el.send_keys("Имя") 

    el = browser.find_element_by_css_selector(".form-control.third")
    el.send_keys("Почта") 

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла