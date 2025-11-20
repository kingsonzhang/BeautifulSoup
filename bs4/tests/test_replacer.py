from bs4.replacer import SoupReplacer
from bs4 import BeautifulSoup

# Milestone2
def test_replacer_b_to_blockquote():
    replacer = SoupReplacer(("b", "blockquote"))
    badHTML = "<html><body><b>Test</b></body></html>"
    soup = BeautifulSoup(badHTML, "lxml", replacer=replacer)
    assert soup.encode() == b"<blockquote>Test</blockquote>"

def test_replacer_blockquote_to_b():
    replacer = SoupReplacer(("blockquote", "b"))
    badHTML = "<html><body><blockquote>Test</blockquote></body></html>"
    soup = BeautifulSoup(badHTML, "lxml", replacer=replacer)
    assert soup.encode() == b"<b>Test</b>"

def test_replacer_same_tags():
    replacer = SoupReplacer(("b", "b"))
    badHTML = "<html><body><b>Test</b></body></html>"
    soup = BeautifulSoup(badHTML, "lxml", replacer=replacer)
    assert soup.encode() == b"<b>Test</b>"

# Milestone3
def test_replacer_with_name_xformer():
    replacer = SoupReplacer(name_xformer = lambda tag: "blockquote" if tag.name == "b" else tag.name)
    badHTML = "<html><body><b>Test</b></body></html>"
    soup = BeautifulSoup(badHTML, "lxml", replacer=replacer)
    assert soup.encode() == b"<html><body><blockquote>Test</blockquote></body></html>"

def test_replacer_with_name_xformer_with_filter():
    replacer = SoupReplacer(("b", "b"), name_xformer = lambda tag: "blockquote" if tag.name == "b" else tag.name)
    badHTML = "<html><body><b>Test</b></body></html>"
    soup = BeautifulSoup(badHTML, "lxml", replacer=replacer)
    assert soup.encode() == b"<blockquote>Test</blockquote>"

def test_replacer_with_name_xformer_with_filter_empty():
    replacer = SoupReplacer(("blockquote", "blockquote"), name_xformer = lambda tag: "blockquote" if tag.name == "b" else tag.name)
    badHTML = "<html><body><b>Test</b></body></html>"
    soup = BeautifulSoup(badHTML, "lxml", replacer=replacer)
    assert soup.encode() == b""

def test_replacer_with_attrs_xformer():
    def remove_class_attr(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]
    
    replacer = SoupReplacer(xformer = remove_class_attr)
    badHTML = "<html><body><b>Test</b></body></html>"
    soup = BeautifulSoup(badHTML, "lxml", replacer=replacer)
    assert soup.encode() == b"<html><body><b>Test</b></body></html>"

def test_replacer_with_attrs_xformer_with_filter():
    def remove_class_attr(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]
    
    replacer = SoupReplacer(("b", "blockquote"), xformer = remove_class_attr)
    badHTML = "<html><body><b>Test</b></body></html>"
    soup = BeautifulSoup(badHTML, "lxml", replacer=replacer)
    assert soup.encode() == b"<blockquote>Test</blockquote>"

def test_replacer_with_attrs_xformer_with_filter_empty():
    def remove_class_attr(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]
    
    replacer = SoupReplacer(("blockquote", "blockquote"), xformer = remove_class_attr)
    badHTML = "<html><body><b>Test</b></body></html>"
    soup = BeautifulSoup(badHTML, "lxml", replacer=replacer)
    assert soup.encode() == b""