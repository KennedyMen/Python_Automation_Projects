import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


website = "https://www.the-sun.com/entertainment/11399168/mary-kate-ashley-olsen-reunite-full-house-cast/"
path = "/Users/033103kennedymensah/Downloads/STASH_ON_DEVICE/chromedriver-mac-arm64/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
containers = driver.find_elements(
    by="xpath", value='//div[@class="article-recommendation-container"]')
titles = []
subtitles = []
links = []
for container in containers:
    container.find_element(by="xpath", value='./div/span').text
    # /div[@class="article-recommendation-container"]/a/div/div/div/div/span
    size = np.char.count(container.find_element(
        by="xpath", value='./div/span').text, ' ') + 1
    if size > 5:
        Title = container.find_element(by="xpath", value='./div/span').text
    else:
        Subtitle = container.find_element(by="xpath", value='./div/span').text
# //div[@class="article-recommendation-container"]/a
    link = container.find_enlement(
        by="xpath", value='./a').get_atttribute('href')
    titles.append(Title)
    subtitles.append(Subtitle)
    links.append(link)

dictionary = pd.DataFrame({'Title': titles, 'Subtitle': subtitles, 'Link': links}).to_csv(
