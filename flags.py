#!/usr/bin/env python3
from guizero import App, Picture, Text, TextBox, PushButton
from random import choice
from os import listdir

directory = "flags/"
points = 0
turns = 10

images = listdir(directory)

imageName = choice(images)
images.remove(imageName)
image = directory + imageName


def guess():
    global imageName, images, points, turns
    if inputData.value.lower() == imageName.strip(".jpg").lower() and turns != 0:
        if len(images) > 0:
            imageName = choice(images)
            images.remove(imageName)
            flag.image = directory + imageName
            # cheat.value = imageName.strip(".jpg")
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
            label.value = "Game over"
        elif turns > 1:
            label.value = "Try again"
            turns -= 1
        else:
            label.value = "Game over"
        scores.value = f"Score: {points} Turns:{turns}"


app = App(title="Guess the Flag", width=300, height=400)
scores = Text(app, f"Score: {points} Turns:{turns}")
# cheat = Text(app, imageName.strip(".jpg"))
flag = Picture(app, image, width=150, height=100)
label = Text(app, "What country does this flag represent?")
inputData = TextBox(app)
button = PushButton(app, text="Submit", command=guess)  # stuck here
app.display()
