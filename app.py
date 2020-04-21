import requests
from bs4 import BeautifulSoup

url = "https://wallpaperplay.com/"
page = requests.get(url)
