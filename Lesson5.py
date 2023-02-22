import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/find_link_text")

inp = driver.find_element(By.LINK_TEXT, "224592")
inp.click()


input1 = driver.find_element(By.TAG_NAME, "input")
input1.send_keys("Ivan")
input2 = driver.find_element(By.NAME, "last_name")
input2.send_keys("Petrov")
input3 = driver.find_element(By.CLASS_NAME, "form-control.city")
input3.send_keys("Smolensk")
input4 = driver.find_element(By.ID, "country")
input4.send_keys("Russia")
button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(30)
driver.quit()
