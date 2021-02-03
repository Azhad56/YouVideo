from selenium import webdriver
import os
import time
import random
from selenium.webdriver.chrome.options import Options


class GetViews:
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=options)

    def getviews(self):
        videos = ["https://www.youtube.com/watch?v=PkVjkVotWHE",
                  "https://www.youtube.com/watch?v=SrhhVjtm_ew&t"]
        url = random.choice(videos)
        print(url)
        self.driver.get(url)
        while(True):
            time.sleep(random.randint(10, 20))
            url = random.choice(videos)
            print(url)
            self.driver.refresh()

    def closeBrowser(self):
        self.driver.close()
