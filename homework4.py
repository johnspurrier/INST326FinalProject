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
        expr1 = re.compile("[A-Z]{1,3}")
        expr2 = re.compile("\d{1,4}(\.?)(\d{1,4})?")
        expr3 = re.compile("(\s?\.?\w?\d+)\s")
        expr4 = re.compile("\d{1,4}")
    # First section: ([A-Z]{1,3})
    # Second section: (\d{1,4}(\.?)(\d{1,4})?)
    # Third section: (\s?\.?\w?\d+)\s
    # Fourth section: \d{1,4}
        self.no1 = expr1.match(self.callnum)
        self.no2 = expr2.match(self.callnum)
        self.no3 = expr3.match(self.callnum)
        self.no4 = expr4.match(self.callnum)
        # if not match:
        #     raise ValueError("Address cannot be parsed")
        # else:
        # self.no1 = match1.group(1)
        # self.no2 = match2.group(1)
        # self.no3 = match3.group(1)
        # self.no4 = match4.group(1)
        return (self.no1, self.no2, self.no3, self.no4)
        
    def __repr__(self): 
        """the formal representation of the book object
        
        Side effects: 
            prints out the formal representation
        """
        to_return = "Book(" + "\'" + self.callnum + "\', " + "\"" + self.title + "\", "  "\'" + self.author + "\')" 
        return to_return
    
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
    
    
    
            