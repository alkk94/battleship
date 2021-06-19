from random import randint
from flask import Flask, render_template

app = Flask(__name__)


def init_board(size: int):
    return [[0 for _ in range(size)] for _ in range(size)]


def init_legal_coordinates(size: int):
    return [(i, j) for i in range(size) for j in range(size)]


def legal_place_for_ship(legal_coordinates, start_coordinates, ship_kind, direction) -> bool:
    if direction == 0:
        for i in range(1, ship_kind):
            if (start_coordinates[0], start_coordinates[1] + i) not in legal_coordinates:
                return False
    else:
        for i in range(1, ship_kind):
            if (start_coordinates[0] + i, start_coordinates[1]) not in legal_coordinates:
                return False
    return True


def set_game_board(game_board, numbers_battleships, legal_coordinates):
    for ship_kind, nr_ships in numbers_battleships.items():
        for _ in range(nr_ships):
            start_coordinates = legal_coordinates[randint(0, len(legal_coordinates) - 1)]
            direction = randint(0, 1)
            while not legal_place_for_ship(legal_coordinates, start_coordinates, ship_kind, direction):
                start_coordinates = legal_coordinates[randint(0, len(legal_coordinates) - 1)]
                direction = randint(0, 1)
            if direction == 0:
                for i in range(0, ship_kind):
                    legal_coordinates.remove((start_coordinates[0], start_coordinates[1] + i))
                    game_board[start_coordinates[0]][start_coordinates[1] + i] = 1
            else:
                for i in range(0, ship_kind):
                    legal_coordinates.remove((start_coordinates[0] + i, start_coordinates[1]))
                    game_board[start_coordinates[0] + i][start_coordinates[1]] = 1


@app.route('/')
def home():
    numbers_battleships = {
        5: 1,
        4: 1,
        3: 1,
        2: 1,
        1: 1
    }
    table_size = 8
    game_board = init_board(table_size)
    legal_coordinates = init_legal_coordinates(table_size)
    set_game_board(game_board, numbers_battleships, legal_coordinates)

    return render_template('home.html', table_size=table_size, str=str, game_board=game_board)


if __name__ == '__main__':
    app.run(debug=True)
