
# Importing Libraries---------------------------------------------------
import pandas as pd
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os
import sys
import hyperlink
# ---------------------------------------------------------------------

# Creating Executable Path
# --------------------------------------------------------------------------


website = "https://www.the-sun.com/"
path = "/Users/033103kennedymensah/Downloads/STASH_ON_DEVICE/chromedriver-mac-arm64/chromedriver"
# Headless Mode
Options_Headless = ChromeOptions()
Options_Headless.add_argument("--headless=new")
# --------------------------------------------------------------------------
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=Options_Headless)

driver.get(website)
iframe = driver.find_element(By.XPATH, "/html/body/footer/div/div[1]/h3")
ActionChains(driver)\
    .scroll_to_element(iframe)\
    .perform()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="teaser__copy-container"]')))
containers = driver.find_elements(
    by="xpath", value='//div[@class="teaser__copy-container"]')
print(len(containers))
titles = []
subtitles = []
links = []
# get names of sites
Header = driver.title
print(Header)
# --------------------------------------------------------------------------

for container in containers:
    # /div[@class="article-recommendation-container"]/a/div/div/div/div/span
    Subtitle = container.find_element(
        by="xpath", value='./a').get_attribute('data-headline')
    Title = container.find_element(
        by="xpath", value='./a//span').get_attribute('data-original-text')
# //div[@class="article-recommendation-container"]/a
    link = container.find_element(
        by="xpath", value='./a').get_attribute('href')

    links.append(link)
    titles.append(Title)
    subtitles.append(Subtitle)

dictionary = {'Title': titles, 'Subtitle': subtitles, 'Link': links}
df = pd.DataFrame(dictionary)
df.to_csv('site.csv')

driver.quit()
