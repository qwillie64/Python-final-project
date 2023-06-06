from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from random import randint, random

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=1")

_max_count = 15
_delay = [1, 2]
_random = False
_mes_func = print


# Search music from google
def search_google(keywords: str) -> dict:
    show_detail("-- Search start --")
    show_detail("Connecting to https://www.google.com.tw/")
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
    show_detail("-- Search start --")
    show_detail("Connecting to https://open.spotify.com/")
    t_start = time.process_time
    t_s_p_a = 0.0
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(
        f"https://open.spotify.com/search/{keywords.replace(' ','%20')}/playlists"
    )
    wait()
    results = driver.find_elements(By.CLASS_NAME, "Nqa6Cw3RkDMV8QnYreTr")
    wait()

    show_detail("Finding playlists")
    playlists = []
    for i in results:
        playlists.append(i.get_attribute("href"))
    driver.quit()

    show_detail("Finding songs in playlists : ")
    count = 0
    songs = []
    for list in playlists:
        show_detail(f" From : {list}")
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
            show_detail(f"  Finding {count + 1}/{_max_count}...")
            t_s = time.process_time()
            links = find_from(song_name[i].text, song_artist[i].text, 1)
            songs.append([song_name[i].text, song_artist[i].text, links[0]])
            t_s_p_a += time.process_time() - t_s
            count += 1
            if count >= _max_count:
                break
        driver.quit()
        wait()

        if count >= _max_count:
            break

    show_detail("-- Search finshed --")
    t_all = time.process_time - t_start
    show_detail(f"-- Process detail --")
    show_detail(f"progress :{t_all} second")
    show_detail(f"Search for all songs : {t_s_p_a} second")
    show_detail(f"Search for one song : {t_s_p_a/len(songs)} second")
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
    return linklists


# setting basic property for searching
def setting(
    total: int = _max_count,
    minDelay: int = _delay[0],
    maxDelay: int = _delay[1],
    random: bool = _random,
    messageFunction=print,
) -> dict:
    global _max_count
    _max_count = total
    global _delay
    _delay = [minDelay, maxDelay]
    global _random
    _random = random
    global _mes_func
    _mes_func = messageFunction

    d = {
        "total": _max_count,
        "min delay": _delay[0],
        "max delay": _delay[1],
        "random": _random,
    }
    show_detail("Setting propirty " + str(d))
    return d


# time.sleep function inside
def wait(min: float = _delay[0], max: float = _delay[1]):
    time.sleep(random() * (max - min) + min)


def show_detail(detailMessage: str):
    global _mes_func
    _mes_func(detailMessage)


if __name__ == "__main__":
    setting(5, 1, 1.5, True)
    print(search_spotify("anime song"))
    # print(find_from("losing it", "", 1))
