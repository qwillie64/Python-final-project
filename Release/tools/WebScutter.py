from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from random import randint, randrange

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=1")

_max_count = 15
_delay = [1, 2]
_random = False
_mes_func = print


# Search music from google
def search_google(keywords: str) -> dict:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.google.com.tw/")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(keywords)
    search_box.send_keys(Keys.RETURN)
    wait()
    results = driver.find_elements(By.CLASS_NAME, "c7r50")
    wait()

    for i in results:
        print(i.text)

    driver.quit()


# Search music from spotify
def search_spotify(keywords: str) -> list:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(
        f"https://open.spotify.com/search/{keywords.replace(' ','%20')}/playlists"
    )
    wait()
    results = driver.find_elements(By.CLASS_NAME, "Nqa6Cw3RkDMV8QnYreTr")
    wait()

    playlists = []
    for i in results:
        playlists.append(i.get_attribute("href"))
    driver.quit()

    count = 0
    songs = []
    for list in playlists:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(list)
        wait()
        song_name = driver.find_elements(
            By.XPATH,
            "//*[@class='Type__TypeElement-sc-goli3j-0 cvuJgi t_yrXoUO3qGsJS4Y6iXX standalone-ellipsis-one-line']",
        )
        wait()
        song_artist = driver.find_elements(
            By.XPATH,
            "//*[@class='Type__TypeElement-sc-goli3j-0 fjvaLo rq2VQ5mb9SDAFWbBIUIn standalone-ellipsis-one-line']",
        )
        wait()

        for i in range(0, len(song_name), (lambda: randint(1, 6) if _random else 1)()):
            print(f"Finding {count + 1}/{_max_count}...")
            links = find_from(song_name[i].text, song_artist[i].text, 1)
            songs.append([song_name[i].text, song_artist[i].text, links[0]])
            count += 1
            if count >= _max_count:
                return songs
        driver.quit()
        wait()

    return songs


# find music online link by given name and artist
def find_from(songName: str, songArtist: str, max: int = 3) -> list:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.youtube.com")
    wait()
    search_box = driver.find_element(by=By.NAME, value="search_query")
    search_box.send_keys(f"{songName} - {songArtist}")
    search_box.send_keys(Keys.RETURN)
    wait(1.5, 2)
    results = driver.find_elements(
        By.XPATH, "//*[@class='yt-simple-endpoint style-scope ytd-video-renderer']"
    )
    wait(2, 3)

    linklists = []
    if len(results) < max:
        max = len(results)
    for i in range(0, max):
        linklists.append(results[i].get_attribute("href"))

    driver.quit()
    print(linklists)
    return linklists


# setting basic property for searching
def setting(
    total: int = _max_count,
    minDelay: int = _delay[0],
    maxDelay: int = _delay[1],
    random: bool = _random,
    messageFunction: function = print,
) -> dict:
    global _max_count
    _max_count = total
    global _delay
    _delay = [minDelay, maxDelay]
    global _random
    _random = random
    global _mes_func
    _mes_func = messageFunction

    return {
        "total": _max_count,
        "min delay": _delay[0],
        "max delay": _delay[1],
        "random": _random,
    }


# time.sleep function inside
def wait(min: float = _delay[0], max: float = _delay[1]):
    time.sleep(randrange(min, max + 1))


def show_detail(detailMessage: str):
    global _mes_func
    _mes_func(detailMessage)


if __name__ == "__main__":
    setting(5, 1, 1.5, True)
    print(search_spotify("anime song"))
    # print(find_from("losing it", "", 1))
