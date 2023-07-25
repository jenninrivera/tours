
from __future__ import annotations

class Card:

    def __init__(self, suit: str, value: int) -> None:
       self.suit = suit
       self.value = value 

    @property
    def suit(self) -> str:
        return self._suit

    @suit.setter
    def suit(self, suit: str) -> None:
        '''
        The suit property setter enforces that the parameter is in the 
        set of suit letters.
        '''
        if suit not in {'S', 'D', 'C', 'H'}:
            raise ValueError("Suit must be 'S', 'D', 'C', or 'H'")
        self._suit = suit
        
    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        '''
        The value property setter enforces that the parameter is a legal card value
        '''
        if value < 1 or value > 13:
            raise ValueError("card value must be between 1 and 13, inclusive") 
        self._value = value 

    def beats(self, card: Card) -> bool:
        '''
        The current card (i.e. self) beats the challenging card if the value 
        is higher. If the values are the same, we check the suit and the 
        letter that is higher alphabetically wins (so _S_pades beats _C_lubs)
        '''
        if self.value == card.value:
            return self.suit > card.suit
        return self.value > card.value
