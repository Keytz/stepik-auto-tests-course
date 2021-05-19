from selenium import webdriver
import time
link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("!!!!!!!!!!!!!!!!!!!!!!!!")
    button = browser.find_element_by_css_selector("body > div.container > form > button")
    button.click()
finally:
    time.sleep(10)
    browser.close()


