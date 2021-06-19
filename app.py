from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    table_size = 8
    game_board = [[0 for _ in range(table_size)] for _ in range(table_size)]
    game_board[0][0] = 1
    game_board[0][1] = 1
    game_board[0][2] = 1

    game_board[4][5] = 1
    game_board[4][6] = 1
    game_board[4][7] = 1

    game_board[2][3] = 1
    game_board[3][3] = 1
    game_board[4][3] = 1

    return render_template('home.html', table_size=table_size, str=str, game_board=game_board)


if __name__ == '__main__':
    app.run(debug=True)
