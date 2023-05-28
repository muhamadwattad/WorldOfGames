from flask import Flask

SCORES_FILE = "scores.txt"


def read_score():
    try:
        with open(SCORES_FILE, "r") as file:
            score = file.read()
            return score.strip()
    except IOError as e:
        return str(e)


def score_server():
    app = Flask("WorldOfGames")

    @app.route("/")
    def show_score():
        score = read_score()
        if score.isdigit():
            html = f"""
            <html>
            <head>
            <title>Scores Game</title>
            </head>
            <body>
            <h1>The score is <div id="score">{score}</div></h1>
            </body>
            </html>
            """
        else:
            html = f"""
            <html>
            <head>
            <title>Scores Game</title>
            </head>
            <body>
            <h1><div id="score" style="color:red">{score}</div></h1>
            </body>
            </html>
            """
        return html

    app.run()


score_server()
