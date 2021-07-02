import random
from tkinter import *
import os
from pprint import pprint
from PIL import Image, ImageTk, ImageDraw, ImageFont

FONT_NAME = "Ariel"
TITLE = True

image_path = './png_print'
image_array = []
current_card = {}

with os.scandir(image_path) as entries:
    for entry in entries:
        if entry.is_file():
            title = " ".join(entry.name.split(".")[0].split("_")[:-1])
            path = f"{image_path}/{entry.name}"
            ml_unit = {
                'flash_card': path,
                'title': title
            }
            image_array.append(ml_unit)


def next_card():
    global current_card, card_back
    print(card_back.height)
    print(card_back.width)
    current_card = random.choice(image_array)
    def_text.config(text="")
    def_text.config(text=current_card['title'])
    card_image_label.config(image=card_back)


def flip_card():
    global current_card, card_image_label
    print(current_card)
    new_image = PhotoImage(file=current_card['flash_card'])
    new_image = new_image.subsample(2, 2)
    card_image_label.config(image=new_image)
    card_image_label.image = new_image


window = Tk()
window.title("Machine Learning Flashcards")
window.config(padx=20, pady=10, bg="white",
              cursor="hand2")

flip_timer = window.after(500, func=next_card)


def_text = Label(text='Text', bg='grey')
def_text.grid(column=0, row=0, columnspan=2)


card_back = PhotoImage(file='./images/card_back.png')
card_image_label = Label(image=card_back)
card_image_label.grid(column=0, row=1, columnspan=2)


flip_image = PhotoImage(file='./images/flip-icon-4.jpg')
flip_image = flip_image.subsample(8, 8)
flip_button = Button(image=flip_image, highlightthickness=0, fg='black',
                     bg='black', command=flip_card)
flip_button.grid(row=2, column=0)

next_image = PhotoImage(file='./images/next.png')
next_image = next_image.subsample(30, 30)
next_button = Button(image=next_image, highlightthickness=0,
                     bg='black', command=next_card)
next_button.grid(row=2, column=1)

window.mainloop()
