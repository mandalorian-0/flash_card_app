import random

def random_word(data: list, canvas, word):
    random_index = random.randint(0, len(data) - 1)
    print(data[random_index]["French"])
    canvas.itemconfig(word, text=data[random_index]["French"])
    
