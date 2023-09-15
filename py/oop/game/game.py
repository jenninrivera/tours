
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from deck import Deck
    from player import Player
    from card import Card

import random
class Game:

    def __init__(self, p1: Player, p2: Player, deck: Deck) -> None:
        self.player1: Player = p1
        self.player2: Player = p2
        self.deck: Deck = deck
        self.game_over: bool = False
        self.winner: Player | None = None

        self.player1.games.append(self)
        self.player2.games.append(self)

    

    def deal(self) -> None:
        '''
        count from 0 to n, where n is the length of the number of 
        cards in the deck. if the number is even, deal a card to 
        player one, else deal a card to player 2
        '''
        assert len(self.deck.cards) == 52, "Deck was not refreshed"
        for i in range(0, len(self.deck.cards)):
            if i % 2 == 0:
                self.player1.hand.append(self.deck.deal_card())
            else:
                self.player2.hand.append(self.deck.deal_card())
    
    def play(self) -> None:
        '''   
        Rules of the game:
        - Each player gets 26 cards
        - A round consists of each player comparing the top
        card of their deck. The player with the higher 
        value wins the round and gets a point. If the values
        are the same then the suit is compared and the highest
        by alphabetical order wins.
        - After all cards have been played, the player with
        the higher score wins
        - If there is a draw, a coin is flipped. If heads player
        one wins, if tails player two wins.
        '''
        self.deal()
        if self.winner == None:
            player1_score: int = 0
            player2_score: int = 0
            assert len(self.player1.hand) == len(self.player2.hand)
            while self.player1.has_cards() and self.player2.has_cards():
                player1_card: Card = self.player1.play_card()
                player2_card: Card = self.player2.play_card()
                if player1_card.beats(player2_card):
                    player1_score += 1
                elif player2_card.beats(player1_card):
                    player2_score += 1
            if player1_score > player2_score:
                self.winner = self.player1
            elif player2_score > player1_score:
                self.winner = self.player2
            else:
                coin = ['HEADS', 'TAILS']
                if random.choice(coin) == 'HEADS':
                    self.winner = self.player1
                else:
                    self.winner = self.player2