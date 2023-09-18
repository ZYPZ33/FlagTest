#!/usr/bin/env python3
from guizero import App, Picture, Text, TextBox, PushButton
from random import choice
from os import listdir


def guess():
    return True


directory = "flags/"
imageName = choice(listdir(directory))
image = directory + imageName

app = App(title="Guess the Flag", width=300, height=400)
Text(app, imageName.strip(".jpg"))

flag = Picture(app, image, width=150, height=100)
Text(app, "What country is this flag?")

inputData = TextBox(app)
PushButton(app, text="Submit", command=guess)

app.display()
