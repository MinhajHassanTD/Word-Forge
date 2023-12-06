import tkinter as tk
import random
import tkinter.messagebox

# The Following Variables are updated repeatedly in the whole file.
global answer
global attempts
global finish
global wincheck
global alphabets
global font
from tkinter import font

attempts = 6
finish = True
wincheck = None
alphabets = {'used': [], 'correct': []}
answer = ''

# Function extract users input and gives relative information to user.
def entry_update():
    global answer
    global attempts
    global finish
    global wincheck

    word = entry_user.get().upper()
    entry_user.delete(0, tk.END)
    if finish == True and attempts > 0:
        if len(word) != len(answer):
            show_message(f'ERROR : GUESS AGAIN\nWITH CORRECT LENGTH {len(answer)}.')
        elif not word.isalpha():
            show_message(f'ERROR : GUESS AGAIN\nWITH ONLY ALPHABETS.')
        else:
            if word == answer:
                wincheck = True
                play_again()
                finish = False
            elif word != answer:
                if attempts > 1:
                    attempts -= 1
                    show_message(f'GUESS AGAIN!\nYOU HAVE {attempts} ATTEMPTS REMAINING.')
                else:
                    wincheck = False
                    play_again()
                    finish = False
            check_guess(word)

# Function Takes the Users Input and Shows relevant Output in frame.
def check_guess(word):
    global answer
    global finish
    global alphabets

    val = []

    frame = tk.Frame(master = frame_guess)
    frame.pack()
    for i in range(len(word)):
        if word[i] == answer[i]:
            val.append(word[i])
            label = tk.Label(master = frame ,text = word[i].upper() , font = ('Helvetica', 32, 'bold'), bg = '#4CAF50', fg = 'white')
            if word[i] not in alphabets['correct']:
                alphabets['correct'].append(word[i])
        elif word[i] in answer:
            if answer.count(word[i]) == 1 and word [i] not in val:
                val.append(word[i])
                label = tk.Label(master = frame ,text = word[i].upper() , font = ('Helvetica', 32, 'bold'), bg = '#FFEB3B', fg = 'white')
                if word[i] not in alphabets['used']:
                    alphabets['used'].append(word[i])
            elif answer.count(word[i]) > 1:
                val.append(word[i])
                label = tk.Label(master = frame ,text = word[i].upper() , font = ('Helvetica', 32, 'bold'), bg = '#FFEB3B', fg = 'white')
                if word[i] not in alphabets['used']:
                    alphabets['used'].append(word[i])
            else:
                val.append(word[i])
                label = tk.Label(master = frame ,text = word[i].upper() , font = ('Helvetica', 32, 'bold'), bg = '#9E9E9E', fg = 'white')
                if word[i] not in alphabets['used']:
                    alphabets['used'].append(word[i])
        else:
            val.append(word[i])
            label = tk.Label(master = frame ,text = word[i].upper(), font = ('Helvetica', 32, 'bold'), bg = '#9E9E9E', fg = 'white')
            if word[i] not in alphabets['used']:
                alphabets['used'].append(word[i])
        
        label.columnconfigure(i, weight = 5 )
        
        label.grid(row = 0, column = i, ipady = 5)

# Function Creates a PopUp Window with a Message.
def show_message(word):

    win_message = tk.Toplevel(master = window, relief = 'raised', bg = '#1E1E1E', bd= 5)

    label = tk.Label(win_message, text = word, font=("Helvetica", 24, 'bold'), bg = '#1E1E1E', fg = 'white')
    label.pack(padx=20, pady=20)

    win_message.update_idletasks()
    width = win_message.winfo_width()
    height = win_message.winfo_height()
    x = (window.winfo_width() - width) // 2
    y = (window.winfo_height() - height - 50) // 2

    win_message.geometry(f"+{window.winfo_x() + x}+{window.winfo_y() + y}")

    win_message.after(1200, win_message.destroy)

# Function Gives User option to Restart Game.
def play_again():
    global answer
    global attempts
    global finish
    global wincheck

    win_play_again = tk.Toplevel(master=window, relief='raised', bg='#1E1E1E', bd=5)

    if wincheck == False:
        label_play_again = tk.Label(win_play_again, text= f'YOU LOSE! THE ANSWER WAS {answer}.', font=("Helvetica", 20, 'bold'),
                                    bg='#1E1E1E', fg='white')
        label_play_again.pack(padx=20, pady=20)

    elif wincheck == True:
        label_play_again = tk.Label(win_play_again, text= f'YOU WIN! THE ANSWER WAS {answer}.', font=("Helvetica", 20, 'bold'),
                                    bg='#1E1E1E', fg='white')
        label_play_again.pack(padx=20, pady=20)

    btn_yes = tk.Button(win_play_again, text="Restart", font=("Helvetica", 16), command = reset_button)
    btn_yes.pack(pady=10)

    btn_no = tk.Button(win_play_again, text="Quit", font=("Helvetica", 16), command = window.destroy)
    btn_no.pack(pady=10)

    win_play_again.update_idletasks()
    width = win_play_again.winfo_width()
    height = win_play_again.winfo_height()
    x = (window.winfo_width() - width) // 2
    y = (window.winfo_height() - height - 50) // 2

    win_play_again.geometry(f"+{window.winfo_x() + x}+{window.winfo_y() + y}")

    win_play_again.after(5000, win_play_again.destroy)

# A helper function which is used by play_again to restart game.
def reset_button():
    global answer
    global attempts
    global finish
    global frame_guess
    global wincheck
    global alphabets

    # Reset Important Variables
    attempts = 6
    finish = True
    wincheck = None
    alphabets = {'used': [], 'correct': []}

    # Clear the Previous Guess in Frame 2
    frame_guess.destroy()
    frame_guess = tk.Frame(master=window, relief='sunken', width=1200, height=440, bg='#1E1E1E')
    frame_guess.grid(row = 1, column = 0, sticky = 'nsew')  

    difficulty_setter() 

# Function Used to Set Difficulty in the start by User.
def difficulty_setter():
    global font

    frame = tk.Frame(master = frame_guess,  bg = '#1E1E1E')
    frame.pack()
    
    label = tk.Label(master = frame, text = 'SELECT YOUR DIFFICULTY', font= font_difficulty, bg = '#1E1E1E', fg = 'white')
    label.pack(padx=20, pady=20)

    btn_easy = tk.Button(master = frame, text="EASY", font=("Helvetica", 16), command = lambda: [select(1), frame.destroy()])
    btn_easy.pack(pady=10)
    
    btn_medium = tk.Button(master = frame, text="MEDIUM", font=("Helvetica", 16), command = lambda: [select(2), frame.destroy()])
    btn_medium.pack(pady=10)

    btn_hard = tk.Button(master = frame, text="HARD", font=("Helvetica", 16), command = lambda: [select(3), frame.destroy()])
    btn_hard.pack(pady=10)

    btn_rules = tk.Button(master=frame, text="GAME RULES", font=("Helvetica", 16), command=show_rules_popup)
    btn_rules.pack(pady=10)

# Helper Function which is used by difficulty_setter which selects the word difficulty.
def select(num):
    global answer

    if num == 1:
        lst = []
        f = open(r'./source/4-wordlist.txt')
        lst = f.readlines()
        f.close()
        answer = (lst[random.randint(0, 2252)]).strip()
        answer = answer.upper()
    elif num == 2:
        lst = []
        f = open(r'./source/5-wordlist.txt')
        lst = f.readlines()
        f.close()
        answer = (lst[random.randint(0, 5757)]).strip()
        answer = answer.upper()
    elif num == 3:
        lst = []
        f = open(r'./source/6-wordlist.txt')
        lst = f.readlines()
        f.close()
        answer = (lst[random.randint(0, 2499)]).strip()
        answer = answer.upper()

# Helper function used by difficulty_setter which shows user game rules.
def show_rules_popup():
    rules_text = (
        "Welcome to Word Forge!\n\n"
        "Rules:\n"
        "1. You'll be given a secret word that you need to guess.\n"
        "2. You'll have 6 attempts to guess correctly.\n"
        "3. Enter your guesses, and we'll provide feedback:\n"
        "   - Green: Correct letter in the correct position.\n"
        "   - Yellow: Correct letter in the incorrect position.\n"
        "   - Grey: Incorrect letter.\n\n"
        "Difficulty Levels:\n"
        " - Easy (4 words): Great for beginners.\n"
        " - Medium (5 words): A bit more challenge.\n"
        " - Hard (6 words): The ultimate word-guessing challenge!\n\n"
        "Tips:\n"
        " - Pay attention to the feedback after each guess.\n"
        " - Use deductive skills to eliminate possibilities.\n"
        " - Keep refining your guesses until you unveil the secret word!\n\n"
        "Get ready to embark on a word-guessing adventure with Word Forge. Good luck!"
    )

    tkinter.messagebox.showinfo("Word Forge Game Rules", rules_text)

# Function Displays the Used Alphabets
def show_used_letters():
    global alphabets
    used = ', '.join(sorted(alphabets['used']))
    correct = ', '.join(sorted(alphabets['correct']))
    info_text = (
        "Here is the Information Regarding Used Letters.\n\n"
        f"Used Letters : {used}\n"
        f"Correct Letters : {correct}\n"
        )

    tkinter.messagebox.showinfo("Letter Information", info_text)

# Initialize the Main Screen
window = tk.Tk()
window.title('WORD FORGE')

font_heading = font.Font(family="ArcadeClassic", size=48)
font_difficulty = font.Font(family="ArcadeClassic", size=32)

# Window Size Setting
window_width = 1200
window_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height - 50) // 2

# Centers the Window on the Device Screen
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Can Resize the Window / Main Screen
window.resizable(True, True)

# Control the Minimim Resize of Window
window.minsize(850 ,600)

# Sets up the Grid in the Main Screen for the 3 Frames
window.rowconfigure(0, weight = 0)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 0)
window.columnconfigure(0, weight = 1)

# The 3 Frames
frame_heading = tk.Frame(master = window, relief = 'raised', bg = '#1E1E1E', bd= 5)
frame_heading.grid(row = 0, column = 0, sticky = 'nsew')

frame_guess = tk.Frame(master = window, relief = 'sunken', width = 1200, height = 440, bg = '#1E1E1E')
frame_guess.grid(row = 1, column = 0, sticky = 'nsew')

frame_entry = tk.Frame(master = window, width= 1200, height = 80, relief = 'raised', bg = '#1E1E1E', bd= 5)
frame_entry.grid(row = 2, column = 0, sticky = 'nsew')

# Frame which contains the heading 'Word Forge'
lbl_heading = tk.Label(master = frame_heading, text = 'WORD FORGE', font = font_heading, bg = '#1E1E1E', fg = 'white')
lbl_heading.pack(fill = tk.BOTH)

# Frame which has the entry place and button for the user to guess
lbl_enterword = tk.Label(master = frame_entry, text = 'Enter Word', font = ('Helvetica, 20'), width = 20, bg = 'light grey', fg = 'black' )
entry_user = tk.Entry(master=frame_entry, font = ('Helvetica', 20), width = 20, bg = 'light grey', fg = 'black')
btn_submit = tk.Button(master=frame_entry, text = 'SUBMIT', font = ('Helvetica', 20), command = entry_update)
btn_show = tk.Button(master=frame_entry, text = 'LETTER INFO', font = ('Helvetica', 20), command = show_used_letters)

lbl_enterword.grid(row = 0, column = 0, padx=10, pady=10, sticky = 'w')
entry_user.grid(row = 0, column = 1, padx=10, pady=10, sticky = 'w')
btn_submit.grid(row = 0, column = 2, padx=10, pady=10, sticky = 'w')
btn_show.grid(row = 0, column = 3, padx=10, pady=10, sticky = 'w')

# The following function called for user to choose difficulty
difficulty_setter()

window.mainloop()
