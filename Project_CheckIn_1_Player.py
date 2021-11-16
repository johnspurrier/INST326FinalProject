class Player: 
    """Creates the player of the card game
    
    Arrtibutes: 
        name(str):
        order(int):
        cards - array of cards
    """
    def __init__(self, name, order, cards): 
        self.name = name
        self.order = order
        self.cards = cards
        self.card_count = 10
        
        
    def turn(self, new_card):
        # search through the array of cards to see if the new card is the same suit or number
        for card in self.cards:
            if new_card.suit == card.suit or new_card.value == card.value:
                self.card_count += 1
                self.cards.append(card) 
                self.remove_card()
                return 
         
    # there should be 11 cards in the hand at this time, and the least valuable card will
    # be dropped    
    def remove_card(self):
        self.cards.pop(0)
            
    # def turn(self, player, new_card, hand, order):
    #     if player.order == self.order: 
    #         self.card_count += 1
    #         if new_card not in hand: 
    #             self.card_count -= 1
    #         return hand 
    #     if player.order == 2: 
    #         self.card_count += 1
    #         if new_card not in hand: 
    #             self.card_count -= 1
    #         return hand
        
    
            
        
            
            
