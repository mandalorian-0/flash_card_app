# 📚 Flashy – A Flashcard App for Learning French → English

## 🎯 Overview  
**Flashy** is a simple, interactive flashcard application built with Python, Tkinter, and Pandas. It helps users learn French-to-English vocabulary by displaying one word at a time. Users can mark a word as "known" (correct) or "not known" (incorrect), and the app automatically updates the list of words to learn.

This app is designed to be lightweight, intuitive, and easy to extend — ideal for educational use or personal language practice.

---

## 🔧 Features

- ✅ **Card flipping**: Automatically flips the card after 3 seconds to show the English translation.
- ✅ **Progress tracking**: Saves learned words to a CSV file (`words_to_learn.csv`) so users can continue from where they left off.
- ✅ **Smooth UI**: Clean, responsive design with a modern card layout and hand cursor on buttons.
- ✅ **Modular structure**: Separates logic (e.g., `cards.utils`) from UI, making it easy to maintain and extend.
- ✅ **Data persistence**: Uses CSV files to store vocabulary and learning progress.

---

## 📂 Project Structure

```
/project
  /data
    /french_words.csv          # Full vocabulary list (source data)
    /words_to_learn.csv        # Words the user hasn't learned yet (progress file)
  /images
    /card_front.png            # Front of card (French)
    /card_back.png             # Back of card (English)
    /right.png                 # "I know" button
    /wrong.png                 # "I don't know" button
  /main.py                     # This file – the core app logic
  /cards/utils.py              # Helper functions (e.g., random word selection)
```

---

## ⚙️ How It Works

1. **Startup**:
   - Loads the full vocabulary from `french_words.csv`.
   - If `words_to_learn.csv` exists, it loads the remaining words to learn.
   - Otherwise, starts with the full list.

2. **Card Display**:
   - A new card is shown every time the user clicks "I don't know" or the timer expires.
   - The front of the card shows the French word.
   - After 3 seconds, it flips to show the English translation.

3. **User Actions**:
   - ✅ Click **"Right"** (✔️): The word is removed from the "to learn" list and saved to the next session.
   - ❌ Click **"Wrong"** (❌): The word stays in the list and is shown again.

4. **Progress**:
   - Words marked as "known" are moved to a separate file (`words_to_learn.csv`).
   - The app starts from the next available word on restart.

---

## 🚀 How to Run

1. Ensure all required libraries are installed:
   ```bash
   pip install pandas
   ```

2. Place the following files in the correct directories:
   - `french_words.csv` → in `/data/french_words.csv`
   - `card_front.png`, `card_back.png`, `right.png`, `wrong.png` → in `/images/`

3. Run the app:
   ```bash
   python main.py
   ```

> 📝 Tip: The app will auto-detect the data and images. No configuration needed!

---

## 🛠️ Extensibility & Improvements

- Add **sound effects** when flipping cards.
- Implement **difficulty levels** (e.g., repeat words after 1 day, 3 days).
- Support **multiple languages** (e.g., Spanish → English).
- Add **statistics** (e.g., words learned, accuracy rate).
- Use **SQLite** or **JSON** for more robust data storage.

---

## 📝 Notes & Best Practices

- `PhotoImage` objects are **not garbage-collected** in Tkinter. Always store them in variables (e.g., `front`, `back`) to avoid crashes.
- The app uses `pandas.to_dict("records")` to convert data into a list of dictionaries for easy access.
- The `after()` and `after_cancel()` functions are used to manage timers and prevent double-flips.
- The `cards.utils` module should contain a function like `random_word(data_list)` to pick a random card.

---

## 📄 License  
MIT

---

## 👤 Author  
Built with ❤️ for language learners.  
Inspired by simple flashcard apps and open-source Python tools.
