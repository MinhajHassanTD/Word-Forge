# Word Forge

Word Forge is a desktop word-guessing game inspired by Wordle, built with Python and Tkinter. Players choose a difficulty level, guess the hidden word in up to 6 attempts, and use color-coded feedback to solve the puzzle.

## Tech Stack

- Python 3
- Tkinter (GUI)
- Standard library modules: `random`, `tkinter.messagebox`
- Text-based word banks in `source/`

## Notable Features

- Three difficulty modes:
	- Easy: 4-letter words
	- Medium: 5-letter words
	- Hard: 6-letter words
- Wordle-style feedback per guess:
	- Green: correct letter in correct position
	- Yellow: correct letter in wrong position
	- Gray: letter not in answer
- 6 attempts per round
- In-app game rules popup
- Letter tracking popup (used letters and confirmed correct letters)
- Restart or quit options at end of each game

## Installation and Run

### 1. Prerequisites

- Python 3.8 or later

### 2. Clone the repository

```bash
git clone https://github.com/MinhajHassanTD/Word-Forge.git
cd Word-Forge
```

### 3. Run the game

```bash
python wordforge.py
```

## Project Structure

```text
Word-Forge/
|- wordforge.py
|- source/
|  |- 4-wordlist.txt
|  |- 5-wordlist.txt
|  \- 6-wordlist.txt
\- README.md
```

## Academic Note

This project was built as a university project (APS Final Project, 2023).
