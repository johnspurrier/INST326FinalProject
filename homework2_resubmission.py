from argparse import ArgumentParser
import sys

LANGUAGES = [
    # "est"
    "eus"
]

ONES = ["zero", "bat", "bi", "hiru", "lau", "bost", "sei", "zazpi", 
        "zortzi", "bederatzi", "hamar", "hamaika", "hamabi", "hamairu", "hamalau",
        "hamabost", "hamasei", "hamazazpi", "hamazortzi", "hemeretzi"]

TENS = ["", "hamar", "hogei", "hogeita hamar", "berrogei", "berrogeita hamar", 
        "hirurogei", "hirurogeita hamar", "laurogei", "laurogeita hamar"]

def eus(num):
    if num == 1: 
        return "bat"
    if num < 20: 
        return ONES[num]
    if num < 100: 
        t, o = divmod(num, 10)
        if o == 0: 
            return TENS[t]
        return f"{TENS[t]} {ONES[o]}"
    if num < 1000: 
        h, r = divmod(num, 100)
        hundreds = "ehun" if h == 1 else f"{ONES[h]} ehun"
        if r == 0: 
            return hundreds
        else: 
            return f"{hundreds} eta {eus(r)}"
    t, r = divmod(num, 1000)
    thousands = "mila" if t == 1 else f"{eus(t)} mila"
    if r == 0: 
        return thousands
    else: 
        return f"{thousands} {eus(r)}"
    
def main(basque, input_path, output_path):
    """outputs the spelling of the numbers in the input file
    
    Args: 
        est(string): the language code
        input_path(string): the file containing one number per line
        output_path(string): the output file 
        
    Raises: 
        new_list(string): the spelling of the numbers in basque
        
    Side effects: 
        print(list): list of spelled numbers
    
    """
    if basque != "eus":
        raise ValueError(f"Language isn't {basque}!")
    with open(input_path, "r", encoding="utf-8") as input_path, \
    open(output_path, "w", encoding="utf-8") as output_path:
        for line in input_path:
            x = int(line)
            print(f"{x} = {eus(x)}", file = output_path)
            
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