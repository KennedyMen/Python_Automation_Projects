from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.the-sun.com/entertainment/11399168/mary-kate-ashley-olsen-reunite-full-house-cast/"
path = "/Users/033103kennedymensah/Downloads/STASH_ON_DEVICE/chromedriver-mac-arm64/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
containers = driver.find_elements(
    by="xpath", value='//div[@class="article-recommendation-container"]')

for container in containers:
    container.find_element(by="xpath", value='./div/span')
# /div[@class="article-recommendation-container"]/a/div/div/div/div/span
