from tkinter import *
import os
from pprint import pprint

FONT_NAME = "Ariel"
CARD_EXPLAINATION = False


def flipcard():
    global CARD_EXPLAINATION, card_info
    if CARD_EXPLAINATION == False:
        canvas.delete('img')
        canvas.itemconfig(language_text, text="english", fill='white')
        CARD_EXPLAINATION = TRUE
    else:
        card_info = canvas.create_image(500, 320, image=card_front, tag='img')
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

language_text = canvas.create_text(400, 150, text="German", fill='black',
                                   font=(FONT_NAME, 40, 'italic'))

card_front = PhotoImage(file='./png_print/AIC_print.png')
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


window.mainloop()
