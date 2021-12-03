from argparse import ArgumentParser
import sys
import re

class Book:
    """
    Attributes: 
        callnum(str): a string containing the book’s Library of Congress call number
        title(str): a string containing the title of the book
        author(str): a string containing the name of the book’s author(s)
    """
    def __init__(self, callnum, title, author): 
        """initializes the book object
        
        Args: 
            callnum(str): a string containing the book’s Library of Congress call number
            title(str): a string containing the title of the book
            author(str): a string containing the name of the book’s author(s)
        """
        self.callnum = callnum
        self.title = title
        self.author = author 
    
    def less_than(self): 
        """the method to compare two books
        
        Args: 
            expr(regex): regular expression to sort through the call numbers and 
            compare the books
            
        Returns:
            self.no1, self.no2, self.no3, self.no4
        """
        expr = r"[A-Z]{1,3}\d{1,4}(\.?)(\d{1,4})?(\s?\.?\w?\d+)\s\d{1,4}"
    # First section: ([A-Z]{1,3})
    # Second section: (\d{1,4}(\.?)(\d{1,4})?)
    # Third section: (\s?\.?\w?\d+)\s
    # Fourth section: \d{1,4}
        match = re.search(expr, self.callnum)
        if match == None:
            raise ValueError("Address cannot be parsed")
        else:
            self.no1 = match.group(1)
            self.no2 = match.group(2)
            self.no3 = match.group(3)
            self.no4 = match.group(4)
        return (self.no1, self.no2, self.no3, self.no4)
        
    def __repr__(self): 
        """the formal representation of the book object
        
        Side effects: 
            prints out the formal representation
        """
        print(f"Book{self.callnum!r}, {self.title!r}, {self.author!r}")
    
    def __lt__(self, other):
        """less than method compares the call numbers 
        
        Args:
            other(book object): the book being compared 
            
        Returns:
            True or False 
        """
        if self.less_than() < other.less_than():
            return True
        else: 
            return False
    
def read_books(file):
    """opens and reads the filepath containing the books and returns them as a list
    
    Args:
        file(list of str): the file containing the title, author and callnums
        
    Returns:
        list1(list): the list of books
    """
    list1 = []
    with open(file, 'r', encoding='utf-8') as f: 
        for line in f:
            title, author, callnum = line.strip("\n").split("\t")
            list1.append(Book(callnum, title, author))
        return list1
            
            
def main(file): 
    """reads and sorts the books file
    
    Args:
        file(list of str): the file containing the title, author and callnums
        
    Side effects: 
        Prints the sorted books 
    """
    books = read_books(file)
    for book in sorted(books):
        print(book)
           
def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory argument, the path to a file of addresses.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with one attribute, file, containing a string."""
    parser = ArgumentParser(arglist)
    parser.add_argument("filename", help="file containing book information")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)
    
    
    
            