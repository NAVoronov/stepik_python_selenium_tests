from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

def my_math(browser):
	x = int( browser.find_element_by_id("input_value").text )
	#browser.execute_script(f"alert({x});")
	#Посчитать математическую функцию от x.
	y = calc(x)
	#Ввести ответ в текстовое поле.
	browser.find_element_by_id("answer").send_keys( str(y) )