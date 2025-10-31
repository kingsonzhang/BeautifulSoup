# Placing a bold "FOUND" in front of all p elements

from bs4 import BeautifulSoup
import sys

soup = BeautifulSoup(open(sys.argv[1], encoding="utf-8"), "lxml")
for tags in soup.find_all("p"):
    tags.insert_before(soup.new_tag("b", string="FOUND"))
with open("task8.txt", "w") as file:
    file.write(soup.prettify())