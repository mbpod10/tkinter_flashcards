import random
from tkinter import *
import os
from pprint import pprint

FONT_NAME = "Ariel"
CARD_EXPLAINATION = False


image_path = '/Users/brock/Desktop/2021_projects_n_practice/tkinter_flashcards/png_print'
image_object = []
current_card = {}
# canvas = ""


def get_image_object():
    global current_card, image_object
    with os.scandir(image_path) as entries:
        for entry in entries:
            if entry.is_file():
                title = " ".join(entry.name.split(".")[0].split("_")[:-1])
                path = f"./{image_path.split('/')[-1]}/{entry.name}"
                ml_unit = {
                    'flash_card': path,
                    'title': title
                }
                image_object.append(ml_unit)
    # image_object = dict(image_object)
    current_card = random.choice(image_object)


get_image_object()


def flipcard():
    global CARD_EXPLAINATION, card_info, canvas, language_text
    if CARD_EXPLAINATION == False:
        print("CURRENT CARD", current_card)
        language_text = canvas.create_text(400, 150, text=f"{current_card['title']}", fill='black',
                                           font=(FONT_NAME, 40, 'italic'), tag='text')
        # canvas.delete('img')
        canvas.itemconfig(
            language_text, text=f"{current_card['title']}", fill='white')
        CARD_EXPLAINATION = True
    else:
        print("WORKING", current_card)
        # print(canvas)
        # canvas.delete('text')
        # card_front = PhotoImage(file=f'{current_card["flash_card"]}')
        # card_front = card_front.subsample(2, 2)
        # canvas.create_image(500, 320, image=card_front, tag='img')
        canvas.itemconfig(language_text, image=card_front)
        CARD_EXPLAINATION = False


def next_card():
    print('next')


language_text = "h"

window = Tk()
window.title("Machine Learning Flashcards")
window.config(padx=20, pady=10, bg="white",
              cursor="hand2")

canvas = Canvas(width=1000, height=726,
                bg='grey', highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# language_text = canvas.create_text(400, 150, text="German", fill='black',
#                                    font=(FONT_NAME, 40, 'italic'))
language_text = canvas.create_text(400, 150, text=f"{current_card['title']}", fill='black',
                                   font=(FONT_NAME, 40, 'italic'))

card_front = PhotoImage(file=f'{current_card["flash_card"]}')
card_front = card_front.subsample(2, 2)
card_info = canvas.create_image(500, 320, image=card_front, tag='img')

# Buttons
flip_image = PhotoImage(file='./images/flip-icon-4.jpg')
flip_image = flip_image.subsample(8, 8)
flip_button = Button(image=flip_image, highlightthickness=0, fg='black',
                     bg='black', command=flipcard)
flip_button.grid(row=1, column=0)

next_image = PhotoImage(file='./images/next.png')
next_image = next_image.subsample(30, 30)
next_button = Button(image=next_image, highlightthickness=0,
                     bg='black', command=next_card)
next_button.grid(row=1, column=1)


# pprint(image_object)
print(current_card)
window.mainloop()
