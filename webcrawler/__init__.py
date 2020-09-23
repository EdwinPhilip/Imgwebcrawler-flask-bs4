"""Scrape assets from target Page URL."""
import requests, re, os
from bs4 import BeautifulSoup
import pprint

from .fetchPage import fetch

def getWebsiteAssets(urls):
    # Function that will use the fetch(url) function and return all the assets from all the pages of the website

    for url in urls:
        imageUrls, linkUrls = fetch(url)
        for imageurl in imageUrls:
            print(imageurl)
            try:
                pos = imageurl.index("?")
                imageurl = imageurl[:pos]
            except ValueError:
                pass
            imgname = re.search(r'\/([\w._-]+[.](jpg|gif|png|svg))$', imageurl)
            if not imgname:
                print("Regex didn't match with the url: {}".format(imageurl))
                continue
            curpath = os.path.abspath(os.curdir)
            if 'http' not in imageurl:
                # sometimes an image source can be relative 
                # if it is, provide the base url which also happens 
                # to be the url variable. 
                imageurl = '{}{}'.format(url, imageurl)
            response = requests.get(imageurl, stream=True)
            with open(os.path.join(curpath,'images',imgname.group(1)), 'wb') as f:
                for chunk in response.iter_content():
                    f.write(chunk)
                print("Image saved :"+ imgname.group(1))
    return True
