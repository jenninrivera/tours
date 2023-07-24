
from game import Game
from player import Player
from deck import Deck
if __name__ == "__main__":
    '''
    Here we'll run simulations of our game playing, then print out the win 
    rate for each player. You'll notice that instead of coverging on a 
    50-50 win rate, it's more like a 40-60 win rate. This is a bug. 
    See if you can find it.
    '''
    player1 = Player('player 1')
    player2 = Player('player 2')
    deck = Deck()
    game = Game(player1, player2, deck)
    game.play()
    for i in range(0,1000):
        game = Game(player1, player2, deck)
        game.play()
        deck.create_new()
    print(player1.win_rate())
    print(player2.win_rate())