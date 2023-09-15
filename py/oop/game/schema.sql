

DROP TABLE IF EXISTS Game;
CREATE TABLE Game(
    id INTEGER PRIMARY KEY autoincrement,
    winner INTEGER NOT NULL,
    note TEXT NOT NULL,
    FOREIGN KEY (winner) REFERENCES Player(id)
);


DROP TABLE IF EXISTS Player;
CREATE TABLE Player(
    id INTEGER PRIMARY KEY autoincrement,
    uname  TEXT NOT NULL
);


DROP TABLE IF EXISTS Player_Game;
CREATE TABLE Player_Game(
    player_id INTEGER NOT NULL,
    game_id INTEGER NOT NULL,

    FOREIGN KEY (player_id) REFERENCES Player(id),
    FOREIGN KEY (game_id) REFERENCES Game(id)
)

