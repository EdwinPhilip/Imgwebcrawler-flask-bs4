"""Scrape img and link attributes from a requested Page URL."""
import requests
from bs4 import BeautifulSoup
import pprint

def fetch(url):
    pprint.pprint(url)
    # Function to fetch the page corresponding to the url and returns an object that has the following attributes:
    #     - assets - an array of urls present in the <img> tags on the page
    #     - links - an array of urls present in the <a> tags on the page
    pass
