import argparse
import sys
import re

class Book:
    """
    Attributes: 
        callnum(str): a string containing the book’s Library of Congress call number
        title(): a string containing the title of the book
        author(): a string containing the name of the book’s author(s); if the author is
        unknown, this should be an empty string
    """
    def __init__(self, callnum, title, author): 
        self.callnum = callnum
        self.title = title
        self.author = author 
        book1 = [callnum, title, author]
        book2 = [callnum, title, author]
    
def read_books(file): # use regular expressions to compare cutter numbers 
    with open(file, 'r', encoding='utf-8') as f: 
        for line in f: 
            line.strip()
            