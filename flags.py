#!/usr/bin/env python3
from guizero import App, Picture, Text, TextBox, PushButton
from random import choice
from os import listdir
from sys import argv

directory = "flags/"
images = listdir(directory)
imageName = choice(images)
images.remove(imageName)
image = directory + imageName


def guess(inputData, imageName, flag, label, cheat, turncount, scores, points):
    if inputData.value.lower() == cheat.value.lower() and turncount.value != "0":
        if len(images) > 0:
            imageName = choice(images)
            images.remove(imageName)
            flag.image = directory + imageName
            cheat.value = imageName.strip(".jpg")
            label.value = "What country does this flag represent?"
        else:
            flag.destroy()
            inputData.destroy()
            label.value = "You got all the flags right!"
        points += 1
        scores.value = f"Score: {points} Turns:{turncount.value}"
        inputData.value = ""
    else:
        if turncount.value <= "1":
            turncount.value = int(turncount.value) - 1
            label.value = "Game over\nAnswer was: ", cheat.value()
            inputData.destroy()
        else:
            label.value = "Try again"
            turncount.value = int(turncount.value) - 1
        scores.value = f"Score: {points} | Turns: {turncount.value}"


def runGame(points, turns):
    app = App(title="Guess the Flag", width=300, height=400)
    scores = Text(app, f"Score: {points} | Turns: {turns}")
    turncount = Text(app, turns)
    turncount.hide()
    cheat = Text(app, imageName.strip(".jpg"))
    if "-l" not in argv:
        cheat.hide()
    flag = Picture(app, image, width=150, height=100)
    label = Text(app, "What country does this flag represent?")
    inputData = TextBox(app)
    PushButton(
        app,
        text="Submit",
        command=guess,
        args=[
            inputData,
            imageName,
            flag,
            label,
            cheat,
            turncount,
            scores,
            points,
        ],
    )
    app.display()


if __name__ == "__main__":
    runGame(0, 10)
