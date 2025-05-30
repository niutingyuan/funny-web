import flask
from flask import Flask
import random

app = Flask(__name__)

jokes = [
    "Relationship status? I'll leave the relations to the database.",
    "How do you get the code for the bank vault? You checkout their branch.",
    "How did the developer announce their engagement? They returned true!"
]

@app.get("/")
def tell_a_joke():
    joke = random.choice(jokes)
    return flask.render_template('jokes.html', joke_text=joke)