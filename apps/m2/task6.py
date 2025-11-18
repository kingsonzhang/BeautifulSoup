from bs4 import BeautifulSoup, SoupReplacer, SoupStrainer

replacer = SoupReplacer("b", "blockquote")
soup = BeautifulSoup(open("./apps/Websites/BeautifulSoup.html", encoding="utf-8"), "lxml", replacer=replacer)
print(soup.prettify())