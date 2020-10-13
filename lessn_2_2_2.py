from selenium import webdriver
import time 
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
wd = os.path.dirname(os.path.realpath(__file__))

try:
    browser = webdriver.Chrome(executable_path = os.path.join(wd, 'webdriver', 'chromedriver.exe'))
    # Открыть страницу http://suninjuly.github.io/execute_script.html
    browser.get(link)

	#Считать значение для переменной x.
    x = int( browser.find_element_by_id("input_value").text )

	#Посчитать математическую функцию от x.
    y = calc(x)
	
	#Проскроллить страницу вниз.
    browser.execute_script("window.scrollBy(0, 100);")

	#Ввести ответ в текстовое поле.
    browser.find_element_by_id("answer").send_keys( str(y) )
	
	#Выбрать checkbox "I'm the robot".
    browser.find_element_by_css_selector("#robotCheckbox").click()    
	
	#Переключить radiobutton "Robots rule!".
    browser.find_element_by_css_selector("#robotsRule").click()

	#Нажать на кнопку "Submit".
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла