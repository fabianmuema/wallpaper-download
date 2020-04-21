Download Wallpapers Using Python
================================

*   The \[website\]([https://wallpaperplay.com/) ](https://wallpaperplay.com/)
*   The web structure is organized, so BeautifulSoup can be used.
*   image contained in the collection\_thumb div
*   To get wallpaper includes changing the link to link to the main wallpaper.
*   filename of the wallpaper is the numbers just before the .jpg

Download Criteria
-----------------

1.  Have the term ‘4k’ in the a title attribute
2.  Have car in the title attribute
3.  Have more either the two attributes above or a like of above 50
4.  Must not exist in the fetched folder

Run the script to download the images every two weeks

### TODO

*   Scrape the website and get the content of the page using BeautifulSoup
*   Get the `<div class="collection_thumb">` element
*   Get the `a` tag from above element, check whether it contains car or 4k
*   if contains above, check whether it has a rating of 50 and above
*   if contains above two conditions, get the `img` element and get source.
*   check whether image already exists in folder
*   if it does not, change directory from `small-retina` to `full`.
*   Download image - file name = combination of numbers before `.jpg + .jpg`