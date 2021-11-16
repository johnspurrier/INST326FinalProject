
SUITS = ["Diamond", "Heart", "Spade","Club"]
VALUES = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
CARD_VALUES = {'2':2, '3':3, '4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}


class Card():
    """Class representing a playing card
    
    Attributes:
        suit(str): a string representing the suit of a card
        value(str): a string representing the value of the card
    """
    
    def __init__(self,suit,value):
        """Initializes a card object"""
        self.suit= suit.strip()
        self.value = value
        
    def __str__(self):
        """String representation of a card
        
        Returns:
            string representation of a card
        """
        return self.suit + self.value
        
    def get_value(self):
        """Retrieve the number value corresponding to the value of the card
        
        Returns:
            int representing number value of card
        """
        return CARD_VALUES.get(self.value)
    
    def same_suit(self,other):
        """Determines whether two cards are the same suit
        
        Args:
            other(Card): the card being compared
            
        Returns:
            boolean: true or false dependent on if the cards have the same suit"""
        if self.suit == other.suit:
            return True
        else: 
            return False
        
    def same_value(self,other):
        """Determines whether two cards are the same value
        
        Args:
            other(Card): the card being compared
            
        Returns:
            boolean: true or false dependent on if the cards have the same value"""
        if self.get_value() == other.get_value():
            return True
        else: 
            return False
        
    def same_card(self,other):
        """Determines whether two cards are the same card
        
        Args:
            other(Card): the card being compared
            
        Returns:
            boolean: true or false dependent on if the cards are the same"""
        if self.get_value() == other.get_value() and self.suit == other.suit:
            return True
        else: 
            return False
        
    def possible_straight(self,other):
        """Determines whether two cards can be part of the same straight
        
        Args:
            other(Card): the card being compared
            
        Returns:
            boolean: true or false dependent on if the cards can be part of the same straight"""
        if self.get_value() > other.get_value() and self.same_suit(other)==True:
            if self.get_value() % other.get_value() == 1:
                return True
            else:
                return False
        elif other.get_value() > self.get_value() and self.same_suit(other)==True:
            if other.get_value() %self.get_value() == 1:
                return True
            else:
                return False
        else: 
            return False
                
        
        
card1 = Card("Diamond",'5')
print(card1)
card2 = Card("Spade",'10')
print(card2)
card3 = Card("Spade",'J')
print(card3)
if card1.same_value(card2)==True:
    print("Card 1 and 2 have the same value")
else: 
    print("Card 1 and 2 do not have the same value")
if card3.possible_straight(card2) == True:
    print("Card 2 and 3 could be part of the same straight")
else:
    print("Cards 2 and 3 could not be part of the same straight")

                
                
    

    


                
    
