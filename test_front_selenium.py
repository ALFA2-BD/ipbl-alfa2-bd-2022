from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("http://127.0.0.1:8000/admin/")

driver.close()