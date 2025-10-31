import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from bs4 import BeautifulSoup, SoupReplacer

soupReplacer = SoupReplacer("b", "blockquote")
soup = BeautifulSoup(open(sys.argv[1], encoding="utf-8"), "lxml", replacer=soupReplacer)
print(soup.prettify())