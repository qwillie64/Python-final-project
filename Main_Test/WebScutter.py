from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from random import randint

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=1")

# Search music from google
def search_google(keywords: str, random: bool = False, max: int = 3) -> dict:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.google.com.tw/")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(keywords)
    search_box.send_keys(Keys.RETURN)
    results = driver.find_elements(By.CLASS_NAME, "c7r50")
    time.sleep(randint(2, 5))

    for i in results:
        print(i.text)

    driver.quit()


# Search music from spotify
def search_spotify(keywords: str, random: bool = False, max: int = 3) -> dict:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(
        f"https://open.spotify.com/search/{keywords.replace(' ','%20')}/playlists"
    )
    time.sleep(2)
    results = driver.find_elements(By.CLASS_NAME, "Nqa6Cw3RkDMV8QnYreTr")
    time.sleep(randint(1, 3))

    playlists = []
    for i in results:
        playlists.append(i.get_attribute("href"))
    driver.quit()

    count = 0
    songs = {}
    for list in playlists:
        # print(f"url = {list}")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(list)
        time.sleep(2)
        song_name = driver.find_elements(
            By.XPATH,
            "//*[@class='Type__TypeElement-sc-goli3j-0 cvuJgi t_yrXoUO3qGsJS4Y6iXX standalone-ellipsis-one-line']",
        )
        time.sleep(2)
        song_artist = driver.find_elements(
            By.XPATH,
            "//*[@class='Type__TypeElement-sc-goli3j-0 fjvaLo rq2VQ5mb9SDAFWbBIUIn standalone-ellipsis-one-line']",
        )
        time.sleep(randint(1, 3))

        for i in range(0, len(song_name)):
            songs[song_name[i].text] = song_artist[i].text
        driver.quit()

        if random:
            count += randint(1, 5)
        else:
            count += 1

        if count >= max:
            break
        time.sleep(randint(1, 3))
    return songs


if __name__=="__main__":
    print(search_spotify("anime song", False, 10))