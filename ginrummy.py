from random import shuffle

winner = None
playing = True
current_player = None


def mk_card(s, index_of_card):
    """displays in the cards in the player's hands
    
    source:
        the below class to display each card is based of the code found on
        https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards """
    
    hand_display = [] 
    hand_display.append("┌─────────┐")
    hand_display.append(f"│{s.name}{' ' if len(s.name) < 2 else ''}. . . .│")
    hand_display.append("│. . . . .│")
    hand_display.append("│. . . . .│")
    hand_display.append(f"│. . {s.suit} . .│")
    hand_display.append("│. . . . .│")
    hand_display.append("│. . . . .│")
    hand_display.append(f"│. . . .{' ' if len(s.name) < 2 else ''}{s.name}│")
    hand_display.append("└─────────┘")
    hand_display.append(f"Card #{index_of_card}")
    return hand_display

    

class Card:
    """ A single Card.
    Attributes:
        value (int): the value of a card between 2 and 14, inclusive.
        suit (str): a string representation of hte suit of the card.
    """

    def __init__(self, value, suit):
        """ Initializes a card object
        Side Effects:
            Sets the suit, value, and name attributes.
        """
        self.value = value
        self.suit = suit
        self.name = str(value) if value < 11 and value > 1 \
            else "J" if value == 11 \
            else "Q" if value == 12 \
            else "K" if value == 13 \
            else "A"

    def __str__(self):
        """ Creates string representation of the object.
        Returns:
            (str): a string representaiton of the object as name, suit.
        """
        return f"{self.name} of {self.suit}"


class Deck:
    """ A deck of cards.
    Attributes:
        cards (list): a list of card objects.
    """

    def __init__(self):
        """ Initializes a deck object.
        Side Effects:
            Sets the card attribute and randomizes the list of cards in the list.
        """
        # Creates a list of card objects from 2-14, inclusive, and does so for each suit.
        self.cards = [Card(value, suit) for value in range(
            1, 14) for suit in ['♠', '♦', '♥', '♣']]
        shuffle(self.cards)

    def draw(self):
        """ Draws a card from the deck.
        Returns:
            remaining cards
        Raises:
            RuntimeError: Raised if the deck is empty.
        """
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            raise RuntimeError("The deck is empty.")


class Hand:
    """displays the players hand
    Attributes: 
        cards: players cards
    """
    def __init__(self, cards):
        self.cards = cards
        self.runs = list()
        self.sets = list()
        # put all cards into the deadwood list and then check for runs and sets.
        # the leftover cards will be deadwoods.

    # we will check the hand each turn to see if they have gin,
    # only check the other stuff when they knock.
    # we also calculate the number of deadwood cards each turn

    # check for runs
    def get_runs(self):
        """sorts hand to determiene runs"""
        
        run_possible = True
        # sort the cards by value, value will not be the same as score.

        while run_possible:
            run_hand = sorted(self.cards, key=lambda card: (card.suit, card.value))

            run_exists = False
            run_length = 0
            index_run_starts = 0
            # for card in run_hand:
            #     print(card.value, card.suit)
            # go through each card in the sorted hand and see if they are in order.
            for i, card in enumerate(run_hand[:-2]):
                if (card.value + 1 == run_hand[i+1].value and card.suit == run_hand[i+1].suit) and \
                        (card.value + 2 == run_hand[i+2].value and card.suit == run_hand[i+2].suit):
                    index_run_starts = i
                    run_length = 3
                    run_exists = True
                    # these cards are a run
                    # check if there are more cards in this run
                    # first check if this is possible
                    if i+2 != len(run_hand)-1:
                        # there can be more cards in the run, check for that
                        for j, card in enumerate(run_hand[index_run_starts+run_length:]):
                            if run_hand[j].value == run_hand[index_run_starts+i + j].value + 1:
                                run_length += 1
                else:
                    run_possible = False

            if run_exists:
                self.runs.append(
                    run_hand[index_run_starts:index_run_starts + run_length])
                del self.cards[index_run_starts: index_run_starts + run_length]
                return True
        return False

    def get_sets(self):
        """sorts hand to determine runs"""
        
        set_possible = len(self.cards) >= 3

        while set_possible:
            set_hand = sorted(self.cards, key=lambda card: card.value)

            set_exists = False
            set_length = 0
            index_set_starts = 0

            # go through each card in the sorted hand and see if they are in order.
            for i, card in enumerate(set_hand[:-2]):

                if (card.value == set_hand[i+1].value) and (card.value == set_hand[i+2].value):
                    index_set_starts = i
                    set_length = 3
                    set_exists = True
                    # these cards are a run
                    # check if there are more cards in this run
                    if i+3 < len(set_hand):
                        if (card.value == set_hand[i+3].value):
                            set_length += 1

                else:
                    set_possible = False

            if set_exists:
                self.sets.append(
                    set_hand[index_set_starts:index_set_starts + set_length])
                del self.cards[index_set_starts: index_set_starts + set_length]
                return True
        return False

    def check_gin(self):
        """Checks number of remaining deadwood cards for winner possibility"""
        
        global current_player
        if len(self.cards) == 0:
            current_player.wins()
        return False

    def check_hand(self):
        # check for runs
        self.runs = list()
        self.get_runs()

        # check for sets
        self.sets = list()
        self.get_sets()

        # check for gin
        self.check_gin()


class Player:
    """Player class
    
    Attibutes:
        name: name of player
        
    """
    def __init__(self, name):
        self.is_dealer = False
        self.name = name

    def wins(self):
        """prints player name which wins
        
        Side effects:
            Prints the name of the winner
        """
        global playing
        playing = False
        print(f"{self.name} wins!")

    def turn(self, deck):
        # draw a card
        # add the drawn card to their hand
        self.hand.cards.append(deck.draw())
        print(f"{self.name} it is your turn.")
        # show the player their hand
        hand_list = list()

        for card_list in self.hand.runs:
            for card in card_list:
                hand_list.append(card)

        for card_list in self.hand.sets:
            for card in card_list:
                hand_list.append(card)
        for card in sorted(self.hand.cards, key=lambda card: (card.suit, card.value)):

            hand_list.append(card)

        print('\n'.join(map('  '.join, zip(*(mk_card(c, i) for i, c in enumerate(hand_list))))))

        # get card user wants to discard
        while True:
            try:
                response = int(input('Select a card to discard '))
                if not len(str(response)) == 1:
                    print('Sorry, please enter a valid option.')
                    continue
                if response < 0 or response > 7:
                    print('Sorry, please enter a valid option.')
                    continue
            except (ValueError, TypeError):
                print('Sorry, please enter a valid option.')
                continue
            else:
                break
        # delete that card from their hand
        del hand_list[response]
        # recheck hand
        self.hand.cards = hand_list
        self.hand.check_hand()


class Game:
    """Game Class - Models a single Game 
    
    Attributes:
        Player 1: name of first player
        Player 2: name of second player
     
    """
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.deck = Deck()

    def deal(self):
        """deals  cards to each player"""
        first_set_cards = []
        second_set_cards = []
        for i in range(14):
            if i % 2 != 0:
                first_set_cards.append(self.deck.draw())
            else:
                second_set_cards.append(self.deck.draw())

        self.player1.hand = Hand(first_set_cards)
        self.player2.hand = Hand(second_set_cards)

    def play(self):
        """Plays the game"""
        global current_player
        global playing
        current_player = self.player1
        self.player1.hand.check_hand()
        self.player2.hand.check_hand()
        while playing:
            current_player.turn(self.deck)
            current_player = self.player1 if current_player != self.player1 else self.player2


def main():
    """runs the entire game"""
    player1_name = input('Player 1, enter your name: ')
    player2_name = input('Player 2, enter your name: ')

    player1 = Player(player1_name)
    player2 = Player(player2_name)
    # start a game
    game = Game(player1, player2)
    # deal
    game.deal()
    game.play()


main()
