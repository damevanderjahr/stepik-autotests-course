from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('div.form-group #input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_css_selector('div.form-group #answer')
    input1.send_keys(str(y))

    option1 = browser.find_element_by_css_selector('div.form-check #robotCheckbox')
    option1.click()
    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
