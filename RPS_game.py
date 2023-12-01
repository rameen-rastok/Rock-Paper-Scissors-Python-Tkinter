import random
import sys
from tkinter import *
import RPS_game

try:
    with open("rps_save.txt", "r") as save_file:
        score_saves = save_file.read()
        saved_scores = eval(score_saves)
        player_score = saved_scores["player score"]
        computer_score = saved_scores["computer score"]
except FileNotFoundError:
    player_score = 0
    computer_score = 0

def play_again():

    options = ["Rock", "Paper", "Scissors"]
    computer = random.choice(options)
    print(computer)

    window = Tk()
    window.geometry("800x700")
    window.config(background="black")
    window.title("Rock, Paper, Scissors Game")

    def play_more():
        window.destroy()
        print("Play Another Round")
        play_again()

    def endGame():
        saved_score = {"player score":RPS_game.player_score, "computer score":RPS_game.computer_score}
        with open("rps_save.txt", "w") as saving_score:
            saving_score.write(str(saved_score))
        window.destroy()
        sys.exit()

    def reset_score():
        RPS_game.player_score = 0
        RPS_game.computer_score = 0
        saved_score = {"player score":RPS_game.player_score, "computer score":RPS_game.computer_score}
        with open("rps_save.txt", "w") as saving_score:
            saving_score.write(str(saved_score))
        window.destroy()
        print("Play Another Round")
        play_again()

    def submit():
        global player
        player = entry_box.get()

        if player == computer:
            print("Draw")
            label.config(text="It is a DRAW!!!")
            RPS_game.computer_score += 1
            RPS_game.player_score += 1
            label.config(text="YOU LOST!!!!!")
        elif player == "Rock" and computer == "Paper" or player == "Paper" and computer == "Scissors" or player == "Scissors" and computer == "Rock":
            print("You Lose!")
            label.config(text="YOU LOST!!!!!")
            RPS_game.computer_score += 1
        elif player == "Rock" and computer == "Scissors" or player == "Paper" and computer == "Rock" or player == "Scissors" and computer == "Paper":
            print("You Win!")
            label.config(text="YOU WIN!!!")
            RPS_game.player_score += 1
        elif player != "Rock" or "Paper" or "Scissors":
            print("Not correct term!")
            label.config(text="Incorrect Term Entered")

        play_again_button = Button(window, text="Play Again?", font=("Times New Roman", 20), fg="#00FF00",
                               bg="#000000", activeforeground="#00FF00", activebackground="#000000",
                               relief=RAISED, bd=12, command=play_more)
        play_again_button.place(x=300, y=600)

    label = Label(window, font=("Times New Roman", 24), text="Enter Rock or Paper or Scissors",
                  fg="#00FF00", bg="#000000",
                  relief=RAISED, bd=12)
    label.pack(side=TOP)

    label_2 = Label(window, font=("Times New Roman", 24), text="Player Score: " + str(player_score),
                  fg="#00FF00", bg="#000000",
                  relief=RAISED, bd=12)
    label_2.place(x=300, y=400)

    label_3 = Label(window, font=("Times New Roman", 24), text="Computer Score: " + str(computer_score),
                  fg="#00FF00", bg="#000000",
                  relief=RAISED, bd=12)
    label_3.place(x=290, y=500)

    entry_box = Entry(window,
                      font=("Times New Roman", 20), fg="#00FF00",
                      bg="#000000", insertbackground="#00FF00",
                      relief=RAISED, bd=12)
    entry_box.place(x=250, y=200)

    submit_button = Button(window, text="Submit", font=("Times New Roman", 20), fg="#00FF00",
                           bg="#000000", activeforeground="#00FF00", activebackground="#000000",
                           relief=RAISED, bd=12, command=submit)
    submit_button.place(x=260, y=280)

    reset_button = Button(window, text="Reset Score", font=("Times New Roman", "20"), fg="#00FF00",
                          bg="#000000", activeforeground="#00FF00", activebackground="#000000",
                          relief=RAISED, bd=12, command=reset_score)
    reset_button.place(x=400, y=280)

    exit_button = Button(window, text="Exit", font=("Times New Roman", 20), fg="#00FF00",
                         bg="#000000", activeforeground="#00FF00", activebackground="#000000",
                         relief=RAISED, bd=12, command=endGame)
    exit_button.place(x=700, y=0)

    window.mainloop()

play_again()