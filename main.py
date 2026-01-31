import tkinter
import pandas as pd
from pathlib import Path
from functools import partial

from cards import utils

BACKGROUND_COLOR = "#B1DDC6"
ROOT = Path(__file__).parent
IMAGES = ROOT.joinpath("images")
DATA_PATH = ROOT.joinpath("data") / "french_words.csv"

# read data
data = pd.read_csv(DATA_PATH)

# transform into list
data_list = data.to_dict("records")

# window setup
window = tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.resizable(False, False)


# canvas for flashcard and text
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
card_background = tkinter.PhotoImage(file=IMAGES.joinpath("card_front.png"))
canvas.create_image(400, 263, image=card_background)

language = canvas.create_text(400, 150, text="French", font=("Arial", 25, "italic"))
word = canvas.create_text(400, 263, text="trouve", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# buttons
is_known_img = tkinter.PhotoImage(file=IMAGES.joinpath("right.png"))
is_not_known_img = tkinter.PhotoImage(file=IMAGES.joinpath("wrong.png"))

wrong_button = tkinter.Button(image=is_not_known_img, highlightthickness=0, border=0, cursor="hand2")
right_button = tkinter.Button(image=is_known_img, highlightthickness=0, border=0, cursor="hand2")

wrong_button.config(command=partial(utils.random_word, data_list, canvas, word))
right_button.config(ccommand=partial(utils.random_word, data_list, canvas, word))

wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

window.mainloop()