import csv
import datetime
import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
    def scrape(self):
        """
        Makes a request to a website and returns a Response object that has its HTML stored in it,
        along with additional data.
        The function r.read() returns the HTML from the Response object.
        All of the HTML from the website is in the variable html.
        BeautifulSoup parses the HTML.
        Looks for all "a" tags and "href" returns non-internal URL links.
        Writes to txt file.
        """
        # Create file named "YYYY_DDD_HH_MM_headlines"
        date = datetime.datetime.now()
        filename = date.strftime("%Y") + "_" + date.strftime("%j") + "_" + date.strftime("%I") + "_" + date.strftime("%M") + "_headlines"
        new_file = open (filename + ".txt", "w") # uses "w" in case file already created within last minute.
        new_file.close

        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)
                f = open (filename + ".txt", "a")
                f.write("\n" + url)
                f.close

# news = "https://www.news.yahoo.com"
news = "https://news.ycombinator.com"
# news = "https://news.google.com" # Google now uses a non-human-readable link-to-external-link. This scraper no longer produces useful results for news.google.com.
Scraper(news).scrape()
