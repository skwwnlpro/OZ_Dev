import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

url = "https://www.melon.com/chart/index.htm"
res = requests.get(url, headers=headers)

html = res.text
soup = BeautifulSoup(html, "html.parser")

wraps = soup.select("tr[data-song-no]")


for wrap in wraps:

    rank = wrap.select_one(".rank").text
    title = wrap.select_one(".ellipsis.rank01 a").text
    artist = wrap.select_one(".ellipsis.rank02 a").text
    album = wrap.select_one(".ellipsis.rank03 a").text

    print(f"순위 : {rank}")
    print(f"노래 제목 : {title}")
    print(f"노래 가수 : {artist}")
    print(f"앫범 : {album}")
