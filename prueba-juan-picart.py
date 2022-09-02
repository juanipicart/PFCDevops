import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://localhost:8114")

campoUser = driver.find_element(By.ID, "user")
campoUser.clear()
campoUser.send_keys("root")

campoPassword = driver.find_element(By.NAME, "pass")
campoPassword.clear()
campoPassword.send_keys("password")

driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()
driver.get("http://localhost:8114")

botonNuevo = driver.find_element(By.XPATH, "//input[@value='Create new ticket']")
botonNuevo.click()

campoAsunto = driver.find_element(By.XPATH, "//input[@name='Subject']")
campoAsunto.send_keys("Este es un mensaje de prueba")

driver.find_element(By.XPATH, "//input[@name='SubmitTicket']").click()
driver.close()