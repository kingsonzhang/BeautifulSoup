from bs4 import BeautifulSoup
import sys

soup = BeautifulSoup(open(sys.argv[1], encoding="utf-8"), "lxml")
print([tag.name for tag in soup.find_all()])