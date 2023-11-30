from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, foreground="white", font=("Arial", 15))
        self.score_label.grid(column=1, row=0)

        # Canvas Configuration
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.timer_text = self.canvas.create_text(
            150,
            125,
            text="Amazon acquired Twitch in \nAugust 2014 for $970 million \ndollars.",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # True (Green Check Mark) button configuration
        true_img_button = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img_button, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        # False (Red Box/white X) button configuration
        false_img_button = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img_button, highlightthickness=0)
        self.false_button.grid(column=1, row=2)




        self.window.mainloop()

