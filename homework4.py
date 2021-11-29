import argparse
import sys
import re

class Book:
    """
    Attributes: 
        callnum(str): a string containing the book’s Library of Congress call number
        title(str): a string containing the title of the book
        author(str): a string containing the name of the book’s author(s); if the author 
        is unknown, this should be an empty string
    """
    def __init__(self, callnum, title, author): 
        self.callnum = callnum
        self.title = title
        self.author = author 
    
    def __repr__(self): 
      print(f"Book{self.callnum!r}, {self.title!r}, {self.author!r}")
    
    def __lt__(self, other):
        if self < other:
            return True
        else: 
            return False
        
    def __gte__(self, other): 
        if self >= other:
            return True
        else: 
            return False
    
def read_books(file): # use regular expressions
    with open(file, 'r', encoding='utf-8') as f: 
        for line in f: 
            line.strip()
            
def main(file): 
    return 
    
def parse_args(list1):
    return 

if __name__ == "__main__":
    main()
    
    
            