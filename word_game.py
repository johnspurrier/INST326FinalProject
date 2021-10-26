"""Compute a team's score for a (fictitious) word game.

In this game, two players independently find words in a matrix of letters.
Each player's words are added to a text file with one word per line. Duplicates
are removed from each player's list. For each word that appears on both players'
lists, the team's score increases by the number of letters in the word minus 2
(words less than three characters long are not worth any points).
"""


from argparse import ArgumentParser
import sys


# Replace this comment with your implementation of the PlayerWords class and the
# main() function
"""Compute a team's score for a (fictitious) word game.

In this game, two players independently find words in a matrix of letters.
Each player's words are added to a text file with one word per line. Duplicates
are removed from each player's list. For each word that appears on both players'
lists, the team's score increases by the number of letters in the word minus 2
(words less than three characters long are not worth any points).
"""

class PlayerWords:
    def __init__(self, f1):
        self.f1 = f1
        words = set()
        with open(f1, "r", encoding="utf-8") as f:
            for line in f:
                words.add(line.strip())
            self.words = words
                
    def score(self, partner):
        total = self.words & partner.words
        scr = set()
        for word in total:
            if len(word) <= 3:
                scr.add(word)
        return len(scr)
    
def main(f1, f2):
    p1 = PlayerWords(f1)
    p2 = PlayerWords(f2)
    score = p1.score(p2)
    print(f"Your team scored {score} points!")

def parse_args(arglist):
    """Parse command line arguments.
    
    Expect two mandatory arguments:
        - str: path to a text file containing words found by player 1.
        - str: path to a text file containing words found by player 2.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.

    """
    parser = ArgumentParser()
    parser.add_argument("wordfile1", help="file containing player 1's words")
    parser.add_argument("wordfile2", help="file containing player 2's words")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.wordfile1, args.wordfile2)
