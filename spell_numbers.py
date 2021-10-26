"""Convert numbers from digits to words in estonian."""


from argparse import ArgumentParser
import sys


LANGUAGES = [
    # uncomment "est" below if you implement Estonian numbers,
    # or "eus" if you implement Basque numbers
    
    "est",
    # "eus",
]
dict1 = {1: "üks", 2: "kaks", 3: "kolm", 4: "neli", 5: "viis", 6: "kuus", 7: "seitse", 8: "kaheksa", 9: "üheksa", 10: "kumme"}
# dict10 = {11: "üksteist", 12: "kaksteist", 13: "kolmteist", 14: "neliteist", 15: "viisteist", 16: "kuusteist", 17: "seitseteist", 18: "kaheksatesist", 19: "üheksateist"}
dict100 = {100: "sada", 200: "kakssada", 300: "kolmsada", 400: "nelisada", 500: "viissada", 600: "kuussada", 700: "seitsesada", 800: "kaheksasada", 900: "ükehsasada"}
suffix = "teist"
sten = "kümmend"
thousand = "tuhat"

def ones(dict1):
    return dict1[ones]

def est(number):
    """A function that takes a list of numbers and spells out the words in estonian.
    
    Args: 
        number(float): a number in a list to be translated in estonian
    
    Returns: 

    
    """
    blank_list=[]
    first3 = number // 1000
    last3 = number % 1000
    
    hundreds = number // 100
    tens = number % 100 // 10
    ones = number % 100 % 10
    
    if first3 != 0:
        hundreds = first3 // 100
        tens = (first3 % 100) // 10
        ones = (first3 % 100) // 100
    if last3 != 0:
       hundreds = last3 //100 
       tens = (last3 % 100) // 10
       ones = (last3 % 100) // 100
    
    if number > 10:
        blank_list.append(dict1[0])
    
    return " ".join(blank_list)
        
    
def main(estonian, input_path, output_path):
    """outputs the spelling of the numbers in the input file
    
    Args: 
        est(string): the language code
        input_path(string): the file containing one number per line
        output_path(string): the output file 
        
    Raises: 
        new_list(string): the spelling of the numbers in estonian 
        
    Side effects: 
        print(list): list of spelled numbers
    
    """
    if estonian != "est":
        raise ValueError(f"Language isn't {estonian}!")
    with open(input_path, "r", encoding="utf-8") as input_path, \
    open(output_path, "w", encoding="utf-8") as output_path:
        for line in input_path:
            x = int(line)
            print(f"{x} = {est(x)}", file = output_path)
    
    

def parse_args(arglist):
    """Parse command-line arguments.
    
    Three arguments are required, in the following order:
    
        lang (str): the ISO 639-3 language code of the language the user wants
            to convert numbers into.
        input_file (str): path to a file containing numbers expressed as digits.
        output_file (str): path to a file where numbers will be written as words
            in the target language.

    Args:
        arglist (list of str): list of command-line arguments.

    Returns:
        namespace: the parsed arguments as a namespace. The following attributes
        will be defined: lang, input_file, and output_file. See above for
        details.
    """
    parser = ArgumentParser()
    parser.add_argument("lang", help="ISO 639-3 language code")
    parser.add_argument("input_file", help="input file containing numbers")
    parser.add_argument("output_file", help="file where output will be stored")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.lang, args.input_file, args.output_file)
