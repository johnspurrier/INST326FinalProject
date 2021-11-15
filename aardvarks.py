""" Simulate a battle between two Battle Aardvarks. """

from argparse import ArgumentParser
from os import name
from random import randint
import sys
from time import sleep


class Aardvark:
    """defines traits of the aardvark
    
    Attributes: 
        name (string): the aardvark's name 
        house (string): the aardvark's house
        hp (float): the aardvark's health points
        power (float): the aardvark's attack power
    """
    def __init__(self, name, house, hp, power): 
        """initializes the instances of each attribute 
        
        Args:
            name(string): the aardvark's name
            house(string): the aardvark's house
            hp(float): the aardvark's health points
            power(float): the aardvark's attack power
        
        """
        self.name = name
        self.house = house
        self.hp = hp
        self.power = power 
        
    def advantage(self, opponent): 
        """Returns an advantage coefficient representing the aardvark’s 
        advantage over their opponent
        
        Args: 
            opponent(str): the aardvark's opponents name 
        
        Returns: 
            advantage coefficient(int): the advantage the aardvark has over its
            opponents; constant depending on who has the advantage
        """
        if self.house == "Orange" and opponent.house == "Green": 
            return 1.25
        elif self.house == "Orange" and opponent.house == "Purple":
            return 0.8
        elif self.house == "Green" and opponent.house == "Purple":
            return 1.25
        elif self.house == "Green" and opponent.house == "Orange":
            return 0.8
        elif self.house == "Purple" and opponent.house == "Orange":
            return 1.25
        elif self.house == "Purple" and opponent.house == "Green":
            return 0.8
        else:
            return 1.0
        
    def attack(self, opponent):
        """Generates a random number (0 or 1) that determines which aardvark wins
        
        Args:
            opponent(aardvark): the name of the aardvark's opponent
            
        Side effects: 
            prints that the aardvark either wins or loses depending on the randint
        """
        random_num = randint(0,1)
        if random_num == 0:
            print(f"{self.name} fails to do damage to {opponent.name}")
        if random_num == 1: 
            damage = self.advantage(opponent) * self.power
            opponent.hp = opponent.hp - damage
            print(f"{self.name} does {damage} damage to {opponent.name}")
            
class Catalog: 
    """reads the CSV file of aardvark stats
    
    Attributes: 
        name(str): the name of the aardvark
        house(str): the aardvark's house
        hp(float): the aardvark's initial health points
        power(float): the aardvark's power
        catalog(dict): each key will be the name of an aardvark
        dict1(dict): the dictionary of all of the aardvarks
    """
    def __init__(self, stats_file): 
        """initializes the path to a file containing aardvark stats 
        
        Args:
            stats_file(str): opens the file to be read
        """
        self.catalog[self.name] = self.house, float(self.hp), float(self.power)
        self.dict1= {}
        with open(stats_file, "r", encoding="utf-8") as file:
            for line in file: 
                name, house, hp, power = line.split(",")
                self.dict1[name]= house, float(hp), float(power)
        
    
    def get_aardvark(self, name):
        """instantiates an Aardvark object with the name, house, health points, 
        and power of the aardvark specified in the second parameter
        
        Args:
            name(str): name of an aardvark in the catalog    
            
        Returns: 
            aardvark(str): name, house, hp, power of an aardvark in the catalog
            
        Raises:
            KeyError(str): key error raised if the name is not in the catalog
        """
        if name not in self.dict1:
            return KeyError("no information")
        else:
            house, hp, power = self.dict1[name]
            return Aardvark(name, house, hp, power)
    
def battle(aardvark_1, aardvark_2, pause=2.0): 
    """Battle between the two aardvarks to determine a winner
    
    Args: 
        aardvark_1(str): the first participant
        aardvark_2(str): the second partcipant
        pause(float): given a default value of 2.0
    
    Side effects: 
        prints aardvark's health points and the winners of the battles 
    """
    while aardvark_1.hp > 0 and aardvark_2.hp > 0:
        aardvark_1.attack(aardvark_2)
        print(f"{aardvark_1} has {float(aardvark_1.hp)} health points.")
        aardvark_2.attack(aardvark_1)
        print(f"{aardvark_2} has {float(aardvark_2.hp)} health points.")
        print()
        sleep(pause)
    if aardvark_1.hp <= 0 and aardvark_2.hp <= 0:
        print("The battle ends in a draw!")
    if aardvark_1.hp > aardvark_2.hp:
        winner = aardvark_1.hp
        print(f"{aardvark_1.name} wins!")
    if aardvark_1.hp < aardvark_2.hp:
        winner = aardvark_2.hp
        print(f"{aardvark_2.name} wins!")

def main(filename, a1_name, a2_name, pause=2.0):
    """ Create two aardvarks from the aardvark catalog and stage a battle.
    
    Args:
        filename (str): A file with other data.
        a1_name (str): The name of the first aardvark, taken from the file.
        a2_name (str): The name of the second aardvark, taken from the file.
        pause (float): an amount of time in seconds to pause between attacks in
            a battle. Allows the user time to read the outcome of each attack.
            Default: 2.0.
        
    Side effects:
        See battle().
    """
    catalog = Catalog(filename)
    a1 = catalog.get_aardvark(a1_name)
    a2 = catalog.get_aardvark(a2_name)
    if a1_name == a2_name:
        a1.name += " 1"
        a2.name += " 2"
    battle(a1, a2, pause)

      
def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect three mandatory arguments:
        - filename: a path to a CSV file containing aardvark stats
        - aardvark_1: the name of the first aardvark in the battle
        - aardvark_2: the name of the second aardvark in the battle

    Also allow one optional argument, which should be preceded by -p or --pause:
        - pause: the number of seconds to pause after each attack in the battle
          (defaults to 2.0)
        
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("filename",
                        help="path to CSV file containing aardvark stats")
    parser.add_argument("aardvark_1", help="name of first aardvark")
    parser.add_argument("aardvark_2", help="name of second aardvark")
    parser.add_argument("-p", "--pause", type=float, default=2.0,
                        help="pause in seconds between attacks in the battle")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename, args.aardvark_1, args.aardvark_2, pause=args.pause)
