from flask import Flask
import random

app = Flask(__name__)

jokes = [
    "Relationship status? I'll leave the relations to the database.",
    "How do you get the code for the bank vault? You checkout their branch.",
    "How did the developer announce their engagement? They returned true!"
]

@app.get("/")
def hello_world():
    joke = random.choice(jokes)
    return f"<p>{joke}</p>"