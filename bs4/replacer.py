#Milestone2
from typing import Optional
from bs4._typing import _RawAttributeValues

class SoupReplacer:
    def __init__(self, ogTag, altTag):
        self.ogTag = ogTag
        self.altTag = altTag

    def replaceTag(self, name):
        if name == self.ogTag:
            return self.altTag
        return name
    
    @property
    def excludes_everything(self) -> bool:
        """Does this `ElementFilter` obviously exclude everything? If
        so, Beautiful Soup will issue a warning if you try to use it
        when parsing a document.

        The `ElementFilter` might turn out to exclude everything even
        if this returns `False`, but it won't exclude everything in an
        obvious way.

        The base `ElementFilter` implementation excludes *nothing*, so
        the base implementation of `excludes_everything` always
        returns `False`.
        """
        return False
    
    def allow_string_creation(self, string: str) -> bool:
        """Based on the content of a string, see whether this
        `ElementFilter` will allow a `NavigableString` object based on
        this string to be added to the parse tree.

        By default, all strings are processed into `NavigableString`
        objects. To change this, subclass `ElementFilter`.

        :param str: The string under consideration.
        """
        return True
    
    def allow_tag_creation(
        self, nsprefix: Optional[str], name: str, attrs: Optional[_RawAttributeValues]
    ) -> bool:
        """Based on the name and attributes of a tag, see whether this
        `ElementFilter` will allow a `Tag` object to even be created.

        By default, all tags are parsed. To change this, subclass
        `ElementFilter`.

        :param name: The name of the prospective tag.
        :param attrs: The attributes of the prospective tag.
        """
        return True