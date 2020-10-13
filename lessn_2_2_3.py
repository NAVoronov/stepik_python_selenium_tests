from selenium import webdriver
import time 
import os
import math

link = "http://suninjuly.github.io/file_input.html"
wd = os.path.dirname(os.path.realpath(__file__))

try:
	#Открыть страницу http://suninjuly.github.io/file_input.html
    browser = webdriver.Chrome(executable_path = os.path.join(wd, 'webdriver', 'chromedriver.exe'))
    browser.get(link)

	#Заполнить текстовые поля: имя, фамилия, email
    browser.find_element_by_css_selector("input[name='firstname']").send_keys("Фамилия") 
    browser.find_element_by_xpath("//input[@name='lastname']").send_keys("Имя") 
    browser.find_element_by_css_selector("input[name='email']").send_keys("Почта") 

	#Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    browser.find_element_by_id("file").send_keys( os.path.join(wd, "конспект.txt") )

	#Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла