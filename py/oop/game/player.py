from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game
    from card import Card


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand: list[Card] = []
        self.games: list[Game] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        '''
        The name property setter enforces a length of at least 1
        '''
        if len(name) < 1:
            raise ValueError("player's name must have at least one character")
        self._name = name

    def has_cards(self) -> bool:
        return len(self.hand) > 0

    def win_rate(self) -> float:
        '''
        The win rate is the number of games won divided by the total number of games played
        '''
        games_played: int = len(self.games)
        won_games: list[Game] = [game for game in self.games if game.winner == self]
        return len(won_games) / games_played

    def play_card(self) -> Card:
        if not self.has_cards():
            raise ValueError('cannot play card from empty hand')
        return self.hand.pop()
