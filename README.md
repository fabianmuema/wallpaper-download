# Welcome to Wallpaper Downloader 👋
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000)
[![Documentation](https://img.shields.io/badge/documentation-yes-brightgreen.svg)](https://github.com/fabianmuema/wallpaper-download/blob/master/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/fabianmuema/wallpaper-download/blob/master/LICENSE)
[![Twitter: fabian\_muema\_m](https://img.shields.io/twitter/follow/fabian\_muema\_m.svg?style=social)](https://twitter.com/fabian\_muema\_m)

### 🏠 [Homepage]()

## Description

Download wallpapers automatically with python from https://wallpaperplay.com and save them in the variety Fetched directory. Variety takes care of the rest.

# Download Wallpapers Using Python

- The [website]([https://wallpaperplay.com/)
- The web structure is organized, so BeautifulSoup can be used.
- image contained in the collection_thumb div
- To get wallpaper includes changing the link to link to the main wallpaper.
- filename of the wallpaper is the numbers just before the .jpg

## Download Criteria

1. Have the term ‘4k’ in the a title attribute
2. Have car in the title attribute
3. Have more either the two attributes above or a like of above 50
4. Must not exist in the fetched folder

### TODO

[x] Scrape the website and get the content of the page using BeautifulSoup

[x] Get the `` element 

[x] Get the `a` tag from above element, check whether it contains car or 4k

[x] if contains above, check whether it has a rating of 50 and above

[x] if contains above two conditions, get the `img` element and get source.

[x] check whether image already exists in folder

[x] if it does not, change directory from `small-retina` to `full`.

[x] Download image - file name = combination of numbers before `.jpg + .jpg`

## Install

```sh
git clone https://github.com/fabianmuema/wallpaper-download.git
```

## Usage

```sh
cd wallpaper-download
python -m venv ./
source bin/activate
pip install -r requirements.txt
python app.py
```

## Author

👤 **Fabian Muema**

* Website: http://fabianmuema.github.io
* Twitter: [@fabian\_muema\_m](https://twitter.com/fabian\_muema\_m)
* Github: [@fabianmuema](https://github.com/fabianmuema)
* LinkedIn: [@fabianmuema](https://linkedin.com/in/fabianmuema)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

Feel free to check [issues page](https://github.com/fabianmuema/wallpaper-download/issues). 

## Show your support

Give a ⭐️ if this project helped you!

[![support us](https://img.shields.io/badge/become-a patreon%20us-orange.svg?cacheSeconds=2592000)](https://www.patreon.com/fabianmuema)


## 📝 License

Copyright © 2020 [Fabian Muema](https://github.com/fabianmuema).

This project is [MIT](https://github.com/fabianmuema/wallpaper-download/blob/master/LICENSE) licensed.

***
