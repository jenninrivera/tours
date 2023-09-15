
from __future__ import annotations
import random
from card import Card
class Deck:

    def __init__(self) -> None:
        self.cards: list[Card] = []
        self.create_new()

    def create_new(self) -> None:
        '''
        The cards attribute is populated by iterating over every possible suit
        and value in a nested loop to get every combination (in other words,
        the Cartesian product of the two sets) 
        '''
        self.cards.clear()
        suits: set[str] = {"H", "D", "C", "S"}
        values: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
        for s in suits:
            for v in values:
                self.cards.append(Card(suit=s, value=v))
        self.shuffle()
    
    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        return self.cards.pop()