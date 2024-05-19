import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

website = "https://www.the-sun.com/entertainment/11399168/mary-kate-ashley-olsen-reunite-full-house-cast/"
path = "/Users/033103kennedymensah/Downloads/STASH_ON_DEVICE/chromedriver-mac-arm64/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)
iframe = driver.find_element(By.XPATH, "/html/body/footer/div/div[2]/h3")
ActionChains(driver)\
    .scroll_to_element(iframe)\
    .perform()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="article-recommendation-container"]')))
containers = driver.find_elements(
    by="xpath", value='//div[@class="article-recommendation-container"]')
print(len(containers))
titles = []
subtitles = []
links = []
for container in containers:
    # /div[@class="article-recommendation-container"]/a/div/div/div/div/span
    Title = container.find_element(
        by="xpath", value='./a//span[1]').text
    Subtitle = container.find_element(
        by="xpath", value='./a//span[2]').text
# //div[@class="article-recommendation-container"]/a
    link = container.find_element(
        by="xpath", value='./a').get_attribute('href')
    links.append(link)
    titles.append(Title)
    subtitles.append(Subtitle)

dictionary = {'Title': titles, 'Subtitle': subtitles, 'Link': links}
df = pd.DataFrame(dictionary)
df.to_csv('Sun.csv')

driver.quit()
