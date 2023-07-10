from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = 'shravanprakash@gmail.com'
ACCOUNT_PASSWORD = 'Stealth007!'
PHONE = 9902026081

chrome_driver_path = '/Users/shravannidankavi/Downloads/chromedriver_mac64/chromedriver'
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3619160384&distance=25&f_AL=true&f_E=3%2C4&f_F=bd%2Crsch%2Ceng%2Cit&f_I=104%2C6%2C4%2C3%2C84%2C41%2C8%2C96%2C118%2C3133%2C43%2C11%2C3231&f_PP=109710172%2C105214831&f_T=131%2C22848%2C25764%2C9%2C30006%2C10%2C25890%2C26262%2C39&f_WT=1%2C2%2C3&geoId=105214831&keywords=sre&location=Bengaluru%2C%20Karnataka%2C%20India&refresh=true&sortBy=R ")

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

#Locate the apply button
time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

#Submit the application
submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()