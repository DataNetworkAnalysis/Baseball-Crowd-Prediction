import os
from selenium import webdriver
from utils import download

# save directory
data_dir = os.path.abspath(os.path.join(os.getcwd(), '../dataset'))

# driver setting
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# crawling
driver = download.kbo_crowd(driver, data_dir)
driver = download.statiz_record(driver, data_dir)
driver.close()


