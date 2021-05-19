import math
import time

from selenium import webdriver

target_url=str(math.ceil(math.pow(math.pi, math.e)*10000))
print(target_url)
link="http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    variable1 = browser.find_element_by_link_text(target_url)
    variable1.click()

    #from lesson6_step4.py
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("body > div.container > form > button")
    button.click()
    #end
finally:
    time.sleep(5)
    browser.close()
