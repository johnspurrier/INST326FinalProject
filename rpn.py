from argparse import ArgumentParser
import sys


# Replace this comment with your implementations of the evaluate() and main()
# functions.
def evaluate(postfix):
    """computes a list of numbers using the Polish method 
    
    Args:
        postfix(string): the list that will be used by the function to evaluate the numbers and operators
        
    Returns: 
        nums.pop(float): evaluated list of numbers 
    """

    
    list = postfix.split()
    nums = []
    ops = []
    for x in list: 
        if(x=="+" or x=="-" or x=="*" or x=="/"):
            ops.append(x)
        else: 
            nums.append(float(x))
    while len(nums) > 1:
        y = nums.pop()
        z = nums.pop()
        w = ops.pop(0)
        if w == "+":
            answer = float(z)+float(y)
            nums.append(answer)
        elif w == "-":
            answer = float(z)-float(y)
            nums.append(answer)  
        elif w == "*":
            answer = float(z)*float(y)
            nums.append(answer)
        elif w == "/":
            answer = float(z)/float(y)
            nums.append(answer)
    return float(nums.pop())
                   
    
def main(file):
    """Opens the file, strips it line by line, reads the file, prints and evaluates the lines as it iterates through
    
    Args: 
        file(string): the file that will be read and evaluated by the function

    
    Side Effects: 
        Prints the postfix espression and the result of the evaluate() function    
    """
    with open(file, "r", encoding= "utf-8") as file: 
        for line in file: 
            line = line.strip()
            answer = evaluate(line)
            print(f'{line} = {answer}') 

def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a file containing postfix expressions).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing reverse polish notation")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
  
