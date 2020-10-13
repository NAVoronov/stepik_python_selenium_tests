from selenium import webdriver
import time 
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
wd = os.path.dirname(os.path.realpath(__file__))

try:
    browser = webdriver.Chrome(executable_path = os.path.join(wd, 'webdriver', 'chromedriver.exe'))
    # Открыть страницу http://suninjuly.github.io/get_attribute.html.
    browser.get(link)

	#Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    el = browser.find_element_by_id("treasure")
	
	#Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.    
    x = el.get_attribute("valuex")

    # Посчитать математическую функцию от x (код для этого приведён ниже).
    y = calc(x)

	#Ввести ответ в текстовое поле.
    el = browser.find_element_by_id("answer")
    el.send_keys(y) 

    # Отметить checkbox "I'm the robot".
    el = browser.find_element_by_css_selector("#robotcheckbox")
    el.click()    

    #Выбрать radiobutton "Robots rule!".    
    el = browser.find_element_by_css_selector("#robotsrule")
    el.click()    

    #Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла