import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import json
driver = webdriver.Chrome()
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = service, options=options)
service = Service("Users/shravannidankavi/Downloads/chromedriver_mac64/chromedriver")
service.start()
chrome_driver_path = '/Users/shravannidankavi/Downloads/chromedriver_mac64/chromedriver'
driver = webdriver.Chrome(chrome_driver_path)

def login_to_linkedin():
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/login")
    driver.find_element_by_id("username").send_keys("shravanprakash@gmail.com")
    driver.find_element_by_id("password").send_keys("Stealth007!")
    driver.find_element_by_id("login-submit").click()

def search_for_jobs(keyword, location):
    driver.find_element_by_id("jobs-search-box").send_keys(keyword)
    driver.find_element_by_id("jobs-search-location").send_keys(location)
    driver.find_element_by_id("jobs-search-button").click()

def apply_for_jobs():
    jobs = driver.find_elements_by_class_name("job-card")
    for job in jobs:
        job.find_element_by_class_name("job-card__apply-button").click()

def main():
    login_to_linkedin()
    search_for_jobs("site Reliability Engineer", "bangalore")
    apply_for_jobs()

if __name__ == "__main__":
    main()