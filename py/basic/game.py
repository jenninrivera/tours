import random






def make_deck() -> list[dict]:
    '''
    The cards attribute is populated by iterating over every possible suit
    and value in a nested loop to get every combination (in other words,
    the Cartesian product of the two sets) 
    '''
    deck: list[dict] = []
    suits: set[str] = {"H", "D", "C", "S"}
    values: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
    for s in suits:
        for v in values:
            deck.append({"suit": s, "value": v})
    return deck

def shuffle_deck(deck) -> None:
    random.shuffle(deck)


def deal(deck) -> tuple[list[dict], list[dict]]:
    '''
    count from 0 to n, where n is the length of the number of 
    cards in the deck. if the number is even, deal a card to 
    player one, else deal a card to player 2
    '''
    player1_hand: list[dict] = []
    player2_hand: list[dict] = []
    for i in range(0, len(deck)):
        if i % 2 == 0:
            player1_hand.append(deck[i])
        else:
            player2_hand.append(deck[i])
    return (player1_hand, player2_hand)

def play_game(player1_hand: list[dict], player2_hand: list[dict]) -> str:
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
    player1_score = 0
    player2_score = 0
    while len(player1_hand) != 0 and len(player2_hand) != 0:
        player1_card = player1_hand.pop()
        player2_card = player2_hand.pop()
        if player1_card["value"] > player2_card["value"]:
            player1_score += 1
        elif player2_card['value'] > player1_card['value']:
            player2_score += 1
        else:
            if player1_card['suit'] > player2_card['suit']:
                player1_score += 1
            else:
                player2_score += 1
    if player1_score > player2_score:
        return "Player 1 wins!"
    elif player2_score > player1_score:
        return "Player 2 wins!"
    else:
        coin = ['HEADS', 'TAILS']
        if random.choice(coin) == 'HEADS':
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"

def get_total_value_of_hand(hand: list[dict]) -> int:
    card_values: list[int] = [card["value"] for card in hand]
    return sum(card_values)


deck: list[dict] = make_deck()
shuffle_deck(deck)
player1_hand, player2_hand = deal(deck)
print(f"value of Player 1's deck: {get_total_value_of_hand(player1_hand)}")
print(f"value of Player 2's deck: {get_total_value_of_hand(player2_hand)}")
result = play_game(player1_hand, player2_hand)
print(result)