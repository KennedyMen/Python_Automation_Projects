import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


website = "https://www.the-sun.com/entertainment/11399168/mary-kate-ashley-olsen-reunite-full-house-cast/"
path = "/Users/033103kennedymensah/Downloads/STASH_ON_DEVICE/chromedriver-mac-arm64/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)
driver.implicitly_wait(10)
containers = driver.find_elements(
    by="xpath", value='//div[@class="article-recommendation-container"]')
print(len(containers))
titles = []
subtitles = []
links = []
for container in containers:
    string = container.find_element(
        by="xpath", value='//div[@class="article-recommendation-container"]/a/div/div/div/div/span').text
    # /div[@class="article-recommendation-container"]/a/div/div/div/div/span
    size = np.char.count(string, ' ') + 1
    if size < 5:
        Title = container.find_element(
            by="xpath", value='//div[@class="article-recommendation-container"]/a/div/div/div/div/span').text
        titles.append(Title)
    else:
        Subtitle = container.find_element(
            by="xpath", value='//div[@class="article-recommendation-container"]/a/div/div/div/div/span').text
        subtitles.append(Subtitle)
# //div[@class="article-recommendation-container"]/a
    link = container.find_element(
        by="xpath", value='//div[@class="article-recommendation-container"]/a').get_attribute('href')
    links.append(link)

dictionary = ({'Title': titles, 'Subtitle': subtitles, 'Link': links})
pd.DataFrame(dictionary).to_csv('Website.csv')

driver.quit()
