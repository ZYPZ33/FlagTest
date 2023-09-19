#!/usr/bin/env python3
from guizero import App, Picture, Text, TextBox, PushButton
from random import choice
from os import listdir

directory = "flags/"
points = 0


def setImageName(directory):
    imageName = choice(listdir(directory))
    image = directory + imageName
    return [imageName, image]


def makeWidget(imageName, image):
    app = App(title="Guess the Flag", width=300, height=400)
    scores = Text(app, f"Score: {points}")
    cheat = Text(app, imageName.strip(".jpg"))
    flag = Picture(app, image, width=150, height=100)
    label = Text(app, "What country does this flag represent?")
    inputData = TextBox(app)
    PushButton(app, text="Submit", command=guess)  # stuck here
    app.display()


def guess():
    if imageData.value.lower() == imageName.strip(".jpg").lower():
        imageName = choice(listdir(directory))
    # imageName = choice(listdir(directory))
    # flag.image = directory + imageName
    # cheat.value = imageName.strip(".jpg")
    # label.value = "What country does this flag represent?"
    # points += 1
    # scores.value = f"Score: {points}"
    # else:
    # label.value = "Try again"


def runGame():
    global vars
    vars = setImageName(directory)
    makeWidget(vars[0], vars[1])


if __name__ == "__main__":
    runGame()
