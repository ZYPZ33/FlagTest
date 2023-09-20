#!/usr/bin/env python3
from guizero import App, Picture, Text, TextBox, PushButton
from random import choice
from os import listdir
from sys import argv

directory = "flags/"
points = 0
turns = 10

images = listdir(directory)

imageName = choice(images)
images.remove(imageName)
image = directory + imageName


def cheat(imageName):
    if "-l" in argv:
        print(imageName.strip(".jpg"))


def guess():
    global imageName, images, points, turns
    if inputData.value.lower() == imageName.strip(".jpg").lower() and turns != 0:
        if len(images) > 0:
            imageName = choice(images)
            images.remove(imageName)
            flag.image = directory + imageName
            cheat(imageName)
            label.value = "What country does this flag represent?"
        else:
            flag.destroy()
            # cheat.destroy()
            inputData.destroy()
            button.destroy()
            label.value = "You got all the flags right!"
        points += 1
        scores.value = f"Score: {points} Turns:{turns}"
        inputData.value = ""
    else:
        if turns == 1:
            turns -= 1
            label.value = "Game over\nAnswer was: " + imageName.strip(".jpg")
            inputData.destroy()
            button.destroy()
        else:
            label.value = "Try again"
            turns -= 1
        scores.value = f"Score: {points} | Turns:{turns}"


app = App(title="Guess the Flag", width=300, height=400)
scores = Text(app, f"Score: {points} | Turns:{turns}")
cheat(imageName)
flag = Picture(app, image, width=150, height=100)
label = Text(app, "What country does this flag represent?")
inputData = TextBox(app)
button = PushButton(app, text="Submit", command=guess)  # stuck here
app.display()
