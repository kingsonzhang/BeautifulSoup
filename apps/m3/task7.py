import sys
from bs4 import BeautifulSoup, SoupReplacer, SoupStrainer

def add_class_attr(tag):
    tag.attrs["class"] = "test"

replacer = SoupReplacer(replaceData=('b', 'b'), attrs_xformer=add_class_attr)
soup = BeautifulSoup(open(sys.argv[1], encoding="utf-8"), "lxml", replacer=replacer)
print(soup.prettify())