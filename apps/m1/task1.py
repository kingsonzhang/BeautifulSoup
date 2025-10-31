from bs4 import BeautifulSoup
import sys

soup = BeautifulSoup(open(sys.argv[1], encoding="utf-8"), "lxml")
with open("task1.txt", "w") as file:
    file.write(soup.prettify())