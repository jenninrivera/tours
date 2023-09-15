
from game import Game
from player import Player
from deck import Deck

if __name__ == "__main__":
    '''
    Here we'll run simulations of our game playing, then print out the win 
    rate for each player. 
    '''
    import ipdb; ipdb.set_trace()
    player1 = Player('player 1')
    player2 = Player('player 2')
    deck = Deck()
    game = Game(player1, player2, deck)
    game.play()
    for i in range(0,1000):
        deck.create_new()
        game = Game(player1, player2, deck)
        game.play()
    print(player1.win_rate())
    print(player2.win_rate())