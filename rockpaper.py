from tkinter import *
import random

choice = ["Rock", "Paper", "Scissors"]
root = Tk()
root.geometry("800x500")
root.title(" Rock Paper Scissors Game")
player_score = 0
computer_score = 0


def game(player_choice):
    global player_score, computer_score, select_lbl1, select_lbl2
    computer_choice = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_choice)
    if player_choice == "Rock" and computer_choice == "Scissors":
        player_score += 1
    elif player_choice == "Paper" and computer_choice == "Rock":
        player_score += 1
    elif player_choice == "Scissors" and computer_choice == "Paper":
        player_score += 1
    elif player_choice == computer_choice:
        pass
    else:
        computer_score += 1
    select_lbl1.destroy()
    select_lbl2.destroy()

    select_lbl1 = Label(root, text="Your selection: " + player_choice, font=("Calibri", 17))
    select_lbl1.place(x=190, y=330)
    select_lbl2 = Label(root, text="Computer selection: " + computer_choice, font=("Calibri", 17))
    select_lbl2.place(x=170, y=390)
    score_lbl1 = Label(root, text="Your score: " + str(player_score), font=("Calibri", 17))
    score_lbl1.place(x=490, y=330)
    score_lbl2 = Label(root, text="Computer score: " + str(computer_score), font=("Calibri", 17))
    score_lbl2.place(x=470, y=390)


title_label = Label(root, text="Rock Paper Scissors", font=("Calibri", 30), fg="grey").place(x=240, y=0)
start_label = Label(root, text="Let's Start the Game...", font=("Calibri", 15), fg="green").place(x=310, y=55)
option_lbl = Label(root, text="Your Options:", font=("Calibri", 15), fg="grey").place(x=90, y=120)
score_lbl = Label(root, text="Score:", font=("Calibri", 17), fg="grey").place(x=110, y=300)

select_lbl1 = Label(root, text="Your Selection: ---", font=("Calibri", 17))
select_lbl1.place(x=190, y=330)
select_lbl2 = Label(root, text="Computer Selection: ---", font=("Calibri", 17))
select_lbl2.place(x=170, y=390)


score_lbl1 = Label(root, text="Your Score: -", font=("Calibri", 17)).place(x=490, y=330)
score_lbl2 = Label(root, text="Computer Score: -", font=("Calibri", 17)).place(x=470, y=390)

b1 = Button(root, text="Rock", font=("Calibri", 18), width=10, bg="light pink", command=lambda: game("Rock"))
b1.place(x=220, y=170)
b2 = Button(root, text='Paper', font=("Calibri", 18), width=10, bg="light grey", command=lambda: game("Paper"))
b2.place(x=385, y=170)
b3 = Button(root, text='Scissors', font=("Calibri", 18), width=10, bg="light blue", command=lambda: game("Scissors"))
b3.place(x=550, y=170)

root.mainloop()