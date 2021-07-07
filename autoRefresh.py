import time
from selenium import webdriver

refresh_time_in_seconds = 15
path = "C:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get('http://www.google.com')
url = driver.current_url
while(true):
    if url == driver.current.url:
        driver.refresh()
    url = driver.current.url
    time.sleep(refresh_time_in_seconds)