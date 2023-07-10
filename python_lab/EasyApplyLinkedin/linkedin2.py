from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
email = os.environ.get('shravanprakash@gmail.com')
password = os.environ.get('Stealth007!')
service = Service('/Users/shravannidankavi/Downloads/chromedriver_mac64/chromedriver')
service.start()

url = "https://www.linkedin.com/jobs/search/?currentJobId=3619160384&distance=25&f_AL=true&f_E=3%2C4&f_F=bd%2Crsch%2Ceng%2Cit&f_I=104%2C6%2C4%2C3%2C84%2C41%2C8%2C96%2C118%2C3133%2C43%2C11%2C3231&f_PP=109710172%2C105214831&f_T=131%2C22848%2C25764%2C9%2C30006%2C10%2C25890%2C26262%2C39&f_WT=1%2C2%2C3&geoId=105214831&keywords=sre&location=Bengaluru%2C%20Karnataka%2C%20India&refresh=true&sortBy=R "
driver = webdriver.Remote(service.service_url)
driver.get(url)
time.sleep(3)
sign_in = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in.click()
username_input = driver.find_element(by=By.ID, value="username")
username_input.send_keys(email)
password_input = driver.find_element(by=By.ID, value="password")
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)
time.sleep(30)
driver.quit()