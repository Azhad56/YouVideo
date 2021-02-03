from selenium import webdriver
import os
import time
import random
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome()

videos = ["https://www.youtube.com/watch?v=PkVjkVotWHE",
          "https://www.youtube.com/watch?v=SrhhVjtm_ew&t"]

url = random.choice(videos)

driver.get(url)

while(True):
    time.sleep(random.randint(50, 110))
    url = random.choice(videos)
    print(url)
    driver.refresh()
# Now you can start using Selenium
driver.close()
