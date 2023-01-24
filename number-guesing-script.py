# Guessing number APP + GUI
# By NIGHT ERROR -> night.error.go@gmail.com
# -----------------------------------------------------------------------------
# Imports
from random import randint
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from time import sleep
import os

# Fuctions
def save_user_info(name, age, range_option, score):
        #This function saves users info
        try:
                os.mkdir("Info")
        except FileExistsError:
                pass
        file = open("Info\\Users.txt", "a")
        file.write(f"""Name: {name.capitalize()}
Age: {age}
Range: {range_option}
----------------------------------------------------\n""")
        file.close()

def number_generator():
        #this function generates a number in the range given
        global computer_number
        global budget
        budget = int(range_holder.get()[4:7])
        computer_number = randint(1, int(range_holder.get()[4:7]))

def check_number():
        #This function checks the number
        global hints
        global score
        pc_num = computer_number
        user_num = int(guess.get())
        #if the guess is less
        if user_num < pc_num:
                hints.set(hints.get() + 1)
                hints_label.config(text=f"Hints: {hints.get()}")
                hint_label.config(text=f"It's more than {user_num}...", fg="#404040")
                hint_label2.config(text=f"It's between {option_range[0]} to {option_range[5:7]}...")

        #if the guess is more
        elif user_num > pc_num:
                hints.set(hints.get() + 1)
                hints_label.config(text=f"Hints: {hints.get()}")
                hint_label.config(text=f"It's less than {user_num}...", fg="#404040")
                hint_label2.config(text=f"It's between {option_range[0]} to {option_range[5:7]}...")

        #if the guess is True
        elif user_num == pc_num:
                new_score = budget / hints.get()
                score = str(float(score) + new_score)[0:3]
                score_label.config(text=f"Score: {str(score)}")
                hint_label.config(text="Nice job dude!", fg="#3AA20F")
                hint_label2.config(text=f"The number was {user_num}.")
                guess_button.config(state=DISABLED)
                guess_entry.config(state=DISABLED)


def check_input():
        #This function checks the guess input
        global num_range
        number = guess.get()
        num_range = int(range_holder.get()[5:7])

        if not number.isnumeric() or (int(number) > num_range) or (int(number) < 1):
                hint_label.config(text=f"Enter a number 1 to {num_range}", fg="#D41D1D")
        else:
                check_number()


def start_new_game():
        #This function starts a new game with cleared score and stuff
        number_generator()
        try:
                win_game.destroy()
        except Exception:
                pass
        new_game()

score = "0"
def new_game():
        #This function designs the new game page
        global score
        global hints
        global guess
        global win_game
        global hints_label
        global hint_label
        global hint_label2
        global option_range
        global score_label
        global guess_button
        global new_game_button
        global guess_entry

        #Assets for new game
        name = name_holder.get().capitalize()
        age = int(age_holder.get())
        option_range = range_holder.get()
                #Destroy old window
        try:
                win.destroy()
        except Exception:
                pass
                #Create new window
        win_game = Tk()
        icon = ImageTk.PhotoImage(image_res)
        win_game.iconphoto(True, icon)
        win_game.config(bg="#F7F7F7")
        win_game.geometry("350x440")
        win_game.resizable(False, False)
        win_game.title("Guess number")

        #needs
        hints = IntVar()
        hints.set(1)
        guess = StringVar()

        #bases
        Label(win_game, text=f"Welcom {name} :)", font=("Anjoman", 13),
        bg="#F7F7F7", fg="#551D78").pack(anchor=N, padx=5, pady=8)

        score_label = Label(win_game,  text=f"Score: {score}", font=("Anjoman", 15),
                                        bg="#FFFFFF", fg="#551D78",
                                        width=19, height=2, highlightthickness=1, highlightbackground="#B7B7B7")
        score_label.pack(anchor=N, padx=5, pady=3)

        hints_label = Label(win_game,  text=f"Hints: {hints.get()}", font=("Anjoman", 15),
                                        bg="#FFFFFF", fg="#551D78",
                                        width=19, height=2, highlightthickness=1, highlightbackground="#B7B7B7")
        hints_label.pack(anchor=N, padx=5, pady=3)

        #Guess part
        Label(win_game, text="Guess the number", font=("Anjoman", 18),
        bg="#F7F7F7", fg="#551D78").pack(anchor=N, padx=5, pady=10)

        guess_entry = Entry(win_game, font=("Anjoman", 20),
                                        bg="#FFFFFF", fg="#404040",
                                        textvariable=guess)
        guess_entry.pack(anchor=N, padx=7, pady=0, fill=X)

        #hints
        hint_label = Label(win_game, text="Here is the first shot!", font=("Anjoman", 14),
                                        bg="#F7F7F7", fg="#404040")
        hint_label.pack(anchor=N, padx=2, pady=1)

        hint_label2 = Label(win_game, text=f"It's between {option_range[0]} to {option_range[5:7]}...", font=("Anjoman", 11),
                                        bg="#F7F7F7", fg="#404040")
        hint_label2.pack(anchor=N, padx=2, pady=0)

        #Buttons
        guess_button = Button(win_game,
                 bg="#551D78", fg="#FFFFFF", activebackground="#461663", activeforeground="#FFFFFF",
                 text="Guess", font=("Anjoman", 17),
                 height=2, command=check_input)
        guess_button.pack(fill=X, padx=7, pady=6)

        new_game_button = Button(win_game,
                 bg="#DBDBDB", fg="#636363", activebackground="#ECECEC", activeforeground="#636363",
                 text="New game", font=("Anjoman", 15),
                 height=1, relief=RIDGE, highlightthickness=0, highlightbackground="red", command=start_new_game)
        new_game_button.pack(fill=X, padx=7, pady=5)

        win_game.mainloop()

def check_float(number):
        #This function checks if a number is float or not
        try:
                float(number)
                return True
        except Exception:
                return False

def start_game():
        #This function checks user login inputs and calls the new_game()
        global check
        check = 0
        #Check for labels
        if name_holder.get == "" or len(name_holder.get()) < 4:
                name_label.config(fg="#D41D1D")
        else:
                for i in name_holder.get():
                        if i == " ":
                                check += 1
                if check > 3:
                        name_label.config(fg="#D41D1D")
                else:
                        name_label.config(fg="#3AA20F")

        if age_holder.get() == "" or (age_holder.get().isnumeric()) == False or check_float(age_holder) == True:
                age_label.config(fg="#D41D1D")
        else:
                if int(age_holder.get()) > 65 or int(age_holder.get()) < 7:
                        age_label.config(fg="#D41D1D")
                else:
                        age_label.config(fg="#3AA20F")

        #Main check
        if name_holder.get == "" or len(name_holder.get()) < 4 or age_holder.get() == "" or (age_holder.get().isnumeric()) == False or check_float(age_holder) == True:
                pass
        else:
                if int(age_holder.get()) > 65 or int(age_holder.get()) < 7:
                        age_label.config(fg="#D41D1D")
                        for i in name_holder.get():
                                if i == " ":
                                        check += 1
                elif check > 3:
                                name_label.config(fg="#D41D1D")
                else:
                        name_label.config(fg="#3AA20F")
                        age_label.config(fg="#3AA20F")
                        win.update()
                        save_user_info(name_holder.get(), age_holder.get(), range_holder.get(), score)
                        start_new_game()

#----------------------------------------------------------------
        # GUI
win = Tk()
win.title("Guess number")
win.geometry("300x300")
win.config(bg="#F7F7F7")
win.resizable(False, False)
        # Images
image = Image.open("icon.png")
image_res = image.resize((25, 25))
image_tk = ImageTk.PhotoImage(image_res)
win.iconphoto(True, image_tk)

# First inputs
name_holder = StringVar()
age_holder = StringVar()
range_options = ["1 to 10", "1 to 20", "1 to 30", "1 to 40", "1 to 50"]
range_holder = StringVar(win)
range_holder.set(range_options[0])

# Name
name_label = Label(win, text="Enter your name:",
        font=("Anjoman", 15),
        fg="#2B2B2B",
        bg="#F7F7F7")
name_label.pack(anchor=NW, padx=7, pady=8, )

Entry(win, font=("Anhoman", 20),
        bg="#F7F7F7",
        fg="#404040",
        textvariable=name_holder).pack(anchor=N, padx=7, pady=1, fill=X)

# Age
age_label = Label(win, text="Enter your age:",
        font=("Anjoman", 15),
        fg="#2B2B2B",
        bg="#F7F7F7")
age_label.pack(anchor=NW, padx=7, pady=5)

Entry(win, font=("Anhoman", 20),
        bg="#F7F7F7",
        fg="#404040",
        textvariable=age_holder).pack(anchor=N, padx=7, pady=1, fill=X)

# Range
range_label = Label(win, text="Select a range:",
        font=("Anjoman", 15),
        fg="#2B2B2B",
        bg="#F7F7F7")
range_label.pack(anchor=NW, padx=7, pady=5)

range_option_menu = OptionMenu(win, range_holder, *(range_options))
range_option_menu.pack(anchor=N, fill=X, padx=7, pady=1)

# submit button
start_button = Button(win,
        bg="#551D78", fg="#FFFFFF", activebackground="#461663", activeforeground="#FFFFFF",
        text="Start game", font=("Anjoman", 16),
        height=2,
        command=start_game)
start_button.pack(fill=X, padx=7, pady=7)

if __name__ == "__main__":
        win.mainloop()