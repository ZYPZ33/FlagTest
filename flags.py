#!/usr/bin/env python3
from guizero import App, Picture, Text, TextBox, PushButton
from random import choice
from os import listdir

directory = "flags/"
image = directory + choice(listdir(directory))

app = App(title="Guess the Flag", width=300, height=400)

flag = Picture(app, image)
Text(app, "What country is this flag?")

inputData = TextBox(app)
PushButton(app, text="Submit", command=guess)

app.display()
