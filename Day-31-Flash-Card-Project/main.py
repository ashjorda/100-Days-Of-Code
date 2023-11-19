from tkinter import *
from tkinter import messagebox
import os
import pandas as pd
import random

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
BACKGROUND_COLOR = "#B1DDC6"
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
current_card = ""

try:
    df = pd.read_csv("./data/words_to_learn.csv")
    dict_data = df.to_dict(orient="records")
except FileNotFoundError:
    # Read the french_words.csv and turn it int a dataframe. The convert the pairs into a dictionary list
    df = pd.read_csv("./data/french_words.csv")
    df.to_csv("./data/words_to_learn.csv", index=False)
    df = pd.read_csv("./data/words_to_learn.csv")
    dict_data = df.to_dict(orient="records")


# ---------------------------- Flip Flash Card ------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')


# ---------------------------- Button Functionality ------------------------------- #
def is_known():
    global dict_data, df
    current_word_index = df[df['French'] == current_card["French"]].index
    df = df.drop(current_word_index)
    dict_data.remove(current_card)
    df.to_csv('./data/words_to_learn.csv', index=False)
    next_card()


# Select a random French/english word pair from the dict_data dictionary, and remove the word from the dictionary if
# the end user already knows the word pair
def next_card():
    global current_card, flip_timer, df
    try:
        current_card = random.choice(dict_data)
        window.after_cancel(flip_timer)
        canvas.itemconfig(canvas_image, image=card_front_img)
        canvas.itemconfig(card_title, text="French", fill='black')
        canvas.itemconfig(card_word, text=current_card["French"], fill='black')
        flip_timer = window.after(3000, flip_card)
    except IndexError:
        messagebox.showinfo(title=None, message="No more words to learn. ")
        os.remove('./data/words_to_learn.csv')
        exit()


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font='Ariel 40 italic', fill='black')
card_word = canvas.create_text(400, 263, text="", font='Ariel 60 bold', fill='black')
canvas.grid(column=0, row=0, columnspan=2)

# Sets 3second timer, then shows the first card before flipping the card from French to English
flip_timer = window.after(3000, flip_card)
next_card()

# Wrong (Red Box/white X) Button configuration
wrong_img_button = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img_button, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

# Right (Green Check Mark) Button configuration
right_img_button = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img_button, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1, row=1)

# Keeps Tkinter window from disappearing when program starts
window.mainloop()
