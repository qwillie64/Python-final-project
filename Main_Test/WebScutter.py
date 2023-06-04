
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=1")



def search_google(keywords:str) : 
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.google.com.tw/")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(keywords)
    search_box.send_keys(Keys.RETURN)
    results = driver.find_elements(By.CLASS_NAME, 'c7r50')
    time.sleep(2)

    for i in results:
        print(i.text)

    driver.quit()
    

def search_spotify(keywords:str) : 
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(f"https://open.spotify.com/search/{keywords.replace(' ','%20')}/playlists")
    driver.refresh()
    time.sleep(2)
    results = driver.find_elements(by=By.CLASS_NAME, value='Nqa6Cw3RkDMV8QnYreTr')
    time.sleep(2)

    driver.quit()
    for i in results:
        print(i.get_attribute('href'))

    
    

search_spotify("anime song")