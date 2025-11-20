#Milestone2
from bs4.filter import SoupStrainer

class SoupReplacer(SoupStrainer):
    def __init__(self, replaceData=None, name_xformer=None, attrs_xformer=None, xformer=None):
        self.replaceData = replaceData
        self.name_xformer=name_xformer
        self.attrs_xformer=attrs_xformer
        self.xformer=xformer
        if (replaceData):
            super().__init__(self.replaceData[1])
        else:
            super().__init__(True)

    def replaceTag(self, tag):
        if (tag == self.replaceData[0]):
            return self.replaceData[1]
        return tag