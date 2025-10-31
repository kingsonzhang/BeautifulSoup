from bs4 import BeautifulSoup
import sys

soup = BeautifulSoup(open(sys.argv[1], encoding="utf-8"), "lxml")
for links in soup.find_all("a"):
    print(links.get("href"))