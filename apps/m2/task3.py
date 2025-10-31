from bs4 import BeautifulSoup, SoupStrainer
import sys

strainer = SoupStrainer(True)
soup = BeautifulSoup(open(sys.argv[1], encoding="utf-8"), "lxml", parse_only=strainer)
for tag in soup.find_all(True):
    print(tag)