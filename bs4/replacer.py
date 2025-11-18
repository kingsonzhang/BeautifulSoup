#Milestone2
from bs4.filter import SoupStrainer, PageElement, NavigableString, Tag

class SoupReplacer(SoupStrainer):
    def __init__(self, originalTag, newTag):
        self.originalTag = originalTag
        self.newTag = newTag
        super().__init__(self.newTag)

    def getOriginalTag(self):
        return self.originalTag
    
    def getNewTag(self):
        return self.newTag