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
        expr = r"[A-Z]{1,3}\d{1,4}(\.?)(\d{1,4})?(\s?\.?\w?\d+)\s\d{1,4}"
    # First section: ([A-Z]{1,3})
    # Second section: (\d{1,4}(\.?)(\d{1,4})?)
    # Third section: (\s?\.?\w?\d+)\s
    # Fourth section: \d{1,4}
        match = re.search(expr,)
        if match == None:
            raise ValueError("Address cannot be parsed")
        else:
            self.callnum = callnum
            self.no1 = match.group(1)
            self.no2 = match.group(2)
            self.no3 = match.group(3)
            self.no4 = match.group(4)
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
    
def read_books(file):
    with open(file, 'r', encoding='utf-8') as f: 
        numlist = [Book(callnum)for callnum in f]
        return numlist.strip()
            
            
def main(file): 
    file.sort()
    return 
    
def parse_args(list1):
    return 

if __name__ == "__main__":
    main()
    
    
    
            