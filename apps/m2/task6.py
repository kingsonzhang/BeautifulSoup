import sys
from bs4 import BeautifulSoup, SoupReplacer, SoupStrainer

replacer = SoupReplacer(("b", "blockquote"))
soup = BeautifulSoup(open(sys.argv[1], encoding="utf-8"), "lxml", replacer=replacer)
print(soup.prettify())