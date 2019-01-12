from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

nameStr = 'Sanchez'
matStr = 'A01209929'
pinStr = '1234'

browser = webdriver.Chrome()
browser.get(('https://millenium.itesm.mx/patroninfo*spi'))

username = browser.find_element(By.XPATH, '//input[1]')
username.send_keys(nameStr)
matricula = browser.find_element_by_name('code')
matricula.send_keys(matStr)
pin = browser.find_element_by_name('pin')
pin.send_keys(pinStr)
nextButton = browser.find_element_by_name('submit')
nextButton.click()
ohterButton = browser.find_element(By.XPATH, '//form/a[2]')
ohterButton.click()
acceptButton = browser.find_element_by_name('renewall')
acceptButton.click()




