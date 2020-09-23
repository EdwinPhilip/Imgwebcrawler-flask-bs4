"""Scrape img and link attributes from a requested Page URL."""
import requests
from bs4 import BeautifulSoup
import pprint

def fetch(url):
    # Function to fetch the page corresponding to the url and returns an object that has the following attributes:
    #     - assets - an array of urls present in the <img> tags on the page
    #     - links - an array of urls present in the <a> tags on the page

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600'
    }
    r = requests.get(url, headers=headers)
    html = BeautifulSoup(r.content, 'html.parser')
    imageUrls = get_imageSrc(html)
    linkUrls = get_linkHref(html)
    return imageUrls, linkUrls

def get_imageSrc(html):
    """Fetch image src"""
    imageUris = []
    if html.find_all("img"):
        images = html.find_all("img")
        for image in images:
            imageUris.append(image['src'])
    return imageUris

def get_linkHref(html):
    """Fetch Link href"""
    linkUris = []
    if html.find_all("a"):
        for link in html.find_all("a"):
            if link.has_attr('href'):
                linkUris.append(link['href'])
    return linkUris
