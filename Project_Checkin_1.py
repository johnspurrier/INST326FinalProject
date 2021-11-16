SUITS = ('Club', 'Spade', 'Heart', 'Diamond')
RANK = = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
VALUE = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
'9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

def scoring_points():
    """Scores point for playes.
    Attributes:
        self
        player1
        player2
    
    """
    
    def __init__(self, player1, player2):
        """initializes Scoring class.
        
        Args:
            Player1
            PLayer2
    
        """
        p1_knock = False
        p2_knock = False
        p1_score = 0
        p2_score = 0
        self.player1 = player1
        self.player2 = player2
        
        
    def going_gin(self, player1, player2,p1_knock, p2_knock):
        """Wins the round and player who knocked scores 25 points
        
        Attributes:
            player1:
            player2:
            p1_knock:
            p2_knock:
        
        Returns:
            return score of player
        """
        if p1_knock == True and player1.hand != unmatched.cards:
            self.p1_score += 25
            return self.p1_score 
        elif p2_knock == True and  player2.hand != unmatched.cards:
            self.p2_score += 25
            return self.p2_score
           
           
    def knock_points(self, player1, player2,p1_knock, p2_knock):
        """ receives knock points for player who knocks.
        
        Attributes:
            player1:
            player2:
            p1_knock:
            p2_knock:
        
        Returns:
            return score of player
        
        """
        if p1_knock:
            p1_score = (player2.hand(deadwood)-player1.hand(deadwood))
            return p1_score
        
        elif p2_knock:
            p2_score = (player1.hand(deadwood)-player2.hand(deadwood))
            return p2_score
        
    def undercut_points(self, player1, player2,p1_knock, p2_knock):
        """receives points for player whos undercut.
        
        Attributes:
            player1:
            player2:
            p1_knock:
            p2_knock:
        
        Returns:
            return score of player
        """
        if p1_knock and player1.hand(deadwood) == player2.hand(deadwood):
            self.p2_score += 10
            return self.p2_score
            
        elif player2.knock and player2.hand(deadwood) == player1.hand(deadwood):
            self.p1_score += 10
            return self.p1_score
        
        
        
        