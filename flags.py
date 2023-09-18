#!/usr/bin/env python3
from guizero import App, Picture, Text, TextBox, PushButton
from random import choice
from os import listdir


def setImageName(directory):
    imageName = choice(listdir(directory))
    image = directory + imageName
    return [imageName, image]


def makeWidget(imageName, image):
    app = App(title="Guess the Flag", width=300, height=400)
    Text(app, imageName.strip(".jpg"))  # cheat
    flag = Picture(app, image, width=150, height=100)
    Text(app, "What country does this flag represent?")
    inputData = TextBox(app)
    PushButton(app, text="Submit", command=guess)
    app.display()


def guess(inputData, imageName):
    if inputData.value.lower() == imageName.strip(".jpg").lower():
        print("correct!")
    else:
        print("Try again!")


def runGame():
    vars = setImageName("flags/")
    makeWidget(vars[0], vars[1])


if __name__ == "__main__":
    runGame()
