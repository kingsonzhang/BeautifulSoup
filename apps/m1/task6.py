from bs4 import BeautifulSoup
import sys

soup = BeautifulSoup(open(sys.argv[1], encoding="utf-8"), "lxml")
for tags in soup.find_all("b"):
    tags.name = "blockquote"
with open("task6.txt", "w") as file:
    file.write(soup.prettify())