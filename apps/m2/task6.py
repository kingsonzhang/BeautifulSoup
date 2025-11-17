import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from bs4 import BeautifulSoup, SoupReplacer, SoupStrainer

strainer = SoupStrainer("b")
soup = BeautifulSoup(open(sys.argv[1], encoding="utf-8"), "lxml", parse_only=strainer)
# Check line 603 in filter.py
print(soup.prettify())