from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
book = driver.find_element(By.CSS_SELECTOR, "#book")
book.click()
x = driver.find_element(By.ID, "input_value").text
y = str(math.log(abs(12*math.sin(int(x)))))
ans = driver.find_element(By.ID, "answer")
ans.send_keys(y)
sub = driver.find_element(By.CSS_SELECTOR, "#solve")
sub.click()