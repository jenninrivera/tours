



from game import Game
from player import Player
from deck import Deck

import sqlite3
get_player_by_name_query = '''
SELECT * from Player
WHERE uname = :uname;
'''
insert_player_query = '''
INSERT INTO Player(uname)
VALUES(:uname);
'''
insert_game_query = '''
INSERT INTO Game(winner, note)
VALUES(:winner, :note);
'''

insert_player_game_query = '''
INSERT INTO Player_Game(game_id, player_id)
VALUES(:game_id, :player_id);
'''
update_game_note_query = '''
UPDATE Game
SET note = :note
WHERE id = :game_id;
'''

get_all_games_for_player_query = '''
SELECT * from player 
INNER JOIN player_game ON player.id = player_id 
INNER JOIN game on game.id = game_id 
WHERE uname = :player_name;
'''




def open_db(db_name):
    db = sqlite3.connect(db_name)
    db.row_factory = sqlite3.Row
    return db


def query_db(db_name, query, args={}):
    '''
    Returns a list of dicts of column name to value
    '''
    db = open_db(db_name)
    cur = db.cursor()
    # Turn on foreign key support as per https://sqlite.org/foreignkeys.html
    cur.execute("PRAGMA foreign_keys=ON")
    cur.execute(query, args)
    id = cur.lastrowid
    rv = cur.fetchall()
    cur.close()
    db.commit()
    db.close()
    return rv,id


player1_name = input("Enter player 1's name: ")
player2_name = input("Enter player 2's name: ")
player1 = Player(player1_name)
player2 = Player(player2_name)
deck = Deck()
game = Game(player1, player2, deck)
game.play()

player1_id = 0
player2_id = 0
results,_ = query_db('games.db', get_player_by_name_query, {'uname': player1_name})
if not results:
    _, player1_id = query_db("games.db",insert_player_query, {'uname':player1.name})
else:
    player1_id = results[0]['id']
results,_ = query_db('games.db', get_player_by_name_query, {'uname': player2_name})
if not results:
    _, player2_id = query_db("games.db",insert_player_query, {'uname':player2.name})
else:
    player2_id = results[0]['id']

winner_id = player1_id if game.winner == player1.name else player2_id
print(winner_id)
_, game_id = query_db("games.db",insert_game_query, {'winner':winner_id, 'note':''})

query_db("games.db",insert_player_game_query, {'game_id':game_id, 'player_id':player1_id})
query_db("games.db",insert_player_game_query, {'game_id':game_id, 'player_id':player2_id})

note = input("Add a note to the game: ")
query_db('games.db', update_game_note_query, {'game_id':game_id, 'note':note})


