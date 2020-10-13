from selenium import webdriver
import time 
import os
import math

link = "http://suninjuly.github.io/selects1.html"
wd = os.path.dirname(os.path.realpath(__file__))

try:
    browser = webdriver.Chrome(executable_path = os.path.join(wd, 'webdriver', 'chromedriver.exe'))
    # Открыть страницу http://suninjuly.github.io/selects1.html
    browser.get(link)

    #Посчитать сумму заданных чисел
    sumka = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)

    #Выбрать в выпадающем списке значение равное расчитанной сумме
    browser.find_element_by_id("num1").click()
    browser.find_element_by_css_selector(f"#dropdown [value='{sumka}']").click()
    """
		from selenium.webdriver.support.ui import Select
		select = Select(browser.find_element_by_tag_name("select"))
		select.select_by_value("1") # ищем элемент с текстом "Python"
    """
    #Нажать кнопку "Submit"

    #Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла