from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/")
driver.maximize_window()

element = driver.find_element(By.XPATH, "//a[text()='HOME']")
if element is not None:
    print("Element found")
else:
    print("Element is missing")