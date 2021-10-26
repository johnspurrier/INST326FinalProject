import sys
__file__

from sys import ArgumentParser
def print_args():
    print(sys.argv)

def get_name():
    print(__name__)
 
def parse_args(argslist):   
    parser = ArgumentParser()
    parser.add_argument("file1", help="the first file")
    parser.add_argument("num", type=int, help="a number")
    parser.add_argument("-p", "--power", type=float, help="the power", default=1)
    parser.add_argument("-v", "--verbose", action="store_true", help="store verbose output")
    return parser.parse_args(argslist)

if __name__ == "__main__":
   args = parse_args(sys.argv[1:])
   print(args)
  
    
