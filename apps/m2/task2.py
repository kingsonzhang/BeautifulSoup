from bs4 import BeautifulSoup, SoupStrainer
import sys

strainer = SoupStrainer("a")
soup = BeautifulSoup(open(sys.argv[1], encoding="utf-8"), "lxml", parse_only=strainer)
anchor_tags = soup.find_all("a")
with open("task2.txt", "w") as file:
    print(soup.prettify())