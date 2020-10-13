from selenium import webdriver
import time 
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
wd = os.path.dirname(os.path.realpath(__file__))

try:
	#Открыть страницу http://suninjuly.github.io/alert_accept.html
    browser = webdriver.Chrome(executable_path = os.path.join(wd, 'webdriver', 'chromedriver.exe'))
    browser.get(link)

    #Нажать на кнопку
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

    #Принять confirm
    browser.switch_to.alert.accept()

    #На новой странице решить капчу для роботов, чтобы получить число с ответом
	#Считать значение для переменной x.
    x = int( browser.find_element_by_id("input_value").text )
	#Посчитать математическую функцию от x.
    y = calc(x)
	#Ввести ответ в текстовое поле.
    browser.find_element_by_id("answer").send_keys( str(y) )

	#Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла