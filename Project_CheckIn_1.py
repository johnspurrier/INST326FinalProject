class Player: 
    """Creates the player of the card game
    
    Arrtibutes: 
        name(str):
        order(int):
    """
    def __init__(self, name, order): 
        self.name = name
        self.order = order
        
    def turn(name, card_count, new_card, hand, order):
        card_count = 10
        if name.order == 1: 
            card_count += 1
            if new_card not in hand: 
                card_count -= 1
            return hand 
        if name.order == 2: 
            card_count += 1
            if new_card not in hand: 
                card_count -= 1
            return hand
        
    
            
        
            
            