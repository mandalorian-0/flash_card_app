import tkinter
import pandas as pd
from pathlib import Path
from functools import partial

from cards import utils

BACKGROUND_COLOR = "#B1DDC6"
ROOT = Path(__file__).parent
IMAGES = ROOT.joinpath("images")
DATA_PATH = ROOT.joinpath("data") / "french_words.csv"

timer_id = None

data = pd.read_csv(DATA_PATH)
data_list = data.to_dict("records")
current_card = {}

# ---------------- Logic -------------------
def next_card():
    global current_card
    current_card = utils.random_word(data_list)
    canvas.itemconfig(card_bg, image=front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

def flip_card():
    canvas.itemconfig(card_bg, image=back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

    window.after_cancel(timer_id)

# ---------------- Window setup ----------------------
window = tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.resizable(False, False)

timer_id = window.after(3000, flip_card)

# ---------------- Card back & front background -------------------
back = tkinter.PhotoImage(file=IMAGES.joinpath("card_back.png"))
front = tkinter.PhotoImage(file=IMAGES.joinpath("card_front.png"))


# ---------------- Canvas for flashcard and text -------------------------
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
# card_img = tkinter.PhotoImage(file=IMAGES.joinpath("card_front.png"))
card_bg = canvas.create_image(400, 263, image=front)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 25, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# buttons
is_known_img = tkinter.PhotoImage(file=IMAGES.joinpath("right.png"))
is_not_known_img = tkinter.PhotoImage(file=IMAGES.joinpath("wrong.png"))

wrong_button = tkinter.Button(image=is_not_known_img, highlightthickness=0, border=0, cursor="hand2")
right_button = tkinter.Button(image=is_known_img, highlightthickness=0, border=0, cursor="hand2")

wrong_button.config(command=next_card)
right_button.config(command=next_card)

wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()