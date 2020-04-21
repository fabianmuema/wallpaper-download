import os.path
import urllib.request

import requests
from bs4 import BeautifulSoup

url = 'https://wallpaperplay.com/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
c_thumb = soup.find_all('div', class_='collection_thumb')

for c in c_thumb:
    a = c.findChildren('a', title=True, class_='image')
    title = a[0]['title']

    # get the image source
    image_tag = c.findChildren('img')
    r_div = c.findChildren('div', class_='image_cap_right')
    for r in r_div:
        rating = int(r.select('div > span')[1].get_text(strip=True))
        if "car" in title or "4k" in title or "Hd" in title or rating >= 50:
            for image in image_tag:
                img_url = 'https://wallpaperplay.com' + image.get('data-src')
                img_url = img_url.replace('small-retina', 'full')
                if not os.path.isfile('/home/fabian/.config/variety/Fetched/' + img_url[-8:]):
                    urllib.request.urlretrieve(img_url, '/home/fabian/.config/variety/Fetched/' + img_url[-8:])
                    print('Wallpaper downloaded successfully')
