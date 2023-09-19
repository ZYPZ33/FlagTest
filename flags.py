#!/usr/bin/env python3
from guizero import App, Picture, Text, TextBox, PushButton
from random import choice
from os import listdir

directory = "flags/"
points = 0

images = listdir(directory)

imageName = choice(images)
images.remove(imageName)
image = directory + imageName


def guess():
    global imageName, points, images
    if inputData.value.lower() == imageName.strip(".jpg").lower():
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
        scores.value = f"Score: {points}"
        inputData.value = ""
    else:
        label.value = "Try again"


app = App(title="Guess the Flag", width=300, height=400)
scores = Text(app, f"Score: {points}")
# cheat = Text(app, imageName.strip(".jpg"))
flag = Picture(app, image, width=150, height=100)
label = Text(app, "What country does this flag represent?")
inputData = TextBox(app)
button = PushButton(app, text="Submit", command=guess)  # stuck here
app.display()
