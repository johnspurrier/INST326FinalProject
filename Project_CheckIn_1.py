class Player: 
    """Creates the player of the card game
    
    Arrtibutes: 
        name(str):
        order(int):
    """
    def __init__(self, name, order): 
        self.name = name
        self.order = order
        
    def turn(name, card_count, order):
        card_count = 10
        if name.order == 1: 
            card_count += 1
        
            
            