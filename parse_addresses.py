from argparse import ArgumentParser
import re
import sys


class Address: 
    """A class for parsing a list of addresses
    
    Attributes:
        line(str): a line in the list of addresses
        filepath(list of str): the file containing the list of addresses
    """
    def __init__(self,line):
        """Initializes the address object
        
        Args:
            line(str): a line in the list of strings
            
        Raises:
            ValueError: address cannot be parsed
            
        Side effects: 
            matches the addresses in the list using the regular expression
        
        """
        expr = r"(^\S+) ([^,]+), (.+) ([A-Z]{2}) (\d{5})"
        match = re.search(expr,line)
        if match == None:
            raise ValueError("Address cannot be parsed")
        else:
            self.address = line
            self.house_number = match.group(1)
            self.street = match.group(2)
            self.city = match.group(3)
            self.state = match.group(4)
            self.zip = match.group(5)
        
    def __repr__(self):
        """Return a formal representation of the Address object."""
        return (
            f"address:      {self.address}\n"
            f"house number: {self.house_number}\n"
            f"street:       {self.street}\n"
            f"city:         {self.city}\n"
            f"state:        {self.state}\n"
            f"zip:          {self.zip}"
        )
        
def read_addresses(filepath):
    """Opens and reads the file containing the addresses and returns
    them as a list
    
    Args: 
        filepath(list of str): the file containing the list of addresses
        
    Returns: 
        addresslist(list of str): the list of addresses sorted by 
        individual components of house number, street, city, state, zip
    """
    with open(filepath,"r",encoding = 'utf-8') as f:
        addresslist = [Address(address) for address in f]
        return addresslist
      

def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory argument, the path to a file of addresses.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with one attribute, file, containing a string.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing one address per line")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for address in read_addresses(args.file):
        # the !r tells the f-string to use the __repr__() method to generate
        # a string version of the address object
        print(f"{address!r}\n")
