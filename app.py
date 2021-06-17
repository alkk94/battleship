from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    table_size = 8
    return render_template('home.html', table_size=table_size, str=str)


if __name__ == '__main__':
    app.run(debug=True)
