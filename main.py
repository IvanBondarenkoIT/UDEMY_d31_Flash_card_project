from tkinter import Button, Tk, Canvas, Label, PhotoImage
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
words_dict = df.to_dict(orient="records")
current_word = {}


# ---------------------------- BUTTONS CLICK  ------------------------------- #
def right_button_click():
    if len(words_dict) == 1:
        canvas.itemconfig(card_title, text="Сongratulations", fill="white")
        canvas.itemconfig(card_word, text="You learned all", fill="white")
    else:
        words_dict.remove(current_word)
        wrong_button_click()
        _data = pandas.DataFrame(words_dict)
        _data.to_csv("data/words_to_learn.csv", index=False)





def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")


def wrong_button_click():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(words_dict)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")
    # canvas.update()
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2, rowspan=2)

card_title = canvas.create_text(400, 150, fill="black", font="Arial 40 italic", text="")
card_word = canvas.create_text(400, 263, fill="black", font="Arial 60 bold", text="")
canvas.update()

# Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(command=right_button_click, image=right_image, highlightthickness=0)
right_button.grid(row=2, column=0)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(command=wrong_button_click, image=wrong_image, highlightthickness=0)
wrong_button.grid(row=2, column=1)

wrong_button_click()

window.mainloop()

