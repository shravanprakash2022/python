from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import re, selenium
import json
driver = webdriver.Chrome()
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.python.org")

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

#driver.quit()

print("\nselenium version is \n \n", selenium.__version__, "\n\n")
class EasyApplyLinkedin:
    def __init__(self, data):
        """Parameter initialization"""

        self.email = data['email']
        self.password = data['password']
        self.keywords = data['keywords']
        self.location = data['location']
        self.driver = webdriver.Chrome(data['driver_path'])
if __name__ == '__main__':
    with open('/Users/shravannidankavi/labs/2023/python_lab/EasyApplyLinkedin/config.json') as config_file:
        data = json.load(config_file)
    bot = EasyApplyLinkedin(data)
    bot.apply()

#driver.quit()