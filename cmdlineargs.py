from argparse import ArgumentParser
import sys


class Person:
    def __init__(self, name, age, vip_status="complete peon", is_president=False):
        self.name = name
        self.age = age
        self.vip_status - vip_status
        self.is_president = is_president
        
    def __repr__(self):
        return(
            f"Person({self.name}, {self.age}, vip_status ={self.vip_status}"
            f"is president = {self.is_president}")

def main(name, age, vip_status="complete peon", is_president=False):
    print(f"{name} is {age} years old and is a {vip_status!r} within our"
          f" organization. They are {'' if is_president else ' not'} is the president")

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("name", help="name of a person")
    parser.add_argument("age", type=int, help="age of the person")
    parser.add_argument("-v", "--vip status", default= "super duper VIP",
                        help="VIP status (if any)")
    parser.add_argument("-p", "--president", action="store_true", 
                        help="indicated that the person is the president")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.name, args.age, vip_status=args.vip_status, is_president=args.is_president) 