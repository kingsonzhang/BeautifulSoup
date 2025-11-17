#Milestone2
from typing import Optional
from bs4._typing import _RawAttributeValues

from bs4.filter import SoupStrainer, PageElement, NavigableString, Tag

class SoupReplacer(SoupStrainer):
    def __init__(self, ogTag, altTag):
        self.ogTag = ogTag
        self.altTag = altTag