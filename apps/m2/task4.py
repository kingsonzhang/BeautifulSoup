from bs4 import BeautifulSoup, SoupStrainer
import sys

strainer = SoupStrainer(id=True)
soup = BeautifulSoup(open("./apps/Websites/BeautifulSoup.html", encoding="utf-8"), "lxml", parse_only=strainer)
for tag in soup.find_all(id=True):
    print(tag)