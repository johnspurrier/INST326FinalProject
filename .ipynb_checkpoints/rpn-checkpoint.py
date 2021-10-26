from argparse import ArgumentParser
import sys


# Replace this comment with your implementations of the evaluate() and main()
# functions.
def evaluate(postfix):
    """ Evaluates a list of numbers using the Polish method 
    
    Args:
        postfix(list): the list that will be used by the function to evaluate the numbers and operators
        
    Returns: 
        nums.pop(float): evaluated list of numbers 
    
    """
    list = postfix.split()
    y = float()
    z = float()
    nums = []
    ops = []
    for x in list: 
        if(x!="+" or x!="-" or x!="*" or x!="/"):
            ops.append(x)
        else: 
            nums.append(float(x))
    while len(nums) > 1:
        y = nums.pop()
        z = nums.pop()
        w = ops.pop(0)
        if w == "+":
            answer = float(y)+float(z)
            nums.append(answer)
        if w == "-":
            answer = float(y)-float(z)
            nums.append(answer)  
        if w == "*":
            answer = float(y)*float(z)
            nums.append(answer)
        if w == "/":
            answer = float(y)/float(z)
            nums.append(answer)
    return float(nums.pop())
    
    
def main(filename):
    """ open and read the file, print and evaluate the lines
    
    Args: 
        filename(list): the file that will be read and evaluated by the function

    
    Side Effects:
        print: print the results of evaluating the lines in the file
        
    """
    File = "postfix_expressions.txt"
    with open(filename, "r", encoding="utf-8") as f: 
        for line in f: 
            print(str(line.rstrip()) + "=" + str(evaluate(line)))

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
    