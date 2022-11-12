from tkinter import Button, Tk, Canvas, Label, PhotoImage
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"


def csv_read():
    pass


# ---------------------------- BUTTONS CLICK  ------------------------------- #
def right_button_click():
    #current_word = random.choice(keys)
    #print(current_word)
    #print(words_translate[current_word])
    #keys.remove(current_word)
    pass
    


def wrong_button_click():
    #current_word = random.choice(keys)
    #print(current_word)
    #print(words_translate[current_word])
    #keys.remove(current_word)
    pass


def main():
    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Flashy")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
    front_img = PhotoImage(file="images/card_front.png")
    back_img = PhotoImage(file="images/card_back.png")
    canvas.create_image(400, 263, image=front_img)
    canvas.grid(row=0, column=0, columnspan=2, rowspan=2)

    df = pandas.read_csv("data/french_words.csv")
    words_translate = {row[0]: row[1] for (index, row) in df.iterrows()}
    keys = list(words_translate.keys())
    
    # todo change Labels to canvas.create_text

    # canvas.create_text(100,10,fill="darkblue",font="Times 20 italic bold",text="Click the bubbles that are multiples of two.")
    # canvas.update


    # Buttons
    right_image = PhotoImage(file="images/right.png")
    right_button = Button(command=right_button_click, image=right_image, highlightthickness=0)
    right_button.grid(row=2, column=0)
    wrong_image = PhotoImage(file="images/wrong.png")
    wrong_button = Button(command=wrong_button_click, image=wrong_image, highlightthickness=0)
    wrong_button.grid(row=2, column=1)
    # Labels
    title_label = Label(text="Title", font=("Arial", 40, "italic"), bg="white")
    title_label.grid(row=0, column=0)
    title_label.place(x=300, y=150)
    word_label = Label(text="Word", font=("Arial", 60, "bold"), bg="white")
    word_label.grid(row=1, column=0)
    word_label.place(x=300, y=263)

    window.mainloop()


if __name__ == "__main__":
    main()
    csv_read()
