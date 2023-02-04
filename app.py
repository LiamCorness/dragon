import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Dragon:
    def __init__(self, colour, eye_colour):
        self.colour = colour
        self.eye_colour = eye_colour

    def mate(self, other_dragon):
        if self.colour == "red" and other_dragon.colour == "red":
            colour = "red"
        elif self.colour == "blue" and other_dragon.colour == "blue":
            colour = "blue"
        elif self.colour == "green" and other_dragon.colour == "green":
            colour = "green"
        else:
            colour = random.choice([self.colour, other_dragon.colour])

        if self.eye_colour == "red" and other_dragon.eye_colour == "red":
            eye_colour = "red"
        elif self.eye_colour == "blue" and other_dragon.eye_colour == "blue":
            eye_colour = "blue"
        else:
            eye_colour = random.choice(["red", "blue"])

        return Dragon(colour, eye_colour)
    
    def __str__(self):
        return f"{self.colour} dragon with {self.eye_colour} eyes"

@app.template_filter()
def enumerate(iterable, start=0):
    counter = start
    for element in iterable:
        yield counter, element
        counter += 1

dragons = {
    0: Dragon("blue", "blue"),
    1: Dragon("blue", "red"),
    2: Dragon("green", "blue"),
    3: Dragon("green", "red"),
    4: Dragon("red", "red"),
    5: Dragon("red", "blue")
}

@app.route("/")
def index():
    return render_template("index.html", dragons=dragons)

@app.route("/mate", methods=["POST"])
def mate():
    dragon1_id = int(request.form["dragon1"])
    dragon2_id = int(request.form["dragon2"])

    dragon1 = dragons[dragon1_id]
    dragon2 = dragons[dragon2_id]

    offspring = dragon1.mate(dragon2)

    return render_template("mate.html", offspring=offspring)

if __name__ == "__main__":
    app.run(debug=True)
