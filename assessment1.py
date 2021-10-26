from argparse import ArgumentParser
import sys


def n_letter_words(filename, desired_length):
    """Takes a list of words and returns each word with a specific character count
    
    Args: 
        line(string): the word that the function will take the length of and return 
        desired_length(int): the desired length of the word to be returned
    
    Side effects: 
        print word(string): the word of the desired character length
    
    """
    with open(filename, 'r', encoding='utf-8') as f:  
        for line in f:       
            for word in line.split():
                if len(word) == 5:        
                    print(word) 
            
def parse_args(arglist):
    """Parse command line arguments
    
    This script expects one or more text files 
    as arguments. 
    
    Args:
        arglist(list or str): arguments from the command line
        
    Returns:
        namespace: the parsed arguments. will have an attribute 
        called files and another attribute called ngram_length.
    """
    parser = ArgumentParser()
    parser.add_argument()
    parser.add_argument()
    return parser.parse_args(arglist)


n_letter_words("assessment1.txt", 5)