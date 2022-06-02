import requests
import time

urls = ["https://www.imdb.com","https://www.ynet.com", "https://www.google.com", "https://www.ratp.fr",  "https://developers.institute/en/"]


def calculate_time_to_load(url):
    t1 = time.time()
    requests.get(url)
    t2 = time.time()
    return t2 - t1


for url in urls:
    delta_time = calculate_time_to_load(url)
    print(f"To reach {url}, it takes {delta_time} seconds")
