"""Generate random text based on training data.
"""

from argparse import ArgumentParser
import random 
import sys

class TextGenerator:
    """A generator of random texts.
    
    Attributes:
        ngrams(dict of (tuple of str): set of str): language model. each key 
        is a sequence of words; each value is a set of individual words that have
        been observed to follow the words in the key.
    """
    def __init__(self, files):
        self.ngrams = dict()
        self.ngram_length = ngram_length
        for filename in files: 
            self.add_file(filename)
            
    def add_file(self, filename): 
        with open(filename, 'r', encoding='utf-8') as f: 
            for line in f:
               text = f.read()
               words = re.findall(r"\S+", text) 
               for i in range(len(words) - (self.ngram_length)):
                   ngram = words[i:i+self.ngram_length]
                   if ngram not in self.ngrams: 
                       self.ngrams[ngram] = set()
                       self.ngrams[ngram].add(words[i+self.ngram_length])
                    
                    
    def generate_text(self, start=("It", "is", "a", "truth"), length=600):
        text = list(start)
        while len(text) < length:
            key = tuple(text[-self.ngram_length:])
            word = random.choice(list(self.ngrams[key]))
            text.append(word)
        return " ".join.text
        

def main(files, ngram_length):
    tg = TextGenerator(files, ngram_length=ngram_length)
    text = tg.generate_text()
    print(text)

def parse_args(arglist):
    """Parse command line arguments
    
    This script expects one or more text files 
    as arguments. it also allows an optional argument, -n, to specify n-gram length.
    
    Args:
        arglist(list or str): arguments from the command line
        
    Returns:
        namespace: the parsed arguments. will have an attribute 
        called files and another attribute called ngram_length.
    """
    parser = ArgumentParser()
    parser.add_argument("files", nargs="+", help="text files to use as training data")
    parser.add_argument("-n", "--ngram_length", type=int, default=2, help="length of n-grams to use")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.files)
    

    
    