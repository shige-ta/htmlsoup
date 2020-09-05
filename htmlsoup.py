import requests
from bs4 import BeautifulSoup

class htmlsoup(object):

    def get_html_parser(self,url):
        res = requests.get(url)
        soup = BeautifulSoup(res.text,"html.parser")
        return soup

    def get_all_links(self,url):
        res = requests.get(url)
        soup = BeautifulSoup(res.text,"html.parser")
        atags = soup.find_all("a")
        links = []
        for link in atags:
            links.append(link.get("href"))
        return links

