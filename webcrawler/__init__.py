"""Scrape assets from target Page URL."""
import requests
from bs4 import BeautifulSoup
import pprint

from .fetchPage import fetch

def getWebsiteAssets(url):
    fetch(url)
    # Function that will use the fetch(url) function and return all the assets from all the pages of the website
    pass
